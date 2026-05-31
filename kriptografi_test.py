import time
from cryptography.fernet import Fernet
# Catatan: pastikan sudah menginstal pycryptodome (pip install pycryptodome)
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# 1. MENYIAPKAN DATA UJI (PLAINTEXT)
plaintext = b"Pesan rahasia pendek."
print(f"=== DATA AWAL ===")
print(f"Plaintext asli : {plaintext.decode()}")
print(f"Ukuran asli    : {len(plaintext)} bytes\n")


# 2. IMPLEMENTASI KRIPTOGRAFI SIMETRIS (AES / FERNET)
print("=== 1. PENGUJIAN METODE SIMETRIS (AES/FERNET) ===")
# Generasi Kunci
start_key_fernet = time.perf_counter()
fernet_key = Fernet.generate_key()
f = Fernet(fernet_key)
t_key_fernet = time.perf_counter() - start_key_fernet

# Proses Enkripsi
start_enc_fernet = time.perf_counter()
ciphertext_fernet = f.encrypt(plaintext)
t_enc_fernet = time.perf_counter() - start_enc_fernet

# Proses Dekripsi
start_dec_fernet = time.perf_counter()
decrypted_fernet = f.decrypt(ciphertext_fernet)
t_dec_fernet = time.perf_counter() - start_dec_fernet

print(f"Ciphertext (Fernet) : {ciphertext_fernet[:50]}...")
print(f"Ukuran Ciphertext   : {len(ciphertext_fernet)} bytes")
print(f"Waktu Gen Kunci     : {t_key_fernet * 1_000_000:.2f} microseconds")
print(f"Waktu Enkripsi      : {t_enc_fernet * 1_000_000:.2f} microseconds")
print(f"Waktu Dekripsi      : {t_dec_fernet * 1_000_000:.2f} microseconds\n")


# 3. IMPLEMENTASI KRIPTOGRAFI ASIMETRIS (RSA 2048-BIT)
print("=== 2. PENGUJIAN METODE ASIMETRIS (RSA) ===")
# Generasi Sepasang Kunci (Public & Private Key)
start_key_rsa = time.perf_counter()
rsa_key = RSA.generate(2048)
private_key = rsa_key
public_key = rsa_key.publickey()
t_key_rsa = time.perf_counter() - start_key_rsa

# Proses Enkripsi (Menggunakan Public Key)
cipher_rsa_enc = PKCS1_OAEP.new(public_key)
start_enc_rsa = time.perf_counter()
ciphertext_rsa = cipher_rsa_enc.encrypt(plaintext)
t_enc_rsa = time.perf_counter() - start_enc_rsa

# Proses Dekripsi (Menggunakan Private Key)
cipher_rsa_dec = PKCS1_OAEP.new(private_key)
start_dec_rsa = time.perf_counter()
decrypted_rsa = cipher_rsa_dec.decrypt(ciphertext_rsa)
t_dec_rsa = time.perf_counter() - start_dec_rsa

print(f"Ciphertext RSA (Hex): {ciphertext_rsa.hex()[:50]}...")
print(f"Ukuran Ciphertext   : {len(ciphertext_rsa)} bytes")
print(f"Waktu Gen Kunci     : {t_key_rsa * 1000:.2f} ms")
print(f"Waktu Enkripsi      : {t_enc_rsa * 1000:.2f} ms")
print(f"Waktu Dekripsi      : {t_dec_rsa * 1000:.2f} ms\n")