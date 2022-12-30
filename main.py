import AES_encryption

def main():
    key = AES_encryption.generate_random_key()
    data = input("Enter the data to be encrypted:")
    aes = AES_encryption.AES(key)
    cyphertext = AES_encryption.encode(data, aes)
    plaintext = AES_encryption.decode(cyphertext, aes)
    print("Ciphertext:", cyphertext)
    print("Plaintext:", plaintext)
    
main()