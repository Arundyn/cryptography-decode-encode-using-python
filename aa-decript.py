def decrypt(ciphertext, key):
    plaintext = ""  
    i = 0  
    while i < len(ciphertext):  
        plaintext += ciphertext[i]  # Ambil karakter asli
        i += key + 1  # Lewati karakter acak sebanyak 'key'
    return plaintext  

# Contoh Penggunaan
ciphertext = input("Masukkan teks terenkripsi: ")
key = int(input("Masukkan kunci enkripsi (1-10): "))

while not (1 <= key <= 10):
    print("Kunci tidak valid, coba lagi!")
    key = int(input("Masukkan kunci enkripsi (1-10): "))

decrypted_text = decrypt(ciphertext, key)
print("\nHasil Dekripsi:")
print(decrypted_text)
