import hashlib

# The message to be hashed
message = "This is the message to be hashed"

# Generate the SHA-1 hash
sha1_hash = hashlib.sha1(message.encode())

# Get the hexadecimal representation of the hash
hex_hash = sha1_hash.hexdigest()

print(hex_hash)