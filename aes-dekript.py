from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad
import base64

# Fungsi untuk dekripsi dengan AES
def aes_decrypt(iv, encrypted_text, key):
    # Mengubah IV dan ciphertext dari base64
    iv = base64.b64decode(iv)
    encrypted_text = base64.b64decode(encrypted_text)
    
    # Membuat objek cipher AES dengan IV yang sama
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Mendekripsi dan menghapus padding
    decrypted_text = unpad(cipher.decrypt(encrypted_text), AES.block_size).decode('utf-8')
    
    return decrypted_text

# Main program untuk dekripsi
key = input("Masukkan kunci dalam base64: ")
iv = input("Masukkan IV dalam base64: ")
encrypted_text = input("Masukkan teks terenkripsi dalam base64: ")

# Mengonversi kembali kunci dari base64 ke bytes
key = base64.b64decode(key)

# Dekripsi
decrypted_text = aes_decrypt(iv, encrypted_text, key)
print("\nHasil Dekripsi:")
print(decrypted_text)
