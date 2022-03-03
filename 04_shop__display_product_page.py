
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.maximize_window()

#===========================================================================#
#                "Shop: отображение страницы товара"
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

#       4. Открыть книгу "HTML 5 Forms"
driver.find_element(By.XPATH, "//img[@title='Mastering HTML5 Forms']").click()

#       5. Добавить тест, что заголовок книги называется: "HTML5 Forms"
element_book = driver.find_element_by_xpath("//h1[contains(text(), 'HTML5 Forms')]")
element_book_text = element_book.text
print('Книга называется:', element_book_text)

driver.quit()
