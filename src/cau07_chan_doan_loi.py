# 1. Ep kieu cong_suat_w sang float de co the thuc hien phep tinh toan hoc.
# 2. Sua loi cu phap f-string (doi bien 'dien_nang' thanh 'dien_nang_kwh')
ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: "))
so_phut = int(input("Nhap so phut: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f} kWh")

# --- CHAN DOAN VA NGUYEN NHAN LOI ---
# - Loi 1 (TypeError): 'cong_suat_w' nhan gia tri tu input() co kieu du lieu la str, khong the nhan truc tiep voi kieu int ('so_phut')
#  - Cach khac phuc: Dung ham float() boc ben ngoai input() de chuyen kieu du lieu.
# - Loi 2 (SyntaxError): Cu phap f-string tai dong in dien nang bi goi nham ten bien 'dien_nang'.
#  - Cach khac phuc: Sua lai thanh '{dien_nang_kwh:.3f}'.