
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
driver.maximize_window()

#===========================================================================#
#                      "Shop: сортировка товаров"
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

#       4. Добавить тест, что в селекторе выбран вариант сортировки по умолчанию (по value)
element_sort = driver.find_element(By.XPATH, '//option[@value= "menu_order"]')
val_sort = element_sort.get_attribute("value")
if val_sort == "menu_order":
    print("Сортировка по умолчанию")
else:
    print("Сортировка не по умолчанию")

#       5. Отсортировать товары по цене от большей к меньшей (использовать класс Select)
el_select = driver.find_element(By.CSS_SELECTOR, "select.orderby")
element_select = Select(el_select)
element_select.select_by_index(5)      # или _value("price-desc")

#       6. Снова объявить переменную с локатором основного селектора сортировки
el_select = driver.find_element(By.CSS_SELECTOR, "select.orderby")

#       7. Проверить по value, что в селекторе выбран вариант сортировки по цене от > к <
val_sort2 = el_select.get_attribute("value")
if val_sort2 == "price-desc":
    print("Сортировка по цене от большей к меньшей")
else:
    print("Сортировка не по цене от большей к меньшей")

driver.quit()
