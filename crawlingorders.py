from selenium.webdriver.common.by import By
import time

def crawlingOders(driver):
    time.sleep(5)
    rows = driver.find_elements(By.CSS_SELECTOR, 'tr.dui-table-row.dui-table-row-level-0')

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        if len(cols) == 4:
            longID = cols[0].text.strip()
            shortID = cols[1].text.strip()
            totalAmount = cols[2].text.strip()
            status = cols[3].text.strip()
            print(f"Long ID: {longID}, Short ID: {shortID}, Total Amount: {totalAmount}, Status: {status}")