
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.maximize_window()

#===========================================================================#
#                      "Home: добавление комментария"
#===========================================================================#

#       1. Открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

#       2. Проскролить страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")

#       3. Нажать на название книги "Selenium Ruby" или на кнопку "READ MORE"
driver.find_element(By.CSS_SELECTOR, "a>img[title='Selenium Ruby']").click()

#       4. Нажать на вкладку "REVIEWS"
driver.find_element(By.CSS_SELECTOR, ".woocommerce-tabs.wc-tabs-wrapper>ul>li:nth-child(2)").click()

#       5. Поставить 5 звёзд
driver.find_element(By.CSS_SELECTOR, ".stars>span>a:nth-child(5)").click()

#       6. Заполнить поле "Review" сообщением: "Nice book!"
field_review = driver.find_element(By.CSS_SELECTOR, "#comment[name='comment']")
field_review.send_keys("Nice book!")

#       7. Заполнить поле "Name"
field_name = driver.find_element(By.CSS_SELECTOR, "form>p:nth-child(4)>input")
field_name.send_keys("Nika")

#       8. Заполнить "Email"
field_email = driver.find_element(By.CSS_SELECTOR, "form>p:nth-child(5)>input")
field_email.send_keys("NikaBon@ro.ru")

#       9. Нажать на кнопку "SUBMIT"
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".form-submit>input#submit").click()

driver.quit()
