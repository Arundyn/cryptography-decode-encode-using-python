def vigenere_encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ""
    
    key_index = 0  # Untuk melacak posisi karakter dalam key
    
    for char in plaintext:
        if char in alphabet:
            shift = alphabet.index(key[key_index])  # Nilai shift berdasarkan key
            new_index = (alphabet.index(char) + shift) % 26
            ciphertext += alphabet[new_index]
            
            # Geser ke karakter key berikutnya, ulangi dari awal jika sudah habis
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char  # Biarkan karakter non-huruf tetap sama

    return ciphertext

# Main program
plaintext = input("Masukkan teks untuk dienkripsi: ")
key = input("Masukkan kunci enkripsi (hanya huruf): ")

ciphertext = vigenere_encrypt(plaintext, key)
print("\nHasil Enkripsi:")
print(ciphertext)
