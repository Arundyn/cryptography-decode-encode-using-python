def caesar_encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    ciphertext = ""

    for char in plaintext:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + key) % len(alphabet)
            ciphertext += alphabet[new_index]
        else:
            ciphertext += char  # Biarkan karakter selain huruf tetap sama
    return ciphertext

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
plaintext = input("Masukkan teks untuk dienkripsi: ")
key = int(input("Masukkan kunci (1-25): "))

while not (1 <= key <= 25):
    print("Kunci tidak valid, coba lagi!")
    key = int(input("Masukkan kunci (1-25): "))

ciphertext = caesar_encrypt(plaintext, key)
print("\nHasil Enkripsi:")
print(ciphertext)

decrypted_text = caesar_decrypt(ciphertext, key)
print("\nHasil Dekripsi:")
print(decrypted_text)
