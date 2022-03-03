
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.maximize_window()

#===========================================================================#
#                      "Shop: проверка цены в корзине"
#===========================================================================#

#       1. Открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

#       2. Нажать на вкладку "Shop"
driver.find_element(By.LINK_TEXT, "Shop").click()

#       3. Добавить в корзину книгу "HTML5 WebApp Development"
driver.find_element(By.CSS_SELECTOR, "[data-product_id='182']").click()

#       4. Тест, что возле корзины количество товаров = "1 Item", а стоимость = "₹180.00"
#          (использовать для проверки assert)
time.sleep(5)
my_item = driver.find_element(By.CSS_SELECTOR, "#wpmenucartli > a > span.cartcontents")
print(my_item.text)
assert my_item.text == "1 Item"
my_price = driver.find_element(By.CSS_SELECTOR, "#main-nav > li:nth-child(6) > a > .amount")
print(my_price.text)
assert my_price.text == "₹180.00"

#       5. Перейти в корзину
driver.find_element(By.LINK_TEXT, "View Basket").click()

#       6. Используя явное ожидание, проверить, что в Subtotal отобразилась стоимость
wait = WebDriverWait(driver,10)
el_subtotal = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.cart-subtotal>td>span"), "180.00"))
# print(str(el_subtotal))   => True

#       7. Используя явное ожидание, проверить, что в Total отобразилась стоимость
el_total = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.order-total>td>strong>span"), "189.00"))
# print(str(el_total))   => True

driver.quit()
