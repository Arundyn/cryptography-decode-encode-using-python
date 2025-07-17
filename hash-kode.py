import hashlib

# Fungsi untuk hashing menggunakan algoritma tertentu
def hash_text(text, algorithm="sha256"):
    # Konversi teks ke bytes
    text_bytes = text.encode("utf-8")

    # Pilih algoritma hashing
    if algorithm == "md5":
        hash_object = hashlib.md5(text_bytes)
    elif algorithm == "sha1":
        hash_object = hashlib.sha1(text_bytes)
    elif algorithm == "sha256":
        hash_object = hashlib.sha256(text_bytes)
    elif algorithm == "sha512":
        hash_object = hashlib.sha512(text_bytes)
    else:
        raise ValueError("Algoritma tidak didukung. Gunakan: md5, sha1, sha256, sha512")

    # Kembalikan hasil hashing dalam format heksadesimal
    return hash_object.hexdigest()

# Main program
text = input("Masukkan teks yang akan di-hash: ")
algorithm = input("Pilih algoritma hashing (md5, sha1, sha256, sha512): ").lower()

try:
    hashed_text = hash_text(text, algorithm)
    print(f"Hasil hashing ({algorithm}): {hashed_text}")
except ValueError as e:
    print(e)
