import pandas as pd
import time
import os
from datetime import datetime
from crawlingCustomer import crawlingCustomer
from crawlingDriver import crawlingDriver

def workingOdersExcel(driver):
    current_datetime = datetime.now().date()
    folder_name = f"Orders_{current_datetime}"
    file_path = f"{folder_name}/orders.xlsx"

    cus_and_driver = f"CusAndDriver_{current_datetime}"
    os.makedirs(cus_and_driver, exist_ok= True)

    df = pd.read_excel(file_path, usecols=["Long ID", "Short ID"])
    for long_id, short_id in zip(df["Long ID"], df["Short ID"]):
        driver.get(f"https://merchant.grab.com/order/5-C3MKVTDGGKWXNA/history/{long_id}?shortOrderID={short_id}")
        time.sleep(20)
        crawlingCustomer(driver, short_id)
        crawlingDriver(driver, short_id)
