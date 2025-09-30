def rsa_encrypt(message, p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    encrypted = []
    for char in message:
        m = ord(char)
        c = pow(m, e, n) 
        encrypted.append(c)
    return encrypted, n
p = 17
q = 23
e = 5
message = "PhanThiNhung"
encrypted_message, n = rsa_encrypt(message, p, q, e)
print("n =", n)
print("Thông điệp dã mã hoá:", encrypted_message)
