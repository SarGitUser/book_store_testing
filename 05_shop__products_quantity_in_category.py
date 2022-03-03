
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.maximize_window()

#===========================================================================#
#                "Shop: количество товаров в категории"
#===========================================================================#

#       1. Открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

#       2. Залогиниться
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT, "My Account").click()
field_email_log = driver.find_element(By.ID, "username")
field_email_log.send_keys("BullockJeims@ro.ru")
field_pass_log = driver.find_element(By.ID, "password")
field_pass_log.send_keys("/!EvPrzCc;;>`2D%'_")
driver.find_element(By.NAME, "login").click()

#       3. Нажать на вкладку "Shop"
driver.find_element(By.LINK_TEXT, "Shop").click()

#       4. Открыть категорию "HTML"
driver.find_element(By.LINK_TEXT, "HTML").click()

#       5. Добавить тест, что отображается три товара
items_count = driver.find_elements(By.CSS_SELECTOR, "ul.products.masonry-done>li")
print("Количество товаров на странице: " + str(len(items_count)))

driver.quit()


