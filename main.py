import AES_encryption
import RSA_encryption
import SHA2_encryption


# def AES(data):
#     cyphertext,key = AES_encryption.encode(data)
#     plaintext = AES_encryption.decode(cyphertext, key)
#     print("Ciphertext:", cyphertext)
#     print("Plaintext:", plaintext)


# def RSA(data):
#     cyphertext, n, publicKey = RSA_encryption.encode(data)
#     print("Encrypted text:", cyphertext)
#     decryptedText = RSA_encryption.decode(cyphertext, n, publicKey)
#     print("Decrypted text:", decryptedText)


# def SHA2(data):
#     cyphertext = SHA2_encryption.encode(data)
#     print("Encrypted text:", cyphertext)


def load_data(file_path):
    with open(file_path, "r") as file:
        data = file.read()
    return data

def write_data(file_path, data):
    with open(file_path, "w") as file:
        file.write(data)
        




def sending_text():
    data = "Hi Bod,how are you?"
    print("Alice wants to send a message to Bob")
    print("Message:", data)
    print("")
    AES_cyphertext, AES_key = AES_encryption.encode(data)
    print("Ciphertext AES:", AES_cyphertext)
    RSA_cyphertext, RSA_n, RSA_publicKey = RSA_encryption.encode(data)
    print("Ciphertext RSA:", RSA_cyphertext)
    SHA2_cyphertext = SHA2_encryption.encode(data)
    print("Ciphertext SHA2_256:", SHA2_cyphertext)
    
    data_write = []
    data_write.append("AES_cyphertext:" + AES_cyphertext)
    data_write.append("AES_key:" + str(AES_key))
    data_write.append("RSA_cyphertext:" + RSA_cyphertext)
    data_write.append("RSA_n:" + str(RSA_n))
    data_write.append("RSA_publicKey:" + str(RSA_publicKey))
    data_write.append("SHA2_cyphertext:" + SHA2_cyphertext)
    data_write = "\n".join(data_write)
    write_data("Ciphertext.txt", data_write)
    
    

def reading_text():
    data = load_data("Ciphertext.txt")
    data = data.split("\n")
    AES_cyphertext = data[0].split(":")[1]
    AES_key = int(data[1].split(":")[1])
    RSA_cyphertext = data[2].split(":")[1]
    RSA_n = int(data[3].split(":")[1])
    RSA_publicKey = int(data[4].split(":")[1])
    SHA2_cyphertext = data[5].split(":")[1]
    print("Bob to read the message from Alice")
    AES_message = AES_encryption.decode(AES_cyphertext, AES_key)
    print("Decrypted AES:", AES_message)
    RSA_message = RSA_encryption.decode(RSA_cyphertext, RSA_n, RSA_publicKey)
    print("Decrypted RSA:", RSA_message)
    print("Ciphertext SHA2_256:", SHA2_cyphertext)
    if SHA2_cyphertext == SHA2_encryption.encode(AES_message):
        print("The message is not changed")
    else:
        print("The message is changed")
        

print("Running main.py")
# sending_text()
reading_text()


# 149904544555546863715321517132090325075
# d1e501d17f11414fa95f6dcedef67a38