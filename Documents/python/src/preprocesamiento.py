"""
Módulo de preprocesamiento de datos para la app de citas.
Contiene funciones para cargar y limpiar datos de usuarios e interacciones.
"""

import pandas as pd
import json

def cargar_datos(ruta_usuarios, ruta_interacciones):
    # Cargar usuarios
    df_usuarios = pd.read_csv(ruta_usuarios, encoding='utf-8')
    
    # Limpiar y convertir edad a numérico
    df_usuarios['edad'] = pd.to_numeric(df_usuarios['edad'], errors='coerce')
    df_usuarios = df_usuarios.dropna(subset=['edad'])  # Eliminar filas con edades no válidas
    df_usuarios['edad'] = df_usuarios['edad'].astype(int)  # Convertir a enteros
    
    # Cargar interacciones
    with open(ruta_interacciones, 'r', encoding='utf-8') as f:
        data = json.load(f)
    df_interacciones = pd.DataFrame(data)
    
    # Convertir fecha a datetime
    df_interacciones['fecha'] = pd.to_datetime(df_interacciones['fecha'])
    
    return df_usuarios, df_interacciones

def manejar_nulos(df, columna):
    """
    Reemplaza los valores nulos en la columna especificada con 'Sin información'.
    
    Args:
        df (pd.DataFrame): DataFrame a procesar
        columna (str): Nombre de la columna a limpiar
    
    Returns:
        pd.DataFrame: DataFrame con valores nulos manejados
    """
    if columna in df.columns:
        df[columna] = df[columna].fillna('Sin información')
    return df

def estandarizar_texto(df, columna):
    """
    Convierte a minúsculas y quita espacios extra en la columna de texto.
    
    Args:
        df (pd.DataFrame): DataFrame a procesar
        columna (str): Nombre de la columna a estandarizar
    
    Returns:
        pd.DataFrame: DataFrame con texto estandarizado
    """
    if columna in df.columns and df[columna].dtype == 'object':
        # Quitar espacios al inicio y final, convertir a minúsculas
        df[columna] = df[columna].str.strip().str.lower()
    return df

def limpieza_especifica(df, columna):
    """
    Asegura que los valores estén uniformes (convertidos a mayúsculas).
    Útil para categorías como estado, tipo, etc.
    
    Args:
        df (pd.DataFrame): DataFrame a procesar
        columna (str): Nombre de la columna a limpiar
    
    Returns:
        pd.DataFrame: DataFrame con valores uniformes
    """
    if columna in df.columns and df[columna].dtype == 'object':
        # Convertir a MAYÚSCULAS y quitar espacios
        df[columna] = df[columna].str.upper().str.strip()
    return df

def validar_datos(df_usuarios, df_interacciones):
    """
    Valida la integridad de los datos cargados.
    
    Args:
        df_usuarios (pd.DataFrame): DataFrame de usuarios
        df_interacciones (pd.DataFrame): DataFrame de interacciones
    
    Returns:
        dict: Diccionario con resultados de validación
    """
    validacion = {
        'usuarios_validos': True,
        'interacciones_validas': True,
        'errores': []
    }
    
    # Validar usuarios
    if df_usuarios.empty:
        validacion['usuarios_validos'] = False
        validacion['errores'].append('DataFrame de usuarios está vacío')
    
    columnas_requeridas_usuarios = ['id_usuario', 'nombre_usuario', 'edad']
    for col in columnas_requeridas_usuarios:
        if col not in df_usuarios.columns:
            validacion['usuarios_validos'] = False
            validacion['errores'].append(f'Columna requerida faltante en usuarios: {col}')
    
    # Validar interacciones
    if df_interacciones.empty:
        validacion['interacciones_validas'] = False
        validacion['errores'].append('DataFrame de interacciones está vacío')
    
    columnas_requeridas_interacciones = ['id_interaccion', 'id_usuario', 'tipo', 'match']
    for col in columnas_requeridas_interacciones:
        if col not in df_interacciones.columns:
            validacion['interacciones_validas'] = False
            validacion['errores'].append(f'Columna requerida faltante en interacciones: {col}')
    
    return validacion

def limpiar_datos_completo(df_usuarios, df_interacciones):
    """
    Aplica todas las funciones de limpieza a los DataFrames.
    
    Args:
        df_usuarios (pd.DataFrame): DataFrame de usuarios sin limpiar
        df_interacciones (pd.DataFrame): DataFrame de interacciones sin limpiar
    
    Returns:
        tuple: (df_usuarios_limpio, df_interacciones_limpio)
    """
    # Limpiar usuarios
    df_usuarios = manejar_nulos(df_usuarios, 'biografia')
    df_usuarios = estandarizar_texto(df_usuarios, 'intereses')
    df_usuarios = estandarizar_texto(df_usuarios, 'nombre_usuario')
    df_usuarios = estandarizar_texto(df_usuarios, 'ciudad')
    
    # Limpiar interacciones
    df_interacciones = limpieza_especifica(df_interacciones, 'tipo')
    
    # Convertir columna match a booleano si es string
    if df_interacciones['match'].dtype == 'object':
        df_interacciones['match'] = df_interacciones['match'].map({
            'true': True, 'True': True, 'TRUE': True,
            'false': False, 'False': False, 'FALSE': False
        })
    
    return df_usuarios, df_interacciones