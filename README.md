# FriendlyVoice - Plataforma de Red Social de Audio

Plataforma social donde los usuarios pueden compartir mensajes de voz, conectarse con otros usuarios y administrar contenido.

## 📁 Estructura del Proyecto

```
Proyecto/
├── FriendlyVoice-App/     # Frontend (Next.js + TypeScript)
├── back_FriendlyVoice/    # Backend (Spring Boot + Java)
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

## 📋 Requisitos Previos

1. **Node.js** (v18 o superior)
2. **Java 17**
3. **Maven**
4. **Cuenta de Firebase** con proyecto configurado
5. **Git**

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

## 🔐 Funcionalidades Principales

- ✅ Autenticación de usuarios (Firebase Auth)
- ✅ Sistema de bloqueo de cuentas (3 intentos fallidos)
- ✅ Gestión de usuarios y reportes (Panel Admin)
- ✅ Publicación y reproducción de mensajes de voz
- ✅ Sistema de seguimiento (seguidores/seguidos)
- ✅ Perfiles de usuario personalizables

## 📝 Notas

- El proyecto requiere credenciales de Firebase para funcionar
- Consulta los README individuales de cada subproyecto para más detalles

## 👤 Autor

Juan Franco

---

**Desarrollado con ❤️ para conectar voces**

