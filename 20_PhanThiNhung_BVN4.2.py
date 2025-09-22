def ma_hoa(plaintext, k):
    ket_qua = ""
 
    for ky_tu in plaintext:
        if ky_tu.isalpha():
            so_nguyen = ord(ky_tu.upper()) - ord('A')
            so_da_ma_hoa = (so_nguyen + k) % 26
            chu_cai_da_ma_hoa = chr(so_da_ma_hoa + ord('A'))
            ket_qua += chu_cai_da_ma_hoa
        else:
            ket_qua += ky_tu        
    return ket_qua
P = "PhanThiNhung"
k = 20
chuoi_da_ma_hoa = ma_hoa(P, k)
print(f"Chuỗi đã mã hóa: {chuoi_da_ma_hoa}")
