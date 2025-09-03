def mahoa(text, k):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            new_char_code = (ord(char) - ord('A') + k) % 26 + ord('A')
            result += chr(new_char_code)
        elif 'a' <= char <= 'z':
            new_char_code = (ord(char) - ord('a') + k) % 26 + ord('a')
            result += chr(new_char_code)
        else:
            result += char
    return result
plain_text = "Phan Thi Nhung"
key = 20 
encrypted_text = mahoa(plain_text, key)
print(f"Văn bản gốc: {plain_text}")
print(f"Khóa (k): {key}")
print(f"Văn bản đã mã hóa: {encrypted_text}")
