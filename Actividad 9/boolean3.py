from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Escenario de prueba 3: Validando de que las opciones del menú funcionen todas

# Inizialización de Chrome WebDriver
driver = webdriver.Chrome()

# Navegación a sitio web
driver.get("https://boolean.careers")

# Click en menu principal
driver.find_element(By.CSS_SELECTOR, ".animation-mobile-course").click()

# Espera para cargar la pagina
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".live-courses")))

# Click en menu
driver.find_element(By.CSS_SELECTOR, ".live-courses > .course-item-1:nth-child(2) .heading-4").click()

# Espera para cargar la pagina
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar-item:nth-child(2) > .heading-5")))

# Click en Menu Corsi
driver.find_element(By.CSS_SELECTOR, ".animation-mobile-course").click()

# Espera para cargar la pagina
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".live-courses")))

# Click en menu
driver.find_element(By.CSS_SELECTOR, ".live-courses > .course-item-1:nth-child(3) .heading-4").click()

# Espera para cargar la pagina
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.LINK_TEXT, "Recensioni")))

# Click nuevamente en Corsi
driver.find_element(By.CSS_SELECTOR, ".animation-mobile-course").click()

# Espera para cargar la pagina
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".live-courses")))

# Click en la otra seccion
driver.find_element(By.CSS_SELECTOR, ".course-item-1:nth-child(4) .heading-4").click()

# Espera para cargar la pagina
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.LINK_TEXT, "Career Service")))

# Click en Menu Chi siamo
driver.find_element(By.CSS_SELECTOR, ".navbar-item:nth-child(2) > .heading-5").click()

# Espera para cargar la pagina
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.LINK_TEXT, "Recensioni")))

# Click en Recensioni
driver.find_element(By.LINK_TEXT, "Recensioni").click()

# Espera para cargar la pagina
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.LINK_TEXT, "Career Service")))

# Click en otro menu
driver.find_element(By.LINK_TEXT, "Career Service").click()

# Espera para cargar la pagina
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.LINK_TEXT, "Perché Boolean")))

# Click en submenú Perché Boolean
driver.find_element(By.LINK_TEXT, "Perché Boolean").click()

# Espera para cargar la pagina
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.LINK_TEXT, "FAQ")))

# Click en FAQ
driver.find_element(By.LINK_TEXT, "FAQ").click()

# Espera para cargar la pagina
print("Se visualizaron todas las paginas correctamente")
time.sleep(4)  # Delay para visibilidad

# Cerrar navegador
driver.close()