import hashlib

def sha256(data):
    print("Enter data to hash: ")
    data = input()
    # Generate the SHA-1 hash
    sha1_hash = hashlib.sha1(data.encode())

    # Get the hexadecimal representation of the hash
    hex_hash = sha1_hash.hexdigest()

    print("After hash using SHA: " ,hex_hash);

sha256("data")