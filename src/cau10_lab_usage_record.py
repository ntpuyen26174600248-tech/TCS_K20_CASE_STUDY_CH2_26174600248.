from datetime import datetime
# Nhap cac thong tin yeu cau tu ban phim
ma_phien = input("Nhap ma phien: ")
ma_may = input("Nhap ma may: ")
cong_suat_input = input("Nhap cong suat thiet bi (W): ")
so_phut_input = input("Nhap thoi gian su dung (phut): ")
don_gia_input = input("Nhap don gia dien (VND/kWh): ")
# Chuyen doi kieu du lieu
cong_suat_w = float(cong_suat_input)
so_phut = int(so_phut_input)
don_gia_kwh = float(don_gia_input)
# Tinh toan dien nang tieu thu (kWh) va chi phi dien uoc tinh (VND)
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
# Kiem tra thoi gian su dung ten 60 phut hay khong (tra ve True/False, khong dung if)
tren_60_phut = so_phut > 60
# Lay thoi diem ghi nhan hien tai
thoi_diem_hien_tai = datetime.now()
thoi_diem_text = thoi_diem_hien_tai.strftime("%Y-%m-%d %H:%M:%S")
# Xuat ket qua theo dung dinh dang mau cua de bai
print("\n--- KET QUA BAO CAO PHIEN SU DUNG ---")
print(f"Ma phien: {ma_phien}")
print(f"May: {ma_may}")
print(f"Cong suat: {cong_suat_w:.2f} W")
print(f"Thoi luong: {so_phut} phut")
print(f"Dien nang: {dien_nang_kwh:.3f} kWh")
print(f"Chi phi: {chi_phi:.2f} VND")
print(f"Tren 60 phut: {tren_60_phut}")
print(f"Ghi nhan luc: {thoi_diem_text}")
# ket thuc bai tap