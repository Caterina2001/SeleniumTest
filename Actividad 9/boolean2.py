from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Definir las variables para el nombre, apellido y correo electrónico

correo = "rosariocaterina@gmail.com"
contraseña = "cate"

#Escenario de prueba 2: Inicio de sesión fallido
driver = webdriver.Chrome()
driver.get("https://hiringplatform.boolean.careers/login")

driver.set_window_size(1051, 846)

#Ingreso de datos definidos en las variables
driver.find_element(By.ID, "email").send_keys(correo)
driver.find_element(By.ID, "password").send_keys(contraseña)
print("Se han ingresado las credenciales")
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, ".button-submit").click()
print("Se ha dado click al botón de iniciar sesión")

#Se espera un mensaje de acceso invalido ya que las credenciales propuestas son incorrectas

time.sleep(10)

#Cerrar navegador
driver.close

