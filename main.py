from Cryptodome.Cipher import AES

# Set the key and initialize the cipher
key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_EAX)

# Encrypt the message
message = b'This is the message to be encrypted'
ciphertext, tag = cipher.encrypt_and_digest(message)

# The ciphertext and tag can be sent to the recipient
# and used to decrypt the message


# Set the key and initialize the cipher
key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_EAX, ciphertext[:16])

# Decrypt the message
plaintext = cipher.decrypt_and_verify(ciphertext[16:], tag)

# The plaintext variable should now contain the original message
