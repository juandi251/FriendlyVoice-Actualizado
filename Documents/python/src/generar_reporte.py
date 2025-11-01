"""
Script para generar el reporte HTML con visualizaciones y tablas.
"""

from analisis import realizar_analisis, generar_tablas_html
from visualizacion import (
    graficar_distribucion_edad,
    graficar_intereses_populares,
    graficar_genero_distribucion,
    graficar_tasa_match,
    graficar_matches_por_ciudad,
    graficar_tipos_interaccion,
    graficar_actividad_temporal
)
from datetime import datetime

def generar_html_reporte(df_usuarios, df_interacciones, df_combinado, resultados, tablas):
    """
    Genera el HTML completo del reporte.
    
    Args:
        df_usuarios: DataFrame de usuarios
        df_interacciones: DataFrame de interacciones
        df_combinado: DataFrame combinado
        resultados: Diccionario con resultados del análisis
        tablas: Diccionario con tablas HTML
    
    Returns:
        str: Contenido HTML completo
    """
    
    # Generar todas las visualizaciones
    print("\n📊 Generando visualizaciones...")
    
    graficos = {}
    graficos['edad'] = graficar_distribucion_edad(df_usuarios)
    print("   ✓ Gráfico de distribución de edad")
    
    graficos['intereses'] = graficar_intereses_populares(df_usuarios)
    print("   ✓ Gráfico de intereses populares")
    
    graficos['genero'] = graficar_genero_distribucion(df_usuarios)
    print("   ✓ Gráfico de distribución por género")
    
    graficos['tasa_match'] = graficar_tasa_match(df_interacciones)
    print("   ✓ Gráfico de tasa de match")
    
    graficos['matches_ciudad'] = graficar_matches_por_ciudad(df_combinado)
    print("   ✓ Gráfico de matches por ciudad")
    
    graficos['tipos'] = graficar_tipos_interaccion(df_interacciones)
    print("   ✓ Gráfico de tipos de interacción")
    
    graficos['actividad'] = graficar_actividad_temporal(df_interacciones)
    print("   ✓ Gráfico de actividad temporal")
    
    # Fecha actual
    fecha_reporte = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    # Construir HTML
    html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte de Análisis - App de Citas</title>
    <link rel="stylesheet" href="estilos.css">
    
    <!-- DataTables CSS -->
    <link rel="stylesheet" href="https://cdn.datatables.net/1.13.7/css/jquery.dataTables.min.css">
    
    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    
    <!-- DataTables JS -->
    <script src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header class="header">
            <h1>💘 Reporte de Análisis - App de Citas</h1>
            <p class="subtitle">Análisis Completo de Usuarios e Interacciones</p>
            <p class="date">Generado el: {fecha_reporte}</p>
        </header>

        <!-- Resumen Ejecutivo -->
        <section class="section">
            <h2 class="section-title">📋 Resumen Ejecutivo</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number">{len(df_usuarios)}</div>
                    <div class="stat-label">Usuarios Registrados</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{len(df_interacciones)}</div>
                    <div class="stat-label">Interacciones Totales</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{df_interacciones['match'].sum()}</div>
                    <div class="stat-label">Matches Exitosos</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{resultados['tasa_match']:.1f}%</div>
                    <div class="stat-label">Tasa de Éxito</div>
                </div>
            </div>
        </section>

        <!-- Hallazgos Clave -->
        <section class="section">
            <h2 class="section-title">🔍 Hallazgos Clave</h2>
            <div class="findings">
                <div class="finding-item">
                    <span class="finding-icon">👥</span>
                    <div class="finding-content">
                        <h3>Demografía</h3>
                        <p>La edad promedio de los usuarios es de <strong>{resultados['edad_promedio']:.1f} años</strong>, 
                        con un rango entre {resultados['edad_min']} y {resultados['edad_max']} años.</p>
                    </div>
                </div>
                <div class="finding-item">
                    <span class="finding-icon">❤️</span>
                    <div class="finding-content">
                        <h3>Interés Principal</h3>
                        <p>El interés más popular es <strong>{list(resultados['top_intereses'].index)[0].capitalize()}</strong> 
                        con {list(resultados['top_intereses'].values)[0]} usuarios.</p>
                    </div>
                </div>
                <div class="finding-item">
                    <span class="finding-icon">🏙️</span>
                    <div class="finding-content">
                        <h3>Ciudad Líder</h3>
                        <p><strong>{resultados['usuarios_por_ciudad'].index[0]}</strong> tiene la mayor cantidad de usuarios 
                        con {resultados['usuarios_por_ciudad'].values[0]} registros.</p>
                    </div>
                </div>
                <div class="finding-item">
                    <span class="finding-icon">💑</span>
                    <div class="finding-content">
                        <h3>Éxito de Matches</h3>
                        <p>La tasa de éxito de matches es del <strong>{resultados['tasa_match']:.1f}%</strong>, 
                        indicando una buena compatibilidad en la plataforma.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Visualizaciones -->
        <section class="section">
            <h2 class="section-title">📊 Análisis Visual</h2>
            
            <div class="chart-container">
                <h3 class="chart-title">Distribución de Edades</h3>
                <img src="data:image/png;base64,{graficos['edad']}" alt="Distribución de Edad" class="chart">
                <p class="chart-description">
                    Este gráfico muestra cómo se distribuyen las edades de los usuarios en la plataforma. 
                    La línea punteada indica la edad promedio de {resultados['edad_promedio']:.1f} años.
                </p>
            </div>

            <div class="chart-container">
                <h3 class="chart-title">Intereses Más Populares</h3>
                <img src="data:image/png;base64,{graficos['intereses']}" alt="Intereses Populares" class="chart">
                <p class="chart-description">
                    Los intereses más comunes entre los usuarios, destacando las preferencias principales 
                    de la comunidad de la app.
                </p>
            </div>

            <div class="chart-row">
                <div class="chart-container-half">
                    <h3 class="chart-title">Distribución por Género</h3>
                    <img src="data:image/png;base64,{graficos['genero']}" alt="Distribución Género" class="chart">
                    <p class="chart-description">
                        Balance de género en la plataforma.
                    </p>
                </div>

                <div class="chart-container-half">
                    <h3 class="chart-title">Tasa de Éxito de Matches</h3>
                    <img src="data:image/png;base64,{graficos['tasa_match']}" alt="Tasa de Match" class="chart">
                    <p class="chart-description">
                        Proporción de interacciones que resultan en match.
                    </p>
                </div>
            </div>

            <div class="chart-container">
                <h3 class="chart-title">Matches por Ciudad</h3>
                <img src="data:image/png;base64,{graficos['matches_ciudad']}" alt="Matches por Ciudad" class="chart">
                <p class="chart-description">
                    Ciudades con mayor actividad de matches, mostrando dónde la app tiene más éxito.
                </p>
            </div>

            <div class="chart-container">
                <h3 class="chart-title">Tipos de Interacción</h3>
                <img src="data:image/png;base64,{graficos['tipos']}" alt="Tipos de Interacción" class="chart">
                <p class="chart-description">
                    Distribución de los tipos de interacciones (likes, superlikes, dislikes) en la plataforma.
                </p>
            </div>

            <div class="chart-container">
                <h3 class="chart-title">Actividad en el Tiempo</h3>
                <img src="data:image/png;base64,{graficos['actividad']}" alt="Actividad Temporal" class="chart">
                <p class="chart-description">
                    Evolución de la actividad de usuarios a lo largo del tiempo, mostrando tendencias y picos de uso.
                </p>
            </div>
        </section>

        <!-- Tablas de Datos -->
        <section class="section">
            <h2 class="section-title">📈 Datos Detallados</h2>
            
            <div class="table-container">
                <h3 class="table-title">Resumen de Matches</h3>
                {tablas['matches_summary']}
            </div>

            <div class="table-container">
                <h3 class="table-title">Top Intereses</h3>
                {tablas['top_intereses']}
            </div>

            <div class="table-container">
                <h3 class="table-title">Estadísticas por Ciudad</h3>
                {tablas['stats_ciudad']}
            </div>

            <div class="table-container">
                <h3 class="table-title">Muestra de Usuarios</h3>
                {tablas['top_usuarios']}
            </div>
        </section>

        <!-- Footer -->
        <footer class="footer">
            <p>Reporte generado automáticamente por el sistema de análisis</p>
            <p>© 2025 App de Citas - Análisis de Datos</p>
        </footer>
    </div>

    <!-- Script para DataTables -->
    <script>
        $(document).ready(function() {{
            $('.table').DataTable({{
                "language": {{
                    "url": "//cdn.datatables.net/plug-ins/1.13.7/i18n/es-ES.json"
                }},
                "pageLength": 10,
                "order": []
            }});
        }});
    </script>
</body>
</html>
"""
    
    return html

def main():
    """Función principal que ejecuta todo el proceso."""
    print("\n" + "=" * 60)
    print("🚀 INICIANDO GENERACIÓN DE REPORTE")
    print("=" * 60)
    
    # 1. Realizar análisis
    df_combinado, df_usuarios, df_interacciones, resultados = realizar_analisis()
    
    # 2. Generar tablas HTML
    print("\n📋 Generando tablas HTML...")
    tablas = generar_tablas_html(df_usuarios, df_interacciones, resultados)
    print("   ✓ Tablas generadas")
    
    # 3. Generar HTML completo
    html_contenido = generar_html_reporte(df_usuarios, df_interacciones, df_combinado, resultados, tablas)
    
    # 4. Guardar archivo
    print("\n💾 Guardando reporte...")
    with open('reporte.html', 'w', encoding='utf-8') as f:
        f.write(html_contenido)
    
    print("   ✓ Reporte guardado como 'reporte.html'")
    
    print("\n" + "=" * 60)
    print("✅ REPORTE GENERADO EXITOSAMENTE")
    print("=" * 60)
    print("\n📄 Abre 'reporte.html' en tu navegador para ver el reporte completo.\n")

if __name__ == '__main__':
    main()