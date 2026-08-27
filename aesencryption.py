import serial
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# ---------------- SERIAL ----------------
ser = serial.Serial('COM13', 115200, timeout=5)   # change COM port
key_hex = ser.readline().decode().strip()

print("Received QRNG Key:", key_hex)

key = bytes.fromhex(key_hex)

# ---------------- AES DEMO ----------------
plaintext = b"HELLO QRNG DEMO"

cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(plaintext, 16))

print("Ciphertext:", ciphertext.hex())

decipher = AES.new(key, AES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), 16)

print("Decrypted:", decrypted.decode())
