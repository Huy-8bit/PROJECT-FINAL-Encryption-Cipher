import base64
from Crypto.Cipher import AES

# Set the key and initialization vector (IV)
key = b"0123456789abcdef0123456789abcdef"  # 32-byte key
iv = b"0123456789abcdef"  # 16-byte IV

# Initialize the cipher
cipher = AES.new(key, AES.MODE_CFB, iv)

# Encrypt some data
data = b"Hello, World!"
ciphertext = cipher.encrypt(data)

# Encode the ciphertext as base64
encoded_ciphertext = base64.b64encode(ciphertext)

print(f"Ciphertext: {encoded_ciphertext}")
