## Agradecimientos a:
Este proyecto está hecho basado en la API desarrollada por https://github.com/apiad , este es un script para facilitar la búsqueda de animes y acceso a sus links respectivos.

## Descripción del Script

Este script permite buscar series de anime utilizando la API de AnimeFLV. Los usuarios pueden seleccionar una serie y un episodio específico, y el script proporcionará enlaces para ver el episodio seleccionado.

## Dependencias

El script requiere las siguientes dependencias:

- **venv**: Para crear un entorno virtual.
- **animeflv**: Biblioteca para interactuar con la API de AnimeFLV.
- **cloudscraper**: Para manejar la protección de Cloudflare.
- **lxml**: Para el procesamiento de XML y HTML.
- **beautifulsoup4**: Para el scrapeo de la web.

## Instalación

### Para Sistemas Linux

1. **Instalar Python y pip** (si no están instalados):
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **Crear un entorno virtual**:
   ```bash
   python3 -m venv myenv
   ```

3. **Activar el entorno virtual**:
   ```bash
   source myenv/bin/activate
   ```

4. **Instalar las dependencias**:
   ```bash
   pip install animeflv cloudscraper lxml
   ```

5. **Ejecutar el script**:
   ```bash
   python anime.py
   ```

### Para Sistemas Windows

1. **Instalar Python y pip** (si no están instalados):
   - Descarga el instalador de Python desde [python.org](https://www.python.org/downloads/) y asegúrate de marcar la opción "Add Python to PATH".

2. **Crear un entorno virtual**:
   ```cmd
   python -m venv myenv
   ```

3. **Activar el entorno virtual**:
   ```cmd
   myenv\Scripts\activate
   ```

4. **Instalar las dependencias**:
   ```cmd
   pip install animeflv cloudscraper lxml beautifulsoup4
   ```

5. **Ejecutar el script**:
   ```cmd
   python anime.py
   ```

## Uso

1. Al ejecutar el script, se te pedirá que escribas el nombre de una serie de anime.
2. Selecciona la serie de la lista que se mostrará.
3. Luego, selecciona un episodio de la serie.
4. Finalmente, se mostrarán los enlaces para ver el episodio seleccionado.

## Notas

- Asegúrate de tener una conexión a Internet activa para que el script funcione correctamente.
- Si encuentras algún error, verifica que todas las dependencias estén correctamente instaladas y que el entorno virtual esté activado.
