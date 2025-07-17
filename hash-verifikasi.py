import hashlib

# Fungsi untuk hashing teks
def hash_text(text, algorithm="sha256"):
    text_bytes = text.encode("utf-8")
    
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

    return hash_object.hexdigest()

# Fungsi untuk verifikasi hash
def verify_hash(original_text, stored_hash, algorithm="sha256"):
    return hash_text(original_text, algorithm) == stored_hash

# Input pengguna
original_text = input("Masukkan teks asli: ")
stored_hash = input("Masukkan hash yang ingin diverifikasi: ")
algorithm = input("Masukkan algoritma hashing (md5, sha1, sha256, sha512): ").lower()

# Verifikasi
if verify_hash(original_text, stored_hash, algorithm):
    print("✅ Teks cocok dengan hash yang diberikan!")
else:
    print("❌ Teks TIDAK cocok dengan hash yang diberikan.")
