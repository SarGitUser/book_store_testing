
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.maximize_window()

#===========================================================================#
#                      "Shop: работа в корзине"
#===========================================================================#

#       1. Открыть http://practice.automationtesting.in/ (логиниться не нужно)
driver.get("http://practice.automationtesting.in/")

#       2. Нажать на вкладку "Shop"
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Shop").click()

#       3. Добавить в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
#          (перед добавлением первой книги, проскролить вниз на 300 пикселей)
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element(By.CSS_SELECTOR, "[data-product_id='182']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "[data-product_id='180']").click()

#       4. Перейти в корзину
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#wpmenucartli").click()

#       5. Удалить первую книгу (перед удалением добавить sleep)
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "[data-product_id='182']").click()

#       6. Нажать на Undo (отмена удаления)
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Undo?").click()

#       7. В Quantity увеличить количество товара до 3 шт для "JS Data Structures and Algorithm“
#          (предварительно очистить поле с помощью локатор_поля.clear())
el_quantity = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1)>td:nth-child(5)>div>input")
el_quantity_val = el_quantity.get_attribute("value")
el_quantity.clear()
time.sleep(1)
el_quantity.send_keys("3")

#       8. Нажать на кнопку "UPDATE BASKET"
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".button[name='update_cart']").click()

#       9. Добавить тест, что value элемента quantity для "JS Data Structures and Algorithm"
#          равно 3 (использовать assert)
assert (str(el_quantity.get_attribute("value"))) == "3"

#       10. Нажать на кнопку "APPLY COUPON" (перед нажатием добавить sleep)
time.sleep(3)
apply_btn = driver.find_element(By.CSS_SELECTOR, ".button[name='apply_coupon']").click()

#       11. Добавить тест, что возникло сообщение: "Please enter a coupon code."
wait = WebDriverWait(driver,10)
el_please = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "ul.woocommerce-error>li"), "Please enter a coupon code."))

time.sleep(3)
driver.quit()
