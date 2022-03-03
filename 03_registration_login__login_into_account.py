
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.maximize_window()

#===========================================================================#
#                "Registration_login: логин в систему"
#===========================================================================#

#       1. Открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

#       2. Нажать на вкладку "My Account Menu"
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT, "My Account").click()

#       3. В разделе "Login", ввести email для логина
field_email_log = driver.find_element(By.ID, "username")
field_email_log.send_keys("BullockJeims@ro.ru")

#       4. В разделе "Login", ввести пароль для логина
field_pass_log = driver.find_element(By.ID, "password")
field_pass_log.send_keys("/!EvPrzCc;;>`2D%'_")

#       5. Нажать на кнопку "Login"
driver.find_element(By.NAME, "login").click()

#       6. Добавить проверку, что на странице есть элемент "Logout"
wait = WebDriverWait(driver,10)
element_logout = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce>nav>ul>li:nth-child(6)>a"), "Logout"))

print(element_logout)
driver.quit()
