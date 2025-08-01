from selenium.webdriver.common.by import By
from openpyxl import Workbook
from datetime import datetime
import os
import time

def crawlingOders(driver):
    time.sleep(5)
    rows = driver.find_elements(By.CSS_SELECTOR, 'tr.dui-table-row.dui-table-row-level-0')

    current_datetime = datetime.now().date()
    folder_name = f"Orders_{current_datetime}"
    os.makedirs(folder_name, exist_ok=True)

    wb = Workbook()
    ws = wb.active
    ws.title = "Orders"

    ws.append(["Long ID", "Short ID", "Total Amount", "Status"])


    for row in rows:
        cols = row.find_elements(By.CSS_SELECTOR, 'td.dui-table-cell')
        if len(cols) == 5:
            empty = cols[0].text.strip()
            longID = cols[1].text.strip()
            shortID = cols[2].text.strip()
            totalAmount = cols[3].text.strip()
            status = cols[4].text.strip()

            ws.append([longID, shortID, totalAmount, status])

            print(f"Long ID: {longID}, Short ID: {shortID}, Total Amount: {totalAmount}, Status: {status}") 
    
    wb.save(f"{folder_name}/orders.xlsx")
    print("Dữ liệu đã được lưu vào 'orders.xlsx'")