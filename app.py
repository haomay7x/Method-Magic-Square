def magic_square(text, mode='encrypt'):
    square = [2, 7, 6, 9, 5, 1, 4, 3, 8]
    while len(text) % 9 != 0:
        text += "_"
    
    result = ""
    for i in range(0, len(text), 9):
        block = text[i:i+9]
        new_block = [""] * 9
        for j in range(9):
            if mode == 'encrypt':
                new_block[square[j]-1] = block[j]
            else:
                new_block[j] = block[square[j]-1]
        result += "".join(new_block)
    return result

msg = str(input("Введите строку: "))
encrypted = magic_square(msg, 'encrypt')
decrypted = magic_square(encrypted, 'decrypt')

print(f"Зашифрованно: {encrypted}")
print(f"Расшифрованно: {decrypted}")