import hashlib

p = 0;
q = 0;
text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!,."
publicKey = 0
privateKey = 0
plainText = ""
encryptedText = ""
word = ""
keyWord = ""
keyNumber = 1

data = input("Alice enter message: ")
# Generate the SHA-1 hash
sha1_hash = hashlib.sha1(data.encode())

# Get the hexadecimal representation of the hash
hex_hash = sha1_hash.hexdigest()

print("After hash using SHA: " ,hex_hash);

#RSA
p, q = input("enter two key PRIME numbers seperated by space ").split(" ")
p = int(p)
q = int(q)
n = p * q
phiN = (p-1) * (q-1)

for i in range(1, 10000):
    if 0 != phiN % i:
        publicKey = round(i)
        break

for j in range(0, 10000):
    d = 1 + (j * phiN)
    d2 = d / publicKey
    if 0 == d % publicKey:
        privateKey = round(d2)
        break
    
print("p=",p)
print("q=",q)
print("modulo=",n)
print("public key=",publicKey)
print("private key=",privateKey)

encryptedText = ""
for k in data:
    m = 0
    for l in text:
        if k == l:
            if m < 10:
                m = m + 00
            encryptedText = encryptedText + (str((m ** publicKey) % n)) + " "
            break
        m+=1
print("Encrypted message : ", encryptedText)

decryptedText = ""
#decryptedText = input("Enter encrypted text: ")
# plainText = ""
for s in encryptedText.split(" "):
    for k in text:
        m = 0
        for l in text:
            if k == l:
                if s == (str((m ** publicKey) % n)):
                    decryptedText = decryptedText + l
                break
            m += 1

print("Bob receive message: ", decryptedText)