import pandas as pd
import os
from datetime import datetime

# Tạo tên thư mục theo ngày hôm nay
current_datetime = datetime.now().date()
folder_name = f"Orders_{current_datetime}"
file_path = f"{folder_name}/orders.xlsx"

# Kiểm tra file tồn tại trước khi đọc
if os.path.exists(file_path):
    df = pd.read_excel(file_path)
    print(df.head())
else:
    print(f"Không tìm thấy file: {file_path}")
