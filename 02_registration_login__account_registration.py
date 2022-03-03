
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.maximize_window()

#===========================================================================#
#                "Registration_login: регистрация аккаунта"
#===========================================================================#

#       1. Открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

#       2. Нажать на вкладку "My Account Menu"
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT, "My Account").click()

#       3. В разделе "Register", ввести email для регистрации
field_email_reg = driver.find_element(By.ID, "reg_email")
field_email_reg.send_keys("BullockJeims@ro.ru")

#       4. В разделе "Register", ввести пароль для регистрации
field_pass_reg = driver.find_element(By.ID, "reg_password")
field_pass_reg.send_keys("/!EvPrzCc;;>`2D%'_")

#       5. Нажать на кнопку "Register"
reg_btn = driver.find_element(By.CSS_SELECTOR, "[type='submit'].woocommerce-Button.button[name='register']")
reg_btn.click()

driver.quit()
