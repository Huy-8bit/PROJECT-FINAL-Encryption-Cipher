import random
import os

def random_prime(size_bit):
    while True:
        # Generate a random number with the specified number of bits
        p = random.getrandbits(size_bit)
        # Set the 2 least significant bits to 1 (to ensure p is odd)
        p |= 3
        if is_prime(p):
            
            return p

def is_prime(n):
    if n in (2, 3):
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True



text = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!,. "





p = random_prime(8)
print("p=",p)
q = random_prime(8)
print("q=",q)
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
    

print("modulo=",n)
print("public key=",publicKey)
print("private key=",privateKey)
plainText = input("Enter plain text: ")
encryptedText = ""
for k in plainText:
    m = 0
    for l in text:
        if k == l:
            if m < 10:
                m = m + 00
            encryptedText = encryptedText + (str((m ** publicKey) % n)) + " "
            break
        m+=1
print("Encrypted text: ", encryptedText)

decryptedText = ""
for s in encryptedText.split(" "):
    for k in text:
        m = 0
        for l in text:
            if k == l:
                if s == (str((m ** publicKey) % n)):
                    decryptedText = decryptedText + l
                break
            m += 1

print("Decrypted text: ", decryptedText)


