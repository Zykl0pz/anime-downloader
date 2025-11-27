# Descargador de Anime - AnimeFLV

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/Licencia-MIT-green.svg)

Una herramienta de línea de comandos en Python para buscar y extraer enlaces de descarga de anime desde AnimeFLV.

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Prerequisitos](#prerequisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribución](#contribución)
- [Licencia](#licencia)
- [Aviso Legal](#aviso-legal)

## 🎯 Descripción

Este script proporciona una interfaz de línea de comandos interactiva para buscar anime en AnimeFLV y extraer enlaces de descarga de episodios. Permite tanto la extracción individual de enlaces por episodio como la extracción masiva de todos los episodios de una serie.

## ✨ Características

- 🔍 **Búsqueda inteligente**: Busca anime por nombre con resultados en tiempo real
- 📺 **Navegación interactiva**: Menús intuitivos para seleccionar anime y episodios
- 🔗 **Extracción de enlaces**: Obtiene enlaces de múltiples servidores con información de calidad
- 💾 **Exportación múltiple**: Guarda resultados en formato JSON o TXT
- 📊 **Progreso visual**: Barra de progreso con tqdm para extracciones largas
- ⚡ **Manejo de errores**: Gestión robusta de errores y reintentos automáticos
- 🎨 **Interfaz amigable**: Pantallas limpias y mensajes informativos

## 📋 Prerequisitos

- Python 3.6 o superior
- Conexión a Internet
- Módulos Python listados en requirements.txt

## 🚀 Instalación

### 1. Clonar o descargar el script
```bash
# Si tienes el repositorio
git clone <url-del-repositorio>

# O simplemente descarga el archivo anime.py
```

### 2. Instalar dependencias
```bash
pip install animeflv tqdm
```

### 3. Verificar instalación
```bash
python anime.py
```

## 📖 Uso

### Ejecución básica
```bash
python anime.py
```

### Flujo de trabajo típico

1. **Iniciar la aplicación**:
   ```bash
   python anime.py
   ```

2. **Menú principal**:
   ```
   ==================================================
            DESCARGADOR DE ANIME - ANIMEFLV
   ==================================================
   1. Buscar y descargar anime
   2. Extraer todos los enlaces de un anime
   3. Salir
   ==================================================
   ```

### Opción 1: Búsqueda y descarga individual

1. Selecciona la opción `1` del menú principal
2. Ingresa el nombre del anime a buscar
3. Selecciona el anime de la lista de resultados
4. Elige el episodio deseado
5. El sistema mostrará todos los enlaces disponibles

**Ejemplo de salida**:
```
📊 Se encontraron 3 enlaces:
1. Servidor: Mega
   URL: https://mega.nz/...
   Calidad: 1080p

2. Servidor: MediaFire
   URL: https://www.mediafire.com/...
   Calidad: 720p
```

### Opción 2: Extracción masiva de enlaces

1. Selecciona la opción `2` del menú principal
2. Ingresa el nombre del anime
3. Selecciona el formato de exportación:
   - **JSON**: Estructurado, ideal para uso programático
   - **TXT**: Formato legible para humanos

**Ejemplo de archivo JSON generado**:
```json
{
  "anime": "Attack on Titan",
  "anime_id": "shingeki-no-kyojin",
  "fecha_extraccion": "2024-01-15T14:30:45",
  "estadisticas": {
    "total_episodios": 25,
    "episodios_exitosos": 24,
    "episodios_con_error": 1
  },
  "episodios": {
    "1": {
      "episodio": "1",
      "enlaces": [
        {
          "servidor": "Mega",
          "url": "https://...",
          "calidad": "1080p"
        }
      ]
    }
  }
}
```

## 🗂️ Estructura del Proyecto

```
anime-downloader/
│
├── anime.py                 # Script principal
├── README.md               # Este archivo
└── ejemplos/               # Ejemplos de uso (opcional)
    ├── enlaces_ejemplo.json
    └── enlaces_ejemplo.txt
```

### Funciones principales

- `main()`: Función principal que maneja el flujo de la aplicación
- `buscar_anime(api)`: Búsqueda y selección individual de episodios
- `extraer_todos_enlaces(api)`: Extracción masiva de enlaces
- `procesar_extraccion_enlaces(api, anime)`: Procesa la extracción con barra de progreso
- `guardar_resultados()`: Guarda los resultados en los formatos soportados

## 🔧 Configuración

El script no requiere configuración adicional. Sin embargo, puedes modificar:

- **Tiempo de espera entre peticiones**: Modifica `time.sleep(0.5)` en `procesar_extraccion_enlaces()`
- **Formato de fechas**: Modifica el formato en `datetime.now().strftime()`

## 🤝 Contribución

Las contribuciones son bienvenidas. Para contribuir:

1. Haz un fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Mejoras potenciales

- [ ] Descarga automática de episodios
- [ ] Soporte para múltiples idiomas
- [ ] Interfaz gráfica (GUI)
- [ ] Sistema de colas de descarga
- [ ] Integración con gestores de descarga

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## ⚠️ Aviso Legal

Este script está diseñado únicamente para fines educativos y de aprendizaje. El usuario es responsable de cumplir con los términos de servicio de AnimeFLV y las leyes de copyright aplicables en su país. Los desarrolladores no se hacen responsables del uso indebido de esta herramienta.

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'animeflv'"
**Solución**: Instala la dependencia faltante:
```bash
pip install animeflv
```

### Error: "No se encontraron resultados para tu búsqueda"
**Solución**:
- Verifica la conexión a Internet
- Revisa la ortografía del nombre del anime
- Intenta con nombres alternativos en inglés/japonés

### Error: "No se encontraron enlaces para este episodio"
**Solución**:
- El episodio puede no estar disponible
- Intenta con otro servidor
- Espera y reintenta más tarde

## 📞 Soporte

Si encuentras problemas o tienes preguntas:

1. Revisa la sección de solución de problemas
2. Verifica que todas las dependencias estén instaladas
3. Asegúrate de usar la versión más reciente del script

---

**¡Disfruta usando el Descargador de Anime!** 🎉