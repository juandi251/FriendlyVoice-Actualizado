# FriendlyVoice - Plataforma de Red Social de Audio

Plataforma social donde los usuarios pueden compartir mensajes de voz, conectarse con otros usuarios y administrar contenido.

## 📁 Estructura del Proyecto

```
Proyecto/
├── FriendlyVoice-App/     # Frontend (Next.js + TypeScript)
├── back_FriendlyVoice/    # Backend (Spring Boot + Java)
├── Documents/python/      # Análisis de Datos y Visualizaciones (Python)
└── README.md              # Este archivo
```

## 🚀 Tecnologías Principales

### Frontend
- **Next.js 14** - Framework React
- **TypeScript** - Tipado estático
- **Firebase SDK** - Autenticación y servicios
- **Tailwind CSS** - Estilos

### Backend
- **Spring Boot 3.4.8** - Framework Java
- **Firebase Admin SDK** - Gestión de Firestore
- **Maven** - Gestión de dependencias

### Análisis de Datos
- **Python 3.8+** - Lenguaje de análisis
- **Pandas** - Manipulación y análisis de datos
- **Matplotlib & Seaborn** - Visualizaciones y gráficos
- **HTML/CSS/JavaScript** - Reportes interactivos

## 📋 Requisitos Previos

1. **Node.js** (v18 o superior)
2. **Java 17**
3. **Maven**
4. **Python 3.8+** (para análisis de datos)
5. **Cuenta de Firebase** con proyecto configurado
6. **Git**

## ⚙️ Configuración

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd Proyecto
```

### 2. Configurar Frontend
```bash
cd FriendlyVoice-App
npm install
```

### 3. Configurar Backend
```bash
cd back_FriendlyVoice
mvn clean install
```

### 4. Configurar Firebase
- Obtén las credenciales de Firebase Admin SDK
- Coloca el archivo `firebase-service-account.local.json` en:
  - `back_FriendlyVoice/src/main/resources/`

⚠️ **IMPORTANTE**: Los archivos de credenciales NO deben subirse a GitHub (ya están en `.gitignore`)

### 5. Configurar Análisis de Datos
```bash
cd Documents/python
pip install -r requirements.txt
```

## 🏃 Ejecución

### Frontend
```bash
cd FriendlyVoice-App
npm run dev
```
Abre http://localhost:3000

### Backend
```bash
cd back_FriendlyVoice
mvn spring-boot:run
```
El backend estará en http://localhost:8080

### Análisis de Datos y Reportes
```bash
cd Documents/python
python src/generar_reporte.py
```
Esto generará un archivo `reporte.html` con visualizaciones y análisis de datos.

## 🔐 Funcionalidades Principales

- ✅ Autenticación de usuarios (Firebase Auth)
- ✅ Sistema de bloqueo de cuentas (3 intentos fallidos)
- ✅ Gestión de usuarios y reportes (Panel Admin)
- ✅ Publicación y reproducción de mensajes de voz
- ✅ Sistema de seguimiento (seguidores/seguidos)
- ✅ Perfiles de usuario personalizables
- ✅ Análisis de datos y visualizaciones estadísticas
- ✅ Generación de reportes HTML interactivos

## 📊 Análisis Visual y Resultados

El proyecto incluye un módulo de análisis de datos ubicado en `Documents/python/` que permite:

- **Preprocesamiento de datos**: Limpieza y estandarización de datos de usuarios e interacciones
- **Análisis estadístico**: Métricas demográficas, de comportamiento y de éxito
- **Visualizaciones**: 7 gráficos diferentes con Matplotlib y Seaborn:
  - 📊 Distribución de edades
  - ❤️ Top intereses más populares
  - 🏙️ Matches por ciudad
  - 📈 Tasa de éxito de matches
  - 🎯 Tipos de interacciones
  - 👫 Distribución por género
  - 📅 Actividad temporal
- **Reporte HTML**: Documento interactivo con tablas y gráficos usando DataTables.js

### Hallazgos Principales

- **Edad promedio**: 27.3 años (rango: 19-36 años)
- **Distribución por género**: Equilibrada (51% M / 49% F)
- **Tasa de éxito**: 62.0% de matches exitosos
- **Interés más popular**: Música (22.2% de usuarios)
- **Ciudad líder**: Medellín (40% de usuarios)

Para más detalles sobre el análisis, consulta `Documents/python/README.md`.

## 📝 Notas

- El proyecto requiere credenciales de Firebase para funcionar
- Consulta los README individuales de cada subproyecto para más detalles

## 👤 Autor

Juan Franco

---

**Desarrollado con ❤️ para conectar voces**

