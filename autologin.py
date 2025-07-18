from selenium.webdriver.common.by import By
import time

def autoLoginLocation(driver):
    username = 'InmamNguyen'
    
    time.sleep(5)
    buttonUsername = driver.find_element(By.ID, 'Username')
    buttonUsername.send_keys(username)
    time.sleep(5)
    buttonContinue = driver.find_element(By.CSS_SELECTOR, 'button.ant-btn.ant-btn-primary')
    buttonContinue.click()
    
    time.sleep(5)    
    buttonPassword = driver.find_element(By.ID, 'password')
    buttonPassword.send_keys('Nguyen102838')
    time.sleep(5)
    buttonContinue = driver.find_element(By.CSS_SELECTOR, 'button.ant-btn.ant-btn-primary')
    buttonContinue.click()