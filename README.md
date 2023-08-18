# 🛒 Amazon Affiliate URL Scraper 📈

Este script en Python te permite realizar web scraping en el sitio web de Amazon para obtener enlaces de afiliados correspondientes a palabras clave específicas. El script carga una lista de palabras clave desde un archivo CSV, realiza búsquedas en Amazon para cada palabra clave y obtiene los enlaces de afiliados generados por Amazon.

**¡Importante!** 🚨 Este script es proporcionado con fines educativos y debe ser utilizado con responsabilidad. El web scraping puede estar sujeto a los términos de servicio de los sitios web y las políticas de uso justo. Por favor, consulta y respeta las políticas de los sitios web que deseas raspar.

## Requisitos 🛠️

- Python 3.x
- Biblioteca `pandas`
- Biblioteca `selenium`
- Controlador de navegador Chrome (Chromedriver)

## Instalación 🚀

1. Instala las bibliotecas requeridas:

```bash
pip install pandas selenium
```

2. Descarga el controlador de navegador Chrome (Chromedriver) adecuado para tu versión de Chrome y sistema operativo. Asegúrate de agregar el directorio del controlador a la variable de entorno `PATH`.

## Uso 📝

1. Crea un archivo CSV llamado `file.csv` con una columna llamada "word" que contenga las palabras clave a buscar en Amazon.

2. Ejecuta el script:

```bash
python amazon_scraper.py
```

3. El script recorrerá cada palabra clave en el archivo CSV, realizará búsquedas en Amazon y obtendrá los enlaces de afiliados correspondientes. Los enlaces actualizados se guardarán en un archivo CSV llamado `output.csv`.

**¡Importante!** Asegúrate de revisar y ajustar la lógica del script según tus necesidades. El tiempo de espera entre las operaciones puede variar según la velocidad de carga de la página y la interacción con elementos.

## Notas 📝

- Este script está destinado a fines educativos y puede requerir ajustes según los cambios en la estructura del sitio web de Amazon.
- El scraping debe realizarse de acuerdo con los términos de servicio y las políticas de uso justo del sitio web.
- ¡Utiliza el script con responsabilidad y ética! 👍
