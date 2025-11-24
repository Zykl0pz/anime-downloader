# 🎬 AnimeFLV Downloader

Una herramienta avanzada en Python para buscar y descargar anime desde AnimeFLV.net con interfaz intuitiva y múltiples opciones de descarga.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Características Principales

### 🚀 **Funcionalidades Avanzadas**
- **🔍 Búsqueda inteligente** de animes con resultados organizados
- **📥 Descarga por intervalos** - Descarga rangos completos de episodios
- **🎯 Descarga individual** - Episodios específicos con un clic
- **🌐 Múltiples servidores** - Visualización de todos los servidores disponibles
- **📊 Progreso en tiempo real** - Barra de progreso para descargas largas

### 🎨 **Interfaz Mejorada**
- **Menú interactivo** con navegación intuitiva
- **Pantallas limpias** y bien organizadas
- **Emojis y formato** para mejor experiencia de usuario
- **Validación de entradas** robusta

### ⚡ **Tecnología**
- **Módulo animeflv** - Conexión directa con AnimeFLV.net
- **Descargas concurrentes** - Manejo eficiente de múltiples episodios
- **Manejo de errores** - Recuperación elegante de fallos

## 📋 Requisitos del Sistema

### Dependencias Principales
```bash
Python 3.6 o superior
animeflv-api
tqdm
requests
bs4
```
## 📋 Dependencias específicas para el script:

### **Esenciales:**
- **`animeflv-downloader`** - La API específica que usa tu script (del repo https://github.com/apiad/animeflv-downloader)
- **`tqdm`** - Para las barras de progreso en las descargas
- **`requests`** - Para las peticiones HTTP
- **`beautifulsoup4`** - Para parsear HTML

### **Para funcionalidades avanzadas:**
- **`selenium`** - Necesario para algunos servidores de video
- **`pathlib2`** - Para manejo de rutas (compatibilidad con Python 2/3)

## 🔧 Instalación:

```bash
# Instalar todas las dependencias
pip install -r requirements.txt

# Instalación manual
pip install animeflv-downloader tqdm requests beautifulsoup4 selenium pathlib2
```

**Versiones compatibles:**
   - Python 3.6 o superior
   - Las versiones especificadas son las mínimas recomendadas

## 🚀 Instalación rápida:

```bash
# Clona el repositorio de la API si no está en PyPI
git clone https://github.com/apiad/animeflv-downloader.git
cd animeflv-downloader
pip install -r requirements.txt
python setup.py install
```

## 🎮 Uso

### Flujo Básico
1. **Iniciar la aplicación**
   ```bash
   python anime.py
   ```

2. **Buscar anime**
   - Selecciona opción 1 del menú principal
   - Ingresa el nombre del anime

3. **Seleccionar episodios**
   - **Opción Individual**: Ver enlaces o descargar un episodio específico
   - **Opción Intervalo**: Descargar un rango completo de episodios

### Ejemplo de Uso
```
🎬 DESCARGADOR DE ANIME - ANIMEFLV
==================================================
1. Buscar y descargar anime
2. Salir
==================================================

Selecciona una opción: 1

🔍 BUSQUEDA DE ANIME
------------------------------
Escribir nombre del anime: Attack on Titan

📺 RESULTADOS DE BUSQUEDA
------------------------------
1. Shingeki no Kyojin
2. Shingeki no Kyojin: Chronicle
3. Attack on Titan: Junior High
4. 🔙 Volver al menú principal

Selecciona una opción: 1

🎬 Shingeki no Kyojin
--------------------------------------------------
📖 Descripción: La humanidad vive en ciudades...
📊 Total de episodios: 75
--------------------------------------------------
📋 Episodios (primeros 5 y últimos 5):
   1. Episodio 1
   2. Episodio 2
   3. Episodio 3
   4. Episodio 4
   5. Episodio 5
   ...
   71. Episodio 71
   72. Episodio 72
   73. Episodio 73
   74. Episodio 74
   75. Episodio 75

76. 📥 Descargar intervalo de episodios
77. 🔗 Ver enlaces de un episodio
78. 🔙 Volver a búsqueda
79. 🏠 Menú principal

Selecciona una opción: 76
```

## 📥 Descarga por Intervalos

### Características Exclusivas
- **Rango flexible**: Especifica episodio inicial y final
- **Validación automática**: Solo descarga episodios existentes
- **Progreso visual**: Barra de progreso en tiempo real
- **Manejo de errores**: Continúa descarga si un episodio falla

### Ejemplo de Descarga por Intervalo
```
📥 DESCARGAR INTERVALO DE EPISODIOS
--------------------------------------------------
🎬 Anime: Shingeki no Kyojin
📊 Episodios disponibles: 75
--------------------------------------------------
📈 Rango disponible: Episodio 1 a 75

Episodio inicial: 10
Episodio final: 15

📋 Episodios a descargar (6):
   - Episodio 10
   - Episodio 11
   - Episodio 12
   - Episodio 13
   - Episodio 14
   - Episodio 15

¿Descargar 6 episodios? (s/n): s
Directorio de descarga (dejar vacío para actual): ./attack_on_titan

📥 Iniciando descarga de 6 episodios...
Descargando: 100%|██████████| 6/6 [15:30<00:00, 155.00s/ep]
```

## 🗂️ Estructura del Proyecto

```
animeflv-downloader/
│
├── anime.py              # Script principal
├── README.md            # Este archivo
└── requirements.txt     # Dependencias del proyecto
```

## 🔧 Configuración Avanzada

### Variables de Entorno (Opcional)
```bash
# Directorio por defecto para descargas
export ANIME_DOWNLOAD_DIR="/ruta/descargas/anime"

# Servidor preferido (si está disponible)
export PREFERRED_SERVER="gocdn"
```

### Personalización
Puedes modificar las siguientes variables en el código:
- **Tiempo de espera** entre descargas
- **Servidores preferidos**
- **Formato de archivo** de salida
- **Límite de episodios** mostrados

## 🐛 Solución de Problemas

### Problemas Comunes

1. **Error de conexión**
   ```bash
   # Verificar conexión a AnimeFLV
   ping animeflv.net
   ```

2. **Dependencias faltantes**
   ```bash
   # Reinstalar todas las dependencias
   pip install -r requirements.txt
   ```

3. **Episodios no encontrados**
   - Verificar que el anime existe en AnimeFLV
   - Comprobar la ortografía del nombre

### Logs y Debug
El script proporciona mensajes detallados de error. Para más información:
```python
# Habilitar modo debug (modificar anime.py)
DEBUG = True
```

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## ⚠️ Aviso Legal

Este software está diseñado para uso educativo y personal. El usuario es responsable de verificar los derechos de autor y términos de uso del contenido descargado. Los desarrolladores no se hacen responsables del uso indebido de esta herramienta.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📞 Soporte

Si encuentras algún problema o tienes sugerencias:
- Abre un **issue** en GitHub
- Consulta la **documentación**
- Revisa los **problemas conocidos**

---

**¡Disfruta de tu anime!** 🎉
