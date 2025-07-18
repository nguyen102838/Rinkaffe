from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from autologin import autoLoginLocation
from crawlingorders import crawlingOders


driver = webdriver.Chrome()
driver.get("https://weblogin.grab.com/merchant/saved-accounts?service_id=MEXUSERS&redirect=https%3A%2F%2Fmerchant.grab.com%2Fportal")
time.sleep(5)

autoLoginLocation(driver)
time.sleep(10)

driver.get("https://merchant.grab.com/order/5-C3MKVTDGGKWXNA/history")
time.sleep(10)
closeBoard = driver.find_element(By.CLASS_NAME, 'dui-modal-close-x')
closeBoard.click()

time.sleep(10)
crawlingOders(driver)
time.sleep(100)

driver.quit()