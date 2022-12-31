# def load_data(file_path):
#     with open(file_path, "r") as file:
#         data = file.read()
#     return data


# def write_data(file_path, data):
#     with open(file_path, "w") as file:
#         file.write(data)


# def SHA(data):
#     print("Select hash function: ")
#     while (True):
#         print("1. sha224")
#         print("2. sha256")
#         print("3. sha384")
#         print("4. sha512")
#         change = input(
#             "Do you want to change the hash function with sha224, sha256, sha384, sha512? (1, 2, 3, 4): ")
#         if (change == "1" or change == "2" or change == "3" or change == "4"):
#             break
#         else:
#             print("Please select again")
#     if (change == "1"):
#         int_change = 224
#     elif (change == "2"):
#         int_change = 256
#     elif (change == "3"):
#         int_change = 384
#     elif (change == "4"):
#         int_change = 512
#     SHA2_cyphertext = SHA2_encryption.encode(data, int_change)
#     return SHA2_cyphertext, int_change


# def sending_text(data):
#     print("Alice wants to send a message to Bob")
#     print("Message:", data)
#     print("")
#     AES_cyphertext, AES_key = AES_encryption.encode(data)
#     print("Ciphertext AES:", AES_cyphertext)
#     keysize = input("Enter key size: ")
#     RSA_cyphertext, RSA_n, RSA_publicKey = RSA_encryption.encode(data, keysize)
#     print("Ciphertext RSA:", RSA_cyphertext)
#     SHA2_cyphertext, SHA2_int_change = SHA(data)
#     SHA2_RSA_cyphertext, SHA2_RSA_n, SHA2_RSA_publicKey = RSA_encryption.encode(
#         SHA2_cyphertext, keysize)
#     SHA2_bit_change_RSA_cyphertext,  SHA2_RSA_n, SHA2_RSA_publicKey = RSA_encryption.encode(
#         str(SHA2_int_change), keysize)
#     print("Ciphertext SHA2:", SHA2_cyphertext)
#     print("Ciphertext SHA2 RSA:", SHA2_RSA_cyphertext)
#     data_write = []
#     data_write.append("AES_cyphertext:" + AES_cyphertext)
#     data_write.append("AES_key:" + str(AES_key))
#     data_write.append("RSA_cyphertext:" + RSA_cyphertext)
#     data_write.append("RSA_n:" + str(RSA_n))
#     data_write.append("RSA_publicKey:" + str(RSA_publicKey))
#     data_write.append("SHA2_RSA_cyphertext:" + SHA2_RSA_cyphertext)
#     data_write.append("SHA2_RSA_n:" + str(SHA2_RSA_n))
#     data_write.append("SHA2_RSA_publicKey:" + str(SHA2_RSA_publicKey))
#     data_write.append("SHA2_bit_change_RSA_cyphertext:" +
#                       str(SHA2_bit_change_RSA_cyphertext))
#     data_write = "\n".join(data_write)
#     write_data("Ciphertext.txt", data_write)


# def reading_text():
#     data = load_data("Ciphertext.txt")
#     data = data.split("\n")
#     AES_cyphertext = data[0].split(":")[1]
#     AES_key = int(data[1].split(":")[1])
#     RSA_cyphertext = data[2].split(":")[1]
#     RSA_n = int(data[3].split(":")[1])
#     RSA_publicKey = int(data[4].split(":")[1])
#     SHA2_RSA_cyphertext = data[5].split(":")[1]
#     SHA2_RSA_n = int(data[6].split(":")[1])
#     SHA2_RSA_publicKey = int(data[7].split(":")[1])
#     SHA2_bit_change_RSA_cyphertext = data[8].split(":")[1]
#     print("Bob to read the message from Alice")
#     AES_message = AES_encryption.decode(AES_cyphertext, AES_key)
#     print("Decrypted AES:", AES_message)
#     RSA_message = RSA_encryption.decode(RSA_cyphertext, RSA_n, RSA_publicKey)
#     print("Decrypted RSA:", RSA_message)
#     SHA2_bit_change = int(RSA_encryption.decode(
#         SHA2_bit_change_RSA_cyphertext, SHA2_RSA_n, SHA2_RSA_publicKey))
#     SHA2_RSA_message = RSA_encryption.decode(
#         SHA2_RSA_cyphertext, SHA2_RSA_n, SHA2_RSA_publicKey)
#     if (SHA2_RSA_message == SHA2_encryption.encode(RSA_message, SHA2_bit_change)):
#         data_write = AES_message + "\n" + "SHA2-RSA:" + "Correct"
#         print("SHA2-RSA:", "Correct")
#         write_data("Decrypted.txt", data_write)
#     else:
#         data_write = AES_message + "\n" + "SHA2-RSA:" + "Incorrect"
#         print("SHA2-RSA:", "Incorrect")
#         write_data("Decrypted.txt", data_write)
    
    


# print("Running....")
# data = "The king of football has left us but his legacy will never be forgotten. RIP KING PELE"
# sending_text(data)
# print("")
# reading_text()

