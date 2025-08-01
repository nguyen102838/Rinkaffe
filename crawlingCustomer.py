from selenium.webdriver.common.by import By
from datetime import datetime

def crawlingCustomer(driver, short_id):
    current_datetime = datetime.now().date()
    name_customer = driver.find_element(By.CSS_SELECTOR, 'div.css-qbank5-CustomerDisplay')
    number_customer = driver.find_element(By.CSS_SELECTOR, 'div.css-1mzbrkh-CustomerDisplay')
    with open(f"CusAndDriver_{current_datetime}/customer_{short_id}.txt", "w",encoding='utf-8') as file:
        file.write(name_customer.text.strip() + "\n")
        file.write(number_customer.text.strip())