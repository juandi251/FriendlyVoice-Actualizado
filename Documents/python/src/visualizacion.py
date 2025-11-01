import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import BytesIO
import base64

# Configuración de estilo
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 10

def figura_a_base64(fig):
    """Convierte una figura de matplotlib a base64 para incrustar en HTML."""
    buffer = BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight', dpi=100)
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read()).decode()
    plt.close(fig)
    return img_base64

def graficar_distribucion_edad(df_usuarios):
    """
    Genera un histograma de la distribución de edades de los usuarios.
    
    Args:
        df_usuarios: DataFrame con los datos de usuarios (debe tener columna 'edad')
    
    Returns:
        str: Imagen en formato base64
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Crear histograma
    ax.hist(df_usuarios['edad'], bins=15, color='#FF6B6B', edgecolor='black', alpha=0.7)
    
    # Añadir línea de media
    media_edad = df_usuarios['edad'].mean()
    ax.axvline(media_edad, color='#4ECDC4', linestyle='--', linewidth=2, 
               label=f'Media: {media_edad:.1f} años')
    
    ax.set_xlabel('Edad', fontsize=12, fontweight='bold')
    ax.set_ylabel('Número de Usuarios', fontsize=12, fontweight='bold')
    ax.set_title('Distribución de Edades en la App', fontsize=14, fontweight='bold', pad=20)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    return figura_a_base64(fig)

def graficar_intereses_populares(df_usuarios, top_n=10):
    """
    Genera un gráfico de barras con los intereses más populares.
    
    Args:
        df_usuarios: DataFrame con los datos de usuarios (debe tener columna 'intereses')
        top_n: Número de intereses top a mostrar
    
    Returns:
        str: Imagen en formato base64
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Contar frecuencia de intereses
    conteo_intereses = df_usuarios['intereses'].value_counts().head(top_n)
    
    # Crear gráfico de barras horizontal
    colores = sns.color_palette("viridis", len(conteo_intereses))
    conteo_intereses.plot(kind='barh', ax=ax, color=colores, edgecolor='black')
    
    ax.set_xlabel('Número de Usuarios', fontsize=12, fontweight='bold')
    ax.set_ylabel('Intereses', fontsize=12, fontweight='bold')
    ax.set_title(f'Top {top_n} Intereses Más Populares', fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, axis='x', alpha=0.3)
    
    # Añadir valores en las barras
    for i, v in enumerate(conteo_intereses):
        ax.text(v + 0.1, i, str(v), va='center', fontweight='bold')
    
    plt.tight_layout()
    return figura_a_base64(fig)

def graficar_publicaciones_por_ciudad(df_combinado):
    """
    Genera un gráfico de barras mostrando el número de publicaciones activas por ciudad.
    
    Args:
        df_combinado: DataFrame combinado con datos de usuarios e interacciones
    
    Returns:
        str: Imagen en formato base64
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Filtrar solo publicaciones activas
    df_publicadas = df_combinado[df_combinado['estado'].str.upper() == 'PUBLICADO']
    
    # Contar publicaciones por ciudad
    publicaciones_ciudad = df_publicadas['ciudad'].value_counts()
    
    # Crear gráfico de barras
    colores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    publicaciones_ciudad.plot(kind='bar', ax=ax, color=colores, edgecolor='black')
    
    ax.set_xlabel('Ciudad', fontsize=12, fontweight='bold')
    ax.set_ylabel('Número de Publicaciones', fontsize=12, fontweight='bold')
    ax.set_title('Publicaciones Activas por Ciudad', fontsize=14, fontweight='bold', pad=20)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True, axis='y', alpha=0.3)
    
    # Añadir valores encima de las barras
    for i, v in enumerate(publicaciones_ciudad):
        ax.text(i, v + 0.5, str(v), ha='center', fontweight='bold')
    
    plt.tight_layout()
    return figura_a_base64(fig)

def graficar_tasa_publicacion(df_interacciones):
    """
    Genera un gráfico de pie mostrando la tasa de publicaciones activas.
    
    Args:
        df_interacciones: DataFrame con las interacciones
    
    Returns:
        str: Imagen en formato base64
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Contar publicaciones activas vs borradores
    conteo_estados = df_interacciones['estado'].str.upper().value_counts()
    
    # Crear gráfico de pie
    colores = ['#4ECDC4', '#FFB6C1']
    explode = (0.05, 0)
    
    labels = [f'{estado.capitalize()} 📝' for estado in conteo_estados.index]
    ax.pie(conteo_estados, labels=labels, autopct='%1.1f%%',
           colors=colores, explode=explode, shadow=True, startangle=90,
           textprops={'fontsize': 12, 'fontweight': 'bold'})
    
    ax.set_title('Estado de Publicaciones', fontsize=14, fontweight='bold', pad=20)
    
    return figura_a_base64(fig)

def graficar_duracion_promedio(df_interacciones):
    """
    Genera un gráfico de barras mostrando la duración promedio de publicaciones por estado.
    
    Args:
        df_interacciones: DataFrame con las interacciones
    
    Returns:
        str: Imagen en formato base64
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Calcular duración promedio por estado
    duracion_por_estado = df_interacciones.groupby(df_interacciones['estado'].str.upper())['duracion_segundos'].mean()
    
    # Crear gráfico de barras
    colores = ['#4ECDC4', '#FFD700']
    duracion_por_estado.plot(kind='bar', ax=ax, color=colores, edgecolor='black')
    
    ax.set_xlabel('Estado de Publicación', fontsize=12, fontweight='bold')
    ax.set_ylabel('Duración Promedio (segundos)', fontsize=12, fontweight='bold')
    ax.set_title('Duración Promedio por Estado', fontsize=14, fontweight='bold', pad=20)
    ax.tick_params(axis='x', rotation=0)
    ax.grid(True, axis='y', alpha=0.3)
    
    # Añadir valores encima de las barras
    for i, v in enumerate(duracion_por_estado):
        ax.text(i, v + 1, f'{v:.1f}', ha='center', fontweight='bold')
    
    plt.tight_layout()
    return figura_a_base64(fig)

def graficar_genero_distribucion(df_usuarios):
    """
    Genera un gráfico de pie mostrando la distribución por género.
    
    Args:
        df_usuarios: DataFrame con los datos de usuarios
    
    Returns:
        str: Imagen en formato base64
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Contar distribución de género
    conteo_genero = df_usuarios['genero'].value_counts()
    
    # Crear gráfico de pie
    colores = ['#4ECDC4', '#FF6B6B']
    explode = (0.05, 0.05)
    
    labels = ['Masculino' if g == 'M' else 'Femenino' for g in conteo_genero.index]
    
    ax.pie(conteo_genero, labels=labels, autopct='%1.1f%%',
           colors=colores, explode=explode, shadow=True, startangle=90,
           textprops={'fontsize': 12, 'fontweight': 'bold'})
    
    ax.set_title('Distribución por Género', fontsize=14, fontweight='bold', pad=20)
    
    return figura_a_base64(fig)

def graficar_actividad_usuario(df_interacciones):
    """
    Genera un gráfico de barras mostrando la distribución de publicaciones por usuario.
    
    Args:
        df_interacciones: DataFrame con las interacciones
    
    Returns:
        str: Imagen en formato base64
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Contar publicaciones por usuario (top 10)
    publicaciones_por_usuario = df_interacciones['id_usuario'].value_counts().head(10)
    
    # Crear gráfico de barras
    ax.bar(range(len(publicaciones_por_usuario)), publicaciones_por_usuario.values, 
           color='#4ECDC4', edgecolor='black', alpha=0.7)
    
    ax.set_xlabel('Usuario ID', fontsize=12, fontweight='bold')
    ax.set_ylabel('Número de Publicaciones', fontsize=12, fontweight='bold')
    ax.set_title('Top 10 Usuarios Más Activos', fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(range(len(publicaciones_por_usuario)))
    ax.set_xticklabels(publicaciones_por_usuario.index, rotation=45, ha='right')
    ax.grid(True, axis='y', alpha=0.3)
    
    # Añadir valores encima de las barras
    for i, v in enumerate(publicaciones_por_usuario.values):
        ax.text(i, v + 0.1, str(v), ha='center', fontweight='bold')
    
    plt.tight_layout()
    return figura_a_base64(fig)

def graficar_tasa_match(df_interacciones):
    """
    Genera un gráfico de pie mostrando la tasa de matches.
    
    Args:
        df_interacciones: DataFrame con las interacciones
    
    Returns:
        str: Imagen en formato base64
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Contar matches vs no matches
    total_matches = df_interacciones['match'].sum()
    total_no_matches = len(df_interacciones) - total_matches
    
    # Crear gráfico de pie
    colores = ['#4ECDC4', '#FFB6C1']
    explode = (0.05, 0)
    
    labels = [f'Matches 💘', f'Sin Match 💔']
    valores = [total_matches, total_no_matches]
    
    ax.pie(valores, labels=labels, autopct='%1.1f%%',
           colors=colores, explode=explode, shadow=True, startangle=90,
           textprops={'fontsize': 12, 'fontweight': 'bold'})
    
    ax.set_title('Tasa de Éxito de Matches', fontsize=14, fontweight='bold', pad=20)
    
    return figura_a_base64(fig)

def graficar_matches_por_ciudad(df_combinado):
    """
    Genera un gráfico de barras mostrando el número de matches por ciudad.
    
    Args:
        df_combinado: DataFrame combinado con datos de usuarios e interacciones
    
    Returns:
        str: Imagen en formato base64
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Filtrar solo matches exitosos
    df_matches = df_combinado[df_combinado['match'] == True]
    
    # Contar matches por ciudad
    matches_ciudad = df_matches['ciudad'].value_counts()
    
    # Crear gráfico de barras
    colores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    matches_ciudad.plot(kind='bar', ax=ax, color=colores, edgecolor='black')
    
    ax.set_xlabel('Ciudad', fontsize=12, fontweight='bold')
    ax.set_ylabel('Número de Matches', fontsize=12, fontweight='bold')
    ax.set_title('Matches Exitosos por Ciudad', fontsize=14, fontweight='bold', pad=20)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True, axis='y', alpha=0.3)
    
    # Añadir valores encima de las barras
    for i, v in enumerate(matches_ciudad):
        ax.text(i, v + 0.5, str(v), ha='center', fontweight='bold')
    
    plt.tight_layout()
    return figura_a_base64(fig)

def graficar_tipos_interaccion(df_interacciones):
    """
    Genera un gráfico de barras mostrando los tipos de interacción.
    
    Args:
        df_interacciones: DataFrame con las interacciones
    
    Returns:
        str: Imagen en formato base64
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Contar tipos de interacción
    tipos = df_interacciones['tipo'].value_counts()
    
    # Crear gráfico de barras
    colores = sns.color_palette("Set2", len(tipos))
    tipos.plot(kind='bar', ax=ax, color=colores, edgecolor='black')
    
    ax.set_xlabel('Tipo de Interacción', fontsize=12, fontweight='bold')
    ax.set_ylabel('Cantidad', fontsize=12, fontweight='bold')
    ax.set_title('Distribución de Tipos de Interacción', fontsize=14, fontweight='bold', pad=20)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True, axis='y', alpha=0.3)
    
    # Añadir valores encima de las barras
    for i, v in enumerate(tipos):
        ax.text(i, v + 0.5, str(v), ha='center', fontweight='bold')
    
    plt.tight_layout()
    return figura_a_base64(fig)

def graficar_actividad_temporal(df_interacciones):
    """
    Genera un gráfico de línea mostrando la actividad temporal.
    
    Args:
        df_interacciones: DataFrame con las interacciones (debe tener columna 'fecha')
    
    Returns:
        str: Imagen en formato base64
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Convertir fecha a datetime si no lo es
    if 'fecha' in df_interacciones.columns:
        df_temp = df_interacciones.copy()
        df_temp['fecha'] = pd.to_datetime(df_temp['fecha'])
        df_temp['fecha_solo'] = df_temp['fecha'].dt.date
        
        # Contar interacciones por fecha
        actividad_diaria = df_temp.groupby('fecha_solo').size()
        
        # Crear gráfico de línea
        ax.plot(actividad_diaria.index, actividad_diaria.values, 
                marker='o', linewidth=2, markersize=6, color='#4ECDC4')
        
        ax.set_xlabel('Fecha', fontsize=12, fontweight='bold')
        ax.set_ylabel('Número de Interacciones', fontsize=12, fontweight='bold')
        ax.set_title('Actividad de Usuarios en el Tiempo', fontsize=14, fontweight='bold', pad=20)
        ax.tick_params(axis='x', rotation=45)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
    else:
        # Si no hay columna fecha, crear un gráfico simple
        ax.text(0.5, 0.5, 'Datos de fecha no disponibles', 
                ha='center', va='center', fontsize=14)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
    
    return figura_a_base64(fig)