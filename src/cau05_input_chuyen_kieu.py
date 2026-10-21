ma_may = input("Nhap ma may: ")
cong_suat_input = input("Nhap cong suat W: ")
so_phut_input = input("Nhap so phut: ")
don_gia_input = input("Nhap don gia dien/kWh: ")
print("--- Kieu du lieu ban dau (str) ---")
print(type(ma_may), type(cong_suat_input), type(so_phut_input), type(don_gia_input))
# Chuyen doi kieu du lieu:
# - Cong suat sang float
# - So phut sang int
# - Don gia sang float
cong_suat_w = float(cong_suat_input)
so_phut = int(so_phut_input)
don_gia_kwh = float(don_gia_input)
# Tinh lai dien nang va chi phi sau khi chuyen kieu
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
# In ra ket qua kiem tra
print("\n--- Ket qua tinh toan sau khi chuyen kieu ---")
print(f"Ma may: {ma_may}")
print(f"Dien nang tieu thu: {dien_nang_kwh} kWh (kieu: {type(dien_nang_kwh)})")
print(f"Chi phi dien: {chi_phi} VND (kieu:{type(chi_phi)})")