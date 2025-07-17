from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
import base64

# Fungsi untuk enkripsi dengan AES
def aes_encrypt(plaintext, key):
    # Membuat objek cipher AES dalam mode CBC
    cipher = AES.new(key, AES.MODE_CBC)
    
    # Padding plaintext agar panjangnya kelipatan blok AES (16 byte)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    
    # Menggabungkan IV dengan ciphertext untuk pengiriman
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    encrypted_text = base64.b64encode(ciphertext).decode('utf-8')
    
    return iv, encrypted_text

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

# Main program
key = get_random_bytes(16)  # Menghasilkan kunci acak 16 byte (128-bit)
print(f"Kunci: {base64.b64encode(key).decode()}")  # Menampilkan kunci dalam base64 untuk referensi

plaintext = input("Masukkan teks untuk dienkripsi: ")

# Enkripsi
iv, encrypted_text = aes_encrypt(plaintext, key)
print(f"\nIV: {iv}")
print(f"Teks Terenkripsi: {encrypted_text}")

# Dekripsi
decrypted_text = aes_decrypt(iv, encrypted_text, key)
print(f"\nHasil Dekripsi: {decrypted_text}")
