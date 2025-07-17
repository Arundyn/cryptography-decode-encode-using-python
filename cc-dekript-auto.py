def caesar_cipher_decrypt(text, shift):
    decrypted_text = []
    for char in text:
        if 'a' <= char <= 'z':
            decrypted_text.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            decrypted_text.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

cipher_text = "kvbsqrd, iye'bo kvwycd drobo! Xyg pyb dro psxkv ..."
for shift in range(1, 26):
    print(f"Shift {shift}: {caesar_cipher_decrypt(cipher_text, shift)}")
