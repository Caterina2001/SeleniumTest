from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Definir las variables para el nombre, apellido y correo electrónico
nombre = "Caterina"
apellido = "Giannecchini"
correo = "rosariocaterina@gmail.com"

# Escenario de prueba 1: Envío de formulario

# Inizialización de Web Driver
driver = webdriver.Chrome()

# Pagina web
driver.get("https://boolean.careers")

driver.maximize_window()
driver.find_element(By.ID, "btn-apply").click()
driver.execute_script("window.scrollTo(0,248)")

# Seleccionar el boón de ISCRIVITI para completar el formulario
driver.find_element(By.CSS_SELECTOR, ".select-input").click()
driver.find_element(By.CSS_SELECTOR, "ul > .paragraph-2:nth-child(2)").click()

# Rellenar el formulario con las variables
driver.find_element(By.CSS_SELECTOR, ".input-container:nth-child(2) > .bg-lightPixel-5").click()
driver.find_element(By.CSS_SELECTOR, ".input-container:nth-child(2) > .bg-lightPixel-5").send_keys(nombre)
driver.find_element(By.CSS_SELECTOR, ".input-container:nth-child(3) > .bg-lightPixel-5").send_keys(apellido)
driver.find_element(By.CSS_SELECTOR, ".input-container:nth-child(4) > .bg-lightPixel-5").send_keys(correo)

# Validar el formulario
driver.find_element(By.NAME, "term_condition").click()
print ("Has dado click en confirmar las condiciones del formulario")

#Pausa para verificar los datos en pantalla
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".button-submit-form").click()

#Se espera el mensaje de que se ha enviado correctamente el formulario
print("Se ha enviado el formulario con éxito")

driver.execute_script("window.scrollTo(0,0)")

#Pausa de 10 seg para visualziacion del mensaje
time.sleep(10)

#Cerrar navegador web
driver.close()

   
