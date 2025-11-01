# 🌿 Guía de Git Flow para el Proyecto

## Estructura de Branches

```
main (producción)
  └── develop (desarrollo)
       └── feature/reporte-visual (tu feature branch)
```

## 📝 Paso a Paso: Crear y Fusionar Feature Branch

### 1. Asegurarte de estar en develop actualizado

```bash
# Cambiar a develop
git checkout develop

# Actualizar develop con los últimos cambios
git pull origin develop
```

### 2. Crear la Feature Branch

```bash
# Crear y cambiar a la nueva branch
git checkout -b feature/reporte-visual

# Verificar que estás en la branch correcta
git branch
# Debería mostrar: * feature/reporte-visual
```

### 3. Añadir los Archivos Nuevos

```bash
# Ver el estado actual
git status

# Añadir archivos específicos
git add src/visualizacion.py
git add src/generar_reporte.py
git add estilos.css
git add README.md
git add requirements.txt

# O añadir todo de una vez
git add .
```

### 4. Hacer Commits Descriptivos

```bash
# Commit del módulo de visualización
git commit -m "feat: añadir módulo de visualización con 7 funciones de gráficos"

# Commit del generador de reportes
git commit -m "feat: crear generador de reportes HTML con análisis completo"

# Commit de estilos
git commit -m "style: añadir estilos CSS modernos y responsive para reporte"

# Commit de documentación
git commit -m "docs: actualizar README con instrucciones y resultados de análisis"

# Commit de dependencias
git commit -m "chore: añadir requirements.txt con dependencias del proyecto"

# Commit de preprocesamiento actualizado
git commit -m "refactor: actualizar módulo de preprocesamiento para nuevos datos"

# Commit de datos actualizados
git commit -m "data: expandir datos a 45 usuarios con contexto de app de citas"
```

### 5. Verificar los Commits

```bash
# Ver el historial de commits
git log --oneline

# Ver los cambios en un commit específico
git show HEAD
```

### 6. Subir la Branch al Remoto

```bash
# Primera vez (crear branch remota)
git push -u origin feature/reporte-visual

# Pushes subsecuentes
git push origin feature/reporte-visual
```

### 7. Crear Pull Request en GitHub

1. Ve a tu repositorio en GitHub
2. Verás un mensaje: "Compare & pull request" - haz clic
3. Configura el PR:
   - **Base**: `develop`
   - **Compare**: `feature/reporte-visual`
4. Título del PR: `feat: Implementar sistema de reportes visuales`
5. Descripción del PR:

```markdown
## 📊 Descripción

Implementación completa del sistema de análisis visual para la app de citas.

## ✨ Cambios Principales

### Nuevos Archivos
- ✅ `src/visualizacion.py`: Módulo con 7 funciones de visualización
- ✅ `src/generar_reporte.py`: Generador de reportes HTML
- ✅ `estilos.css`: Estilos modernos y responsive
- ✅ `requirements.txt`: Dependencias del proyecto

### Archivos Actualizados
- ✅ `README.md`: Documentación completa con resultados
- ✅ `src/preprocesamiento.py`: Adaptado para nuevos datos
- ✅ `data/usuarios.csv`: Expandido a 45 usuarios
- ✅ `data/interacciones.json`: 50 interacciones reales

## 📈 Funcionalidades

### Visualizaciones
1. Distribución de edades
2. Intereses más populares
3. Matches por ciudad
4. Tasa de éxito de matches
5. Tipos de interacción
6. Distribución por género
7. Actividad temporal

### Reporte HTML
- Resumen ejecutivo con KPIs
- Hallazgos clave automatizados
- Tablas interactivas con DataTables.js
- Diseño responsive y moderno
- 7 gráficos integrados

## 🧪 Testing

- [x] Código ejecuta sin errores
- [x] Todas las visualizaciones se generan correctamente
- [x] Reporte HTML se crea exitosamente
- [x] Tablas interactivas funcionan
- [x] Diseño responsive verificado

## 📸 Screenshots

(Aquí puedes añadir capturas de pantalla del reporte)

## ⚡ Cómo Probar

```bash
# Instalar dependencias
pip install -r requirements.txt

# Generar reporte
python src/generar_reporte.py

# Abrir reporte.html en el navegador
```

## 📝 Checklist

- [x] Código sigue las convenciones del proyecto
- [x] Tests pasan exitosamente
- [x] Documentación actualizada
- [x] Sin conflictos con develop
- [x] Commits son descriptivos

## 🔗 Issues Relacionados

Cierra #1 (si hay issues relacionados)
```

6. Clic en "Create pull request"

### 8. Revisar y Aprobar el PR

Si eres el único desarrollador:
1. Revisa tu código
2. Verifica que no hay conflictos
3. Clic en "Merge pull request"
4. Selecciona "Squash and merge" o "Create a merge commit"
5. Confirma el merge

Si trabajas en equipo:
- Espera la revisión de otros
- Atiende los comentarios
- Haz los cambios necesarios

### 9. Limpiar Después del Merge

```bash
# Volver a develop
git checkout develop

# Actualizar develop con el merge
git pull origin develop

# Borrar la feature branch local (opcional)
git branch -d feature/reporte-visual

# Borrar la feature branch remota (opcional)
git push origin --delete feature/reporte-visual
```

## 🔄 Flujo Completo Resumido

```bash
# 1. Actualizar develop
git checkout develop
git pull origin develop

# 2. Crear feature branch
git checkout -b feature/reporte-visual

# 3. Hacer cambios y commits
git add .
git commit -m "feat: descripción del cambio"

# 4. Push a remoto
git push -u origin feature/reporte-visual

# 5. Crear PR en GitHub

# 6. Después del merge, limpiar
git checkout develop
git pull origin develop
git branch -d feature/reporte-visual
```

## 📋 Convenciones de Commits

### Tipos de Commit

- `feat:` - Nueva funcionalidad
- `fix:` - Corrección de bug
- `docs:` - Cambios en documentación
- `style:` - Formato, punto y coma, etc.
- `refactor:` - Refactorización de código
- `test:` - Añadir o corregir tests
- `chore:` - Tareas de mantenimiento
- `data:` - Cambios en datos

### Ejemplos

```bash
git commit -m "feat: añadir visualización de distribución de edad"
git commit -m "fix: corregir error en cálculo de tasa de match"
git commit -m "docs: actualizar README con instrucciones de instalación"
git commit -m "style: aplicar formato PEP8 a visualizacion.py"
git commit -m "refactor: optimizar función de generación de gráficos"
git commit -m "test: añadir tests unitarios para preprocesamiento"
git commit -m "chore: actualizar dependencias en requirements.txt"
```

## 🚨 Resolver Conflictos

Si hay conflictos al hacer merge:

```bash
# 1. Actualizar develop en tu feature branch
git checkout feature/reporte-visual
git merge develop

# 2. Resolver conflictos manualmente en los archivos
# Git marcará los conflictos con <<<<<<, ======, >>>>>>

# 3. Después de resolver
git add .
git commit -m "merge: resolver conflictos con develop"

# 4. Push
git push origin feature/reporte-visual
```

## 💡 Tips Útiles

### Ver diferencias antes de commit
```bash
git diff
```

### Ver cambios en staged
```bash
git diff --staged
```

### Deshacer cambios no guardados
```bash
git checkout -- nombre_archivo.py
```

### Deshacer último commit (mantener cambios)
```bash
git reset --soft HEAD~1
```

### Ver historial bonito
```bash
git log --graph --oneline --all
```

### Guardar cambios temporalmente
```bash
git stash
git stash pop  # Para recuperarlos
```

## 📚 Recursos

- [Git Flow Cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)

---

**¿Dudas sobre Git?** Consulta este documento o busca en la documentación oficial de Git.