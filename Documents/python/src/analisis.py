import pandas as pd
import sys
import os

# Añadir el directorio padre al path para imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora importar los módulos
from src.preprocesamiento import cargar_datos, manejar_nulos, estandarizar_texto, limpieza_especifica
from src.visualizacion import (
    graficar_distribucion_edad,
    graficar_intereses_populares,
    graficar_genero_distribucion
)

# Rutas de los archivos
USUARIOS_PATH = 'data/usuarios.csv' 
INTERACCIONES_PATH = 'data/interacciones.json'

def realizar_analisis():
    """
    Función principal que realiza el análisis completo de datos de la app tipo Tinder.
    
    Returns:
        tuple: (df_combinado, df_usuarios, df_interacciones, resultados_analisis)
    """
    print("=" * 60)
    print("📊 ANÁLISIS DE DATOS - APP DE CITAS")
    print("=" * 60)
    
    # 1. CARGA Y PREPROCESAMIENTO
    print("\n🔄 1. Cargando y limpiando datos...")
    df_usuarios, df_interacciones = cargar_datos(USUARIOS_PATH, INTERACCIONES_PATH)
    
    # Aplicar funciones de limpieza
    df_usuarios = manejar_nulos(df_usuarios, 'biografia')
    df_usuarios = estandarizar_texto(df_usuarios, 'intereses')
    df_usuarios = estandarizar_texto(df_usuarios, 'nombre')
    
    print(f"   ✓ {len(df_usuarios)} usuarios cargados")
    print(f"   ✓ {len(df_interacciones)} interacciones cargadas")
    
    # 2. COMBINACIÓN DE DATOS
    print("\n🔗 2. Combinando datos...")
    df_combinado = pd.merge(df_usuarios, df_interacciones, on='id_usuario', how='inner')
    print(f"   ✓ {len(df_combinado)} registros combinados")
    
    # 3. ANÁLISIS ESTADÍSTICO
    print("\n📈 3. Realizando análisis estadísticos...")
    
    resultados = {}
    
    # Análisis 1: Estadísticas de edad
    resultados['edad_promedio'] = df_usuarios['edad'].mean()
    resultados['edad_mediana'] = df_usuarios['edad'].median()
    resultados['edad_min'] = df_usuarios['edad'].min()
    resultados['edad_max'] = df_usuarios['edad'].max()
    
    print(f"\n   👥 DEMOGRAFÍA:")
    print(f"      • Edad promedio: {resultados['edad_promedio']:.1f} años")
    print(f"      • Edad mediana: {resultados['edad_mediana']:.0f} años")
    print(f"      • Rango de edad: {resultados['edad_min']}-{resultados['edad_max']} años")
    
    # Análisis 2: Intereses más populares
    resultados['top_intereses'] = df_usuarios['intereses'].value_counts().head(5)
    
    print(f"\n   ❤️ TOP 5 INTERESES:")
    for interes, count in resultados['top_intereses'].items():
        print(f"      • {interes.capitalize()}: {count} usuarios")
    
    # Análisis 3: Tasa de matches
    total_interacciones = len(df_interacciones)
    total_matches = df_interacciones['match'].sum()
    resultados['tasa_match'] = (total_matches / total_interacciones) * 100
    
    print(f"\n   💘 MÉTRICAS DE MATCHES:")
    print(f"      • Total interacciones: {total_interacciones}")
    print(f"      • Matches exitosos: {total_matches}")
    print(f"      • Tasa de éxito: {resultados['tasa_match']:.1f}%")
    
    # Análisis 4: Distribución por ciudad
    resultados['usuarios_por_ciudad'] = df_usuarios['ciudad'].value_counts()
    
    print(f"\n   🏙️ DISTRIBUCIÓN GEOGRÁFICA:")
    for ciudad, count in resultados['usuarios_por_ciudad'].items():
        print(f"      • {ciudad}: {count} usuarios")
    
    # Análisis 5: Distribución por género
    resultados['distribucion_genero'] = df_usuarios['genero'].value_counts()
    
    print(f"\n   👫 DISTRIBUCIÓN POR GÉNERO:")
    for genero, count in resultados['distribucion_genero'].items():
        genero_texto = 'Masculino' if genero == 'M' else 'Femenino'
        print(f"      • {genero_texto}: {count} usuarios")
    
    # Análisis 6: Tipos de interacción
    resultados['tipos_interaccion'] = df_interacciones['tipo'].value_counts()
    
    print(f"\n   🎯 TIPOS DE INTERACCIÓN:")
    for tipo, count in resultados['tipos_interaccion'].items():
        print(f"      • {tipo.capitalize()}: {count}")
    
    # Análisis 7: Usuarios más activos
    usuarios_activos = df_interacciones['id_usuario'].value_counts().head(5)
    resultados['usuarios_activos'] = usuarios_activos
    
    print(f"\n   🔥 TOP 5 USUARIOS MÁS ACTIVOS:")
    for id_usuario, count in usuarios_activos.items():
        usuario = df_usuarios[df_usuarios['id_usuario'] == id_usuario]
        if not usuario.empty:
            nombre = usuario['nombre'].values[0]
            print(f"      • {nombre}: {count} interacciones")
        else:
            print(f"      • Usuario ID {id_usuario}: {count} interacciones (usuario no encontrado)")
    
    # Análisis 8: Matches por ciudad
    df_matches = df_combinado[df_combinado['match'] == True]
    resultados['matches_por_ciudad'] = df_matches['ciudad'].value_counts()
    
    print(f"\n   💑 MATCHES POR CIUDAD:")
    for ciudad, count in resultados['matches_por_ciudad'].items():
        print(f"      • {ciudad}: {count} matches")
    
    print("\n" + "=" * 60)
    print("✅ Análisis completado exitosamente")
    print("=" * 60)
    
    return df_combinado, df_usuarios, df_interacciones, resultados

def generar_tablas_html(df_usuarios, df_interacciones, resultados):
    """
    Genera tablas HTML para el reporte.
    
    Args:
        df_usuarios: DataFrame de usuarios
        df_interacciones: DataFrame de interacciones
        resultados: Diccionario con resultados del análisis
    
    Returns:
        dict: Diccionario con las tablas en formato HTML
    """
    tablas = {}
    
    # Tabla 1: Top usuarios por edad
    df_top_usuarios = df_usuarios[['nombre', 'edad', 'ciudad', 'intereses']].head(10)
    tablas['top_usuarios'] = df_top_usuarios.to_html(
        classes='table table-striped table-hover',
        index=False,
        border=0
    )
    
    # Tabla 2: Estadísticas por ciudad
    stats_ciudad = df_usuarios.groupby('ciudad').agg({
        'id_usuario': 'count',
        'edad': 'mean'
    }).round(1)
    stats_ciudad.columns = ['Número de Usuarios', 'Edad Promedio']
    tablas['stats_ciudad'] = stats_ciudad.to_html(
        classes='table table-striped table-hover',
        border=0
    )
    
    # Tabla 3: Top intereses
    df_intereses = pd.DataFrame({
        'Interés': resultados['top_intereses'].index,
        'Número de Usuarios': resultados['top_intereses'].values
    })
    tablas['top_intereses'] = df_intereses.to_html(
        classes='table table-striped table-hover',
        index=False,
        border=0
    )
    
    # Tabla 4: Resumen de matches
    df_matches_summary = pd.DataFrame({
        'Métrica': ['Total Interacciones', 'Matches Exitosos', 'Tasa de Éxito'],
        'Valor': [
            len(df_interacciones),
            df_interacciones['match'].sum(),
            f"{resultados['tasa_match']:.1f}%"
        ]
    })
    tablas['matches_summary'] = df_matches_summary.to_html(
        classes='table table-striped table-hover',
        index=False,
        border=0
    )
    
    return tablas

if __name__ == '__main__':
    df_combinado, df_usuarios, df_interacciones, resultados = realizar_analisis()