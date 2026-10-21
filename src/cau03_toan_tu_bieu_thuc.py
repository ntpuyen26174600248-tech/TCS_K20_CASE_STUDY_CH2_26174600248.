# Cho tong thoi gian su dung la 135 phut va cac bien ban dau
tong_phut = 135
cong_suat_w = 250
so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60
print("So gio tron:", so_gio)
print("So phut con lai:", so_phut_con_lai)
su_dung_lau = tong_phut > 60
print("Su dung lau:", su_dung_lau)
du_lieu_hop_le = cong_suat_w > 0 and tong_phut > 0
print("Du lieu hop le:", du_lieu_hop_le)
# Du doan:
# - Bieu thuc 1 (100 + 20 * 3): Uu tien nhan truoc (20 * 3 = 60) roi cong 100 = 160
# - Bieu thuc 2 ((100 + 20) * 3): Uu tien trong ngoac truoc (100 + 20 = 120) nhan 3 = 360.
print("Ket qua bieu thuc thu 1:", 100 + 20 * 3)
print("Ket qua bieu thuc thu 2:", (100 + 20) * 3) 
