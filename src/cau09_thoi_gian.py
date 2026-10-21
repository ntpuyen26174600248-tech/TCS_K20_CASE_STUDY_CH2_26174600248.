from datetime import datetime
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print("Thoi diem (doi tuong datetime):", thoi_diem)
print("Kieu du lieu:", type(thoi_diem))
print("Thoi diem (chuoi dinh dang str):", thoi_diem_text)
print("Kieu du lieu:", type(thoi_diem_text))
# Bo sung
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print("\n--- Tinh thoi luong su dung ---")
print("Thoi luong:", thoi_luong)
print("Kieu du lieu cua thoi luong:", type(thoi_luong))