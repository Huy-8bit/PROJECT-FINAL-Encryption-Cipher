import AES_encryption
import RSA_encryption
import SHA2_encryption
import random


# alice send message to bob
# acice encrypt message using AES with the private key
# bob have a public key and private key
# alice encrypt private key using RSA with bob's public key
# bob decrypt private key using RSA with his private key
# bob decrypt message using AES with the private key
# alice encrypt message using SHA2 with the private key
# alice encrypt SHA2 with RSA with bob's public key
# bob decrypt SHA2 with RSA with his private key
# bob decrypt SHA2 with the private key
# bob compare SHA2 with SHA2 decrypted
# if SHA2 == SHA2 decrypted, SHA2-RSA is correct
# else SHA2-RSA is incorrect


def main():
    data = "RSA is a public-key cryptography algorithm that is widely used for secure data transmission."
    alice_AES_cyphertext, alice_AES_key = AES_encryption.encode(data)
    print("alice_AES_cyphertext=", alice_AES_cyphertext)

    print("alice_AES_key=", alice_AES_key)
    enter_key_size = input("Enter key size:")
    key_size = int(enter_key_size)
    bob_privateKey, bob_n, bob_publicKey = RSA_encryption.create_key(
        key_size)
    print("bob_privateKey=", bob_privateKey)
    print("bob_n=", bob_n)
    print("bob_publicKey=", bob_publicKey)

    alice_AES_key_encrypted = RSA_encryption.encode(
        str(alice_AES_key), bob_publicKey, bob_n)
    print("alice_AES_key_encrypted=", alice_AES_key_encrypted)

    bob_AES_key = RSA_encryption.decode(
        alice_AES_key_encrypted, bob_n, bob_publicKey)
    print("bob_AES_key=", bob_AES_key)
    bob_AES_key_recovered = int(bob_AES_key)
    message = AES_encryption.decode(
        alice_AES_cyphertext, bob_AES_key_recovered)

    print("message=", message)

    alice_SHA2_cyphertext = SHA2_encryption.encode(data, key_size)
    print("alice_SHA2_cyphertext=", alice_SHA2_cyphertext)
    alice_SHA2_cyphertext_encrypted = RSA_encryption.encode(
        alice_SHA2_cyphertext, bob_publicKey, bob_n)

    bob_SHA2_cyphertext_recovered = RSA_encryption.decode(
        alice_SHA2_cyphertext_encrypted, bob_n, bob_publicKey)
    Bob_SHA2_cyphertext = SHA2_encryption.encode(message, key_size)
    print("Bob_SHA2_cyphertext=", Bob_SHA2_cyphertext)
    if bob_SHA2_cyphertext_recovered == Bob_SHA2_cyphertext:
        print("SHA2-RSA is correct")
    else:
        print("SHA2-RSA is incorrect")


main()
