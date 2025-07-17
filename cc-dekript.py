def caesar_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    plaintext = ""

    for char in ciphertext:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index - key) % len(alphabet)
            plaintext += alphabet[new_index]
        else:
            plaintext += char  # Biarkan karakter selain huruf tetap sama
    return plaintext

# Main Program
ciphertext = input("Masukkan teks terenkripsi: ")
key = int(input("Masukkan kunci enkripsi (1-25): "))

while not (1 <= key <= 25):
    print("Kunci tidak valid, coba lagi!")
    key = int(input("Masukkan kunci enkripsi (1-25): "))

decrypted_text = caesar_decrypt(ciphertext, key)
print("\nHasil Dekripsi:")
print(decrypted_text)
