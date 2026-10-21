# Nhap thong tin chi tiet phien su dung tu ban phim
ma_phien = input("Nhap ma phien: ")
ma_may = input("Nhap ma may: ")
cong_suat_input = input("Nhap cong suat thiet bi (W): ")
so_phut_input = input("Nhap so phut su dung: ")
don_gia_input = input("Nhap don gia dien (VND/kWh): ")
# Chuyen doi kieu du lieu (Ep kieu sang float/int de tinh toan)
cong_suat_w = float(cong_suat_input)
so_phut = int(so_phut_input)
don_gia_kwh = float(don_gia_input)
# Tinh toan dien nang tieu thu (kWh) va chi phi (VND)
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
# In ket qua theo dung dinh dang toi thieu cua de bai
print("\n--- THONG TN KET QUA PHIEN SU DUNG ---")
print(f"Ma phien: {ma_phien}")
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh}")
print(f"Cgi phi: {chi_phi}")