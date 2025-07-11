import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Создаем настройки браузера
options = webdriver.ChromeOptions()

# Предотвращаем закрытие браузера после выполнения скрипта
options.add_experimental_option("detach", True)

# Запускаем Chrome с автоматически установленным драйвером и заданными опциями
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Базовые данные
base_url = "http://www.saucedemo.com/"
valid_username = "performance_glitch_user"
valid_password = "secret_sauce"

# Переход на страницу авторизации  и разворачивание окна на весь экран
driver.get(base_url)
driver.maximize_window()

# Ввод логина
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(valid_username)
print("Input login")

# Ввод пароля
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(valid_password)
print("Input password")

# Клик по кнопке "Login"
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='login-button']").click()
print("Click login button")

# Клик по кнопке скрытого меню
time.sleep(5)
driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
print("Click menu button")

# Logout
time.sleep(5)
driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()
print("Click logout button")

# Выход из браузера
time.sleep(1)
driver.quit()
print("Browser is closed")