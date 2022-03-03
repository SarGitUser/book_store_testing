
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
wait = WebDriverWait(driver,10)

#===========================================================================#
#                      "Shop: отображение, скидка товара"
#===========================================================================#

#       1. Открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

#       2. Залогиниться
driver.find_element(By.LINK_TEXT, "My Account").click()
field_email_log = driver.find_element(By.ID, "username")
field_email_log.send_keys("BullockJeims@ro.ru")
field_pass_log = driver.find_element(By.ID, "password")
field_pass_log.send_keys("/!EvPrzCc;;>`2D%'_")
driver.find_element(By.NAME, "login").click()

#       3. Нажать на вкладку "Shop"
driver.find_element(By.LINK_TEXT, "Shop").click()

#       4. Открыть книгу "Android Quick Start Guide"
driver.find_element(By.CSS_SELECTOR, ".post-169 h3").click()

#       5. Добавить тест, что содержимое старой цены = "₹600.00" (использовать assert)
old_price = driver.find_element(By.CSS_SELECTOR, ".price > del > span")
old_price_text = old_price.text
assert old_price_text == "₹600.00"

#       6. Добавить тест, что содержимое новой цены = "₹450.00" (использовать assert)
new_price = driver.find_element(By.CSS_SELECTOR, ".price > ins > span")
new_price_text = new_price.text
assert new_price_text == "₹450.00"

#       7. Добавить явное ожидание и нажать на обложку книги
#          (подобрать такой селектор и тайминги, чтобы открылось окно
#          предпросмотра картинки (не вся картинка на всю страницу)
book_cover = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
book_cover.click()

#       8. Добавить явное ожидание и закрыть предпросмотр, нажав на крестик (кнопка вверху справа)
book_cover_close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
book_cover_close.click()

driver.quit()
