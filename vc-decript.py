def vigenere_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ""
    
    key_index = 0  # Untuk melacak posisi karakter dalam key
    
    for char in ciphertext:
        if char in alphabet:
            shift = alphabet.index(key[key_index])  # Nilai shift berdasarkan key
            new_index = (alphabet.index(char) - shift) % 26
            plaintext += alphabet[new_index]
            
            # Geser ke karakter key berikutnya, ulangi dari awal jika sudah habis
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char  # Biarkan karakter non-huruf tetap sama

    return plaintext

# Main program
ciphertext = input("Masukkan teks terenkripsi: ")
key = input("Masukkan kunci enkripsi (hanya huruf): ")

decrypted_text = vigenere_decrypt(ciphertext, key)
print("\nHasil Dekripsi:")
print(decrypted_text)
