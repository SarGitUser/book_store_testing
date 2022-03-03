
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
driver.maximize_window()

#===========================================================================#
#                      "Shop: покупка товара"
#===========================================================================#

#       1. Открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

#       2. Нажать на вкладку "Shop" и проскролить на 300 пикселей вниз
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Shop").click()
driver.execute_script("window.scrollBy(0, 300);")

#       3. Добавить в корзину книгу "HTML5 WebApp Development"
driver.find_element(By.CSS_SELECTOR, "[data-product_id='182']").click()

#       4. Перейдти в корзину
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#wpmenucartli").click()

#       5. Нажать "PROCEED TO CHECKOUT" (перед нажатием, добавить явное ожидание)
wait = WebDriverWait(driver,10)
el_proceed = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button.alt.wc-forward")))
el_proceed.click()

#       6. Заполнить все обязательные поля
field_first = wait.until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
field_first.send_keys("Irina")
field_first.click()

field_last = wait.until(EC.element_to_be_clickable((By.ID, "billing_last_name")))
field_last.send_keys("Smirnova")
field_last.click()

field_email = wait.until(EC.element_to_be_clickable((By.ID, "billing_email")))
field_email.send_keys("IrinaSm@ro.ru")
field_email.click()

field_phone = wait.until(EC.element_to_be_clickable((By.ID, "billing_phone")))
field_phone.send_keys("1234567809")
field_phone.click()

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='s2id_billing_country']/a/span[2]/b"))).click()
field_search1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".select2-search>input")))
field_search1.send_keys("Russia")
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "select2-match"))).click()

field_address_1 = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "[placeholder='Street address']")))
field_address_1.send_keys("str. Sennay, home №5")
field_address_1.click()

field_city = wait.until(EC.element_to_be_clickable((By.ID, "billing_city")))
field_city.send_keys("g.Samara")
field_city.click()

field_state = wait.until(EC.element_to_be_clickable((By.ID, "billing_state")))
field_state.send_keys("My State")
field_state.click()

field_postcode = wait.until(EC.element_to_be_clickable((By.ID, "billing_postcode")))
field_postcode.send_keys("2145")
field_postcode.click()

#       7. Проскролить на 600 пикселей вниз и выбрать способ оплаты "Check Payments"
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#payment>ul>li:nth-child(2)>input").click()
time.sleep(5)

#       8. Нажать PLACE ORDER
driver.find_element(By.ID, "place_order").click()
time.sleep(5)

#       9. Проверить, что отображается надпись "Thank you. Your order has been received."
el_thank = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce>p"), "Thank you. Your order has been received."))
print(str(el_thank))   #=> True

#       10. Проверить, что в Payment Method отображается текст "Check Payments"
el_check = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method>strong"), "Check Payments"))
print(str(el_check))   #=> True

driver.quit()
