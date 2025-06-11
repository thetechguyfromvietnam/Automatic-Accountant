import pandas as pd
import random
from datetime import datetime


df = pd.read_excel('Taco Place-Danh mục sản phẩm-23032025_201140.xlsx', usecols=["Ten_san_pham", "Don_vi_tinh", "Don_gia"])
df["Don_gia"] = (
    df["Don_gia"]
    .astype(str)
    .str.replace(".", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

df["Tinh_chat"] = 1
df["Ma_so"] = ""

def generate_random_order(df, target_amount):
    selected_items = []
    current_total = 0
    
    while current_total < target_amount:
        item = df.sample().iloc[0]
        price = item["Don_gia"]
        max_qty = (target_amount - current_total) // price
        
        if max_qty <= 0:
            break
        
        qty = random.randint(1,min(3,max_qty))
        line_total = qty * price
        
        selected_items.append({
            "Tinh_chat": 1,
            "Ma_so": "",
            "Ten_san_pham": item["Ten_san_pham"],
            "Don_vi_tinh": item["Don_vi_tinh"],
            "Don_gia": f"{price:,.2f}",
            "So_luong": qty,
        })
        
        current_total += line_total
        
    return pd.DataFrame(selected_items)


try: 
    amount_input = int(input("Nhập số tiền bạn muốn chi tiêu : "))
    target_amount = amount_input - amount_input * 0.08
    result_df = generate_random_order(df, target_amount)
    
    if result_df.empty:
        print("Không thể tạo đơn hàng với số tiền đã nhập.")
    else:
        date_str = datetime.now().strftime("%Y-%m-%d")
        output_file = f"random_order_output_{date_str}.xlsx"
        result_df.to_excel(output_file, index=False)
        print(f"Đơn hàng đã được tạo và lưu vào {output_file}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
    
    
    



print(result_df)
print("🎉 Done! File saved as 'random_order_output.xlsx'")

