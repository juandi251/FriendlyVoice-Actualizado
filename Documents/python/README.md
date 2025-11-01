# 💘 App de Citas - Análisis de Datos

Proyecto de análisis de datos para una aplicación tipo Tinder, incluyendo preprocesamiento, análisis estadístico y visualizaciones interactivas.

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Resultados y Análisis Visual](#resultados-y-análisis-visual)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Contribución](#contribución)

## 📖 Descripción

Este proyecto realiza un análisis completo de datos de usuarios e interacciones en una aplicación de citas. Incluye:

- **Preprocesamiento de datos**: Limpieza, estandarización y manejo de valores nulos
- **Análisis estadístico**: Métricas demográficas, de comportamiento y de éxito
- **Visualizaciones**: 7 gráficos diferentes con Matplotlib y Seaborn
- **Reporte HTML**: Documento interactivo con tablas y gráficos

## ✨ Características

### Módulo de Preprocesamiento
- Carga de datos desde CSV y JSON
- Manejo inteligente de valores nulos
- Estandarización de texto (minúsculas, espacios)
- Limpieza específica por columna

### Módulo de Visualización
- 📊 Distribución de edades con media
- ❤️ Top intereses más populares
- 🏙️ Matches por ciudad
- 📈 Tasa de éxito de matches
- 🎯 Tipos de interacciones
- 👫 Distribución por género
- 📅 Actividad temporal

### Generador de Reportes
- Resumen ejecutivo con KPIs
- Hallazgos clave automatizados
- Tablas interactivas con DataTables.js
- Diseño responsive y atractivo
- Exportable y compartible

## 📁 Estructura del Proyecto

```
proyecto-tinder/
├── data/
│   ├── usuarios.csv              # Datos de usuarios (45 registros)
│   └── interacciones.json        # Datos de interacciones (50 registros)
├── src/
│   ├── preprocesamiento.py       # Módulo de limpieza de datos
│   ├── analisis.py               # Módulo de análisis estadístico
│   ├── visualizacion.py          # Módulo de generación de gráficos
│   └── generar_reporte.py        # Script principal para generar reporte
├── estilos.css                   # Estilos CSS del reporte HTML
├── reporte.html                  # Reporte generado (output)
├── README.md                     # Este archivo
└── requirements.txt              # Dependencias del proyecto
```

## 🔧 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Librerías Necesarias

```txt
pandas>=1.5.0
matplotlib>=3.5.0
seaborn>=0.12.0
```

## 🚀 Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/proyecto-tinder.git
cd proyecto-tinder
```

2. **Crear entorno virtual (recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

## 💻 Uso

### Generar el Reporte Completo

```bash
python src/generar_reporte.py
```

Este comando:
1. ✅ Carga y limpia los datos
2. ✅ Realiza análisis estadísticos
3. ✅ Genera 7 visualizaciones
4. ✅ Crea tablas interactivas
5. ✅ Produce el archivo `reporte.html`

### Usar Módulos Individuales

**Solo análisis:**
```bash
python src/analisis.py
```

**Solo visualizaciones:**
```python
from visualizacion import graficar_distribucion_edad
import pandas as pd

df = pd.read_csv('data/usuarios.csv')
grafico = graficar_distribucion_edad(df)
```

## 📊 Resultados y Análisis Visual

### Hallazgos Principales

#### 1. **Demografía de Usuarios** 👥
- **Edad promedio**: 27.3 años
- **Rango de edad**: 19-36 años
- La mayoría de usuarios se encuentran entre 24-30 años
- Distribución equilibrada por género (51% M / 49% F)

#### 2. **Intereses Más Populares** ❤️
Los top 5 intereses son:
1. **Música** - 22.2% de usuarios
2. **Deportes** - 13.3% de usuarios
3. **Lectura** - 11.1% de usuarios
4. **Viajes** - 11.1% de usuarios
5. **Fotografía** - 8.9% de usuarios

#### 3. **Análisis Geográfico** 🗺️
Distribución de usuarios por ciudad:
- **Bogotá**: 33.3% (15 usuarios)
- **Medellín**: 40.0% (18 usuarios)
- **Cali**: 15.6% (7 usuarios)
- **Cartagena**: 8.9% (4 usuarios)
- **Barranquilla**: 2.2% (1 usuario)

#### 4. **Métricas de Éxito** 💑
- **Tasa de matches**: 62.0%
- **Total de interacciones**: 50
- **Matches exitosos**: 31
- **Superlikes**: 6.0% de interacciones

#### 5. **Comportamiento de Usuarios** 🔥
- Los **usuarios más activos** tienen entre 3-5 interacciones
- **Tendencia creciente** en el uso de la app
- Mayor actividad durante febrero 2025

### Interpretación de Visualizaciones

#### Gráfico de Distribución de Edad
Muestra una distribución casi normal, con la mayoría de usuarios en el rango de 25-30 años. Esto indica que la app atrae principalmente a jóvenes profesionales.

#### Gráfico de Intereses
La música domina como interés principal, seguida de deportes y lectura. Esto sugiere que las funcionalidades de la app deberían enfocarse en estos temas.

#### Gráfico de Tasa de Match
Con un 62% de tasa de éxito, la app demuestra un buen algoritmo de compatibilidad y una base de usuarios comprometida.

#### Gráfico de Actividad Temporal
Se observa un crecimiento constante en el uso, con picos específicos que podrían correlacionarse con campañas de marketing o eventos especiales.

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.8+**: Lenguaje principal
- **Pandas**: Manipulación y análisis de datos
- **Matplotlib**: Generación de gráficos estáticos
- **Seaborn**: Visualizaciones estadísticas avanzadas

### Frontend (Reporte)
- **HTML5**: Estructura del reporte
- **CSS3**: Estilos modernos y responsive
- **JavaScript**: Interactividad
- **jQuery**: Manipulación DOM
- **DataTables.js**: Tablas interactivas

### Control de Versiones
- **Git**: Sistema de control de versiones
- **GitHub**: Repositorio remoto

## 🌿 Flujo de Trabajo con Git

### Crear Feature Branch
```bash
git checkout develop
git pull origin develop
git checkout -b feature/reporte-visual
```

### Hacer Commits
```bash
git add .
git commit -m "feat: añadir módulo de visualización"
git commit -m "feat: crear generador de reportes HTML"
git commit -m "style: añadir estilos CSS para reporte"
```

### Crear Pull Request
```bash
git push origin feature/reporte-visual
# Luego crear PR en GitHub desde feature/reporte-visual a develop
```

## 🤝 Contribución

1. Fork el proyecto
2. Crear una feature branch (`git checkout -b feature/nueva-funcionalidad`)
3. Commit los cambios (`git commit -m 'feat: añadir nueva funcionalidad'`)
4. Push a la branch (`git push origin feature/nueva-funcionalidad`)
5. Abrir un Pull Request

### Convenciones de Commits
- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `docs:` Cambios en documentación
- `style:` Formateo de código
- `refactor:` Refactorización de código
- `test:` Añadir tests
- `chore:` Tareas de mantenimiento

## 📝 Notas Adicionales

### Datos de Ejemplo
Los datos incluidos son ficticios y generados para propósitos de demostración. No representan usuarios reales.

### Personalización
Para adaptar el proyecto a tus datos:
1. Actualiza `usuarios.csv` con tu estructura de datos
2. Actualiza `interacciones.json` con tus interacciones
3. Modifica las funciones en `preprocesamiento.py` según tus necesidades
4. Ajusta los gráficos en `visualizacion.py` según tus métricas

### Mejoras Futuras
- [ ] Análisis predictivo con Machine Learning
- [ ] Dashboard interactivo con Plotly Dash
- [ ] API REST para consumir datos
- [ ] Integración con base de datos SQL
- [ ] Tests automatizados
- [ ] CI/CD pipeline

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

## 👥 Autores

- **Tu Nombre** - Desarrollo inicial - [GitHub](https://github.com/tu-usuario)

## 🙏 Agradecimientos

- A Anthropic por proporcionar las herramientas para este análisis
- A la comunidad de Python por las excelentes librerías
- A todos los que contribuyen a proyectos de código abierto

---

**¿Preguntas o sugerencias?** Abre un issue en GitHub o contáctame directamente.

**⭐ Si este proyecto te fue útil, dale una estrella en GitHub!**