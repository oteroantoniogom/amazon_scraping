import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Cargar el archivo CSV que contiene las palabras clave
csv_file = 'words_url.csv'
df = pd.read_csv(csv_file)

# Inicializar el controlador del navegador Chrome
driver = webdriver.Chrome()

# Recorrer las filas del DataFrame
for index, row in df.iterrows():
    # Obtener la palabra de la columna 'word' en la fila actual
    word = row['word']
    print(f"Procesando palabra clave: {word}")
    
    # Construir la URL de búsqueda en Amazon | Necesario cambiar tema
    search_url = f'https://www.amazon.es/s?k={word}+tema'
    
    # Abrir la página de búsqueda en Amazon
    driver.get(search_url)
    time.sleep(1)  # Esperar para asegurarse de que la página se cargue

    # Click en el enlace para obtener el enlace de afiliado
    link = driver.find_element('xpath', '//a[@href="javascript:void(0)"]')
    link.click()
    time.sleep(2)  # Esperar para que la página se cargue completamente después de hacer clic
    
    # Obtener el enlace de afiliado desde el elemento de textarea
    affiliate = driver.find_element(By.ID, 'amzn-ss-text-shortlink-textarea')
    affiliate_content = affiliate.get_attribute('value')
    print(f"Enlace de afiliado obtenido: {affiliate_content}")
    time.sleep(1)
    
    # Actualizar la columna 'url' en el DataFrame con el enlace de afiliado
    df.at[index, 'url'] = affiliate_content

# Cerrar el navegador Chrome
driver.quit()

# Guardar el DataFrame actualizado en un archivo CSV
output_csv = 'output.csv'
df.to_csv(output_csv, index=False)

print(f"Proceso completado. Resultados guardados en {output_csv}")