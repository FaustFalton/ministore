# MINISTORE (BÀI 1 ĐẾN BÀI 6)

# B1: Khởi tạo cửa hàng và chào khách
ten_cua_hang = "MiniStore"
ten_khach = input("Nhap ten cua ban: ")
print(f"\nChao mung {ten_khach} den voi {ten_cua_hang}!\n")

# B2-3-4: Quản lý kho hàng và giá cả ban đầu
kho = ["sua tuoi", "banh mi", "trung ga", "ca phe", "duong"]
gia = [5000, 25000, 15000, 10000, 60000]  # Giá tương ứng với 5 món ban đầu

# Sửa đổi vị trí: Thay "trung ga" bằng "nuoc suoi"
vt = kho.index("trung ga")
kho[vt] = "nuoc suoi"  # Thay thế trực tiếp thay vì pop và insert
gia[vt] = 8000         # Cập nhật lại giá tiền cho nước suối nếu cần

# Thêm khuyến mãi "keo" vào đầu danh sách (B3)
kho.insert(0, "keo")
gia.insert(0, 3000)    # Thêm giá tiền của kẹo vào đầu danh sách giá tương ứng

# Viết hoa chữ cái đầu cho kho hàng (B4)
for i in range(len(kho)):
    kho[i] = kho[i].capitalize()

# B5: Tìm sản phẩm đắt nhất, rẻ nhất
vt_max, vt_min = 0, 0
for i in range(1, len(gia)):
    if gia[i] > gia[vt_max]:
        vt_max = i
    if gia[i] < gia[vt_min]:
        vt_min = i

print("--- THÔNG TIN KHO HÀNG ---")
for i in range(len(kho)):
    print(f"{i + 1}. {kho[i]} - {gia[i]}d")
print(f"-> Dat nhat: {kho[vt_max]} ({gia[vt_max]}d) | Re nhat: {kho[vt_min]} ({gia[vt_min]}d)\n")

# B6: Giỏ hàng và Vòng lặp mua hàng
gio_hang = []
print("--- BẮT ĐẦU MUA HÀNG ---")
while True:
    mon_chon = input("Nhap ten mon muon mua (nhap 'xong' de ket thuc): ").strip().capitalize()
    
    # Sentinel dừng vòng lặp
    if mon_chon == "Xong":
        break
        
    # Kiểm tra tồn tại trong kho (B2 & 6)
    if mon_chon in kho:
        gio_hang.append(mon_chon)
        print(f" -> Da them [{mon_chon}] vao gio.")
    else:
        print(" -> Khong co mon nay trong kho, vui long chon lai!")

# TỔNG KẾT HÓA ĐƠN & GIẢM GIÁ 10% (B5 & 6)
tong_tien = 0
for sp in gio_hang:
    tong_tien += gia[kho.index(sp)]

tien_phai_tra = int(tong_tien * 0.9)  # Giảm 10%, làm tròn số nguyên

print("\n" + "="*30)
print(f"HOA DON THANH TOAN: {ten_khach.upper()}")
print("Cac mon da mua :", ", ".join(gio_hang) if gio_hang else "Chưa mua món nào")
print("So luong mon    :", len(gio_hang))
print(f"Tong tien goc   : {tong_tien} d")
print(f"Tien sau giam10%: {tien_phai_tra} d")
print("Cam on quy khach da mua hang!")
print("="*30)
