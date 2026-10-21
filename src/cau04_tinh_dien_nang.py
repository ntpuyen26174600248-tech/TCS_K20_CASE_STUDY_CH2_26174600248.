# Khai bao du lieu ban dau 
cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000
# Cong thuc: dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
# chi_phi = dien_nang_kwh * don_gia_kwh
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("Dien nang tieu thu:", dien_nang_kwh, "kWh, kieu:", type(dien_nang_kwh))
print("Chi phi dien:", chi_phi, "VND, kieu:", type(chi_phi))
# Du doan ket qua truoc khi chay:
# - Dien nang = 250 * 90 / 60 / 1000 = 0.375 kwh
# - Chi phi = 0.375 * 3000 = 1125.0 VND
# Thay so phut bang 60 roi chay lai va so sanh
so_phut = 60
dien_nang_kwh_moi = cong_suat_w * so_phut / 60 / 1000
chi_phi_moi = dien_nang_kwh_moi * don_gia_kwh
print("\n--- Sau khi thay doi so phut thanh 60 ---")
print("Dien nang moi:", dien_nang_kwh_moi, "kWh")
print("Chi phi moi:", chi_phi_moi, "VND")