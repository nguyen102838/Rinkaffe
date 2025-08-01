from selenium.webdriver.common.by import By
from datetime import datetime

def crawlingDriver(driver, short_id):
    current_datetime = datetime.now().date()
    name_driver = driver.find_element(By.CSS_SELECTOR, 'div.css-zep5kh-DriverDisplay')
    number_driver = driver.find_element(By.CSS_SELECTOR, 'div.css-vodjec-DriverDisplay')
    with open(f"CusAndDriver_{current_datetime}/driver_{short_id}.txt", "w", encoding='utf-8') as file:
        file.write(name_driver.text.strip() + "\n")
        file.write(number_driver.text.strip())