# TTS App

## Estructura básica

Hay tres cuestiones clave para la estructura de la aplicación:

1. **Aplicación en flask y función tts:**

* app.py
* make_audio.py

2. **Dependencias del modelo TTS:**

* config_vocoder.json
* config.json
* scale_stats_vocoder.npy
* scale_stats.npy

3. Archivo .venv; requirements.txt

Para instalar las dependencias, basta con correr
 `pip install -r requirements.txt`

Cabe destacar que hay **dos archivos no incluidos** en el repositorio **debido a su tamaño**. Estos dos archivos pueden encontrarse en este [google drive](app.pyhttps://drive.google.com/drive/folders/1w-4ZosaiQhPCtuuDySHqpIL2LyZooZKN). Es una descarga tardada, por lo que se recomienda su instalación directa en el directorio del proyecto.

## Uso del programa

En el ambiente escogido con las dependencias instaladas, correr **app.py**. Se debería visualizar en consola la carga del modelo y la aplicación en modo debug.

## Issues en desarrollo

* Integración de app con gcp y mongo
* Añadir app en inglés
* Organización de archivos de audio.
* Identificadores de ID de cliente.
* Contenedor optimizado de la aplicación.