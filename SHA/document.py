from bitarray import bitarray
from bitarray import  util
from textwrap import wrap
from consts import Const
W = 64 
M = 1 << W
FF = M - 1



def RR(x, b):
    return ((x >> b) | (x << (W - b))) & FF


def Pad(W):

    mdi = len(W) % 64
    L = (len(W) << 3).to_bytes(8, 'big')
    npad = 55 - mdi if mdi < 56 else 119 - mdi
    return bytes(W, 'ascii') + b'\x80' + (b'\x00' * npad) + L


def Pad512(W):

    mdi = len(W) % 128
    L = (len(W) << 3).to_bytes(16, 'big')
    npad = 111 - mdi if mdi < 112 else 239 - mdi
    return bytes(W, 'ascii') + b'\x80' + (b'\x00' * npad) + L


def Sha256CF(Wt, Kt, A, B, C, D, E, F, G, H):

    Ch = (E & F) ^ (~E & G)
    Ma = (A & B) ^ (A & C) ^ (B & C)
    S0 = RR(A, 2) ^ RR(A, 13) ^ RR(A, 22)
    S1 = RR(E, 6) ^ RR(E, 11) ^ RR(E, 25)
    T1 = H + S1 + Ch + Wt + Kt
    return (T1 + S0 + Ma) & FF, A, B, C, (D + T1) & FF, E, F, G


def Sha512CF(Wt, Kt, A, B, C, D, E, F, G, H):

    Ch = (E & F) ^ (~E & G)
    Ma = (A & B) ^ (A & C) ^ (B & C)
    S0 = RR(A, 28) ^ RR(A, 34) ^ RR(A, 39)
    S1 = RR(E, 14) ^ RR(E, 18) ^ RR(E, 41)
    T1 = H + S1 + Ch + Wt + Kt
    return (T1 + S0 + Ma) & FF, A, B, C, (D + T1) & FF, E, F, G


def Sha256(M):

    M = Pad(M)
    DG = list(Const.H)
    for j in range(0, len(M), 64):
        S = M[j:j + 64]
        W = [0] * 64
        W[0:16] = [int.from_bytes(S[i:i + 4], 'big') for i in range(0, 64, 4)]

        for i in range(16, 64):
            s0 = RR(W[i - 15], 7) ^ RR(W[i - 15], 18) ^ (W[i - 15] >> 3)
            s1 = RR(W[i - 2], 17) ^ RR(W[i - 2], 19) ^ (W[i - 2] >> 10)
            W[i] = (W[i - 16] + s0 + W[i-7] + s1) & FF

        A, B, C, D, E, F, G, H = DG

        for i in range(64):
            A, B, C, D, E, F, G, H = Sha256CF(W[i], Const.K[i], A, B, C, D, E, F, G, H)
        DG = [(X + Y) & FF for X, Y in zip(DG, (A, B, C, D, E, F, G, H))]
    return b''.join(Di.to_bytes(4, 'big') for Di in DG)


def Sha224(M):

    M = Pad(M)
    DG = list(Const.H1)
    for j in range(0, len(M), 64):
        S = M[j:j + 64]
        W = [0] * 64
        W[0:16] = [int.from_bytes(S[i:i + 4], 'big') for i in range(0, 64, 4)]

        for i in range(16, 64):
            s0 = RR(W[i - 15], 7) ^ RR(W[i - 15], 18) ^ (W[i - 15] >> 3)
            s1 = RR(W[i - 2], 17) ^ RR(W[i - 2], 19) ^ (W[i - 2] >> 10)
            W[i] = (W[i - 16] + s0 + W[i-7] + s1) & FF

        A, B, C, D, E, F, G, H = DG

        for i in range(64):
            A, B, C, D, E, F, G, H = Sha256CF(W[i], Const.K[i], A, B, C, D, E, F, G, H)
        DG = [(X + Y) & FF for X, Y in zip(DG, (A, B, C, D, E, F, G, H))]
    return b''.join(Di.to_bytes(4, 'big') for Di in DG)


def Sha512(M):

    M = Pad512(M)
    DG = list(Const.H2)
    for j in range(0, len(M), 128):
        S = M[j:j + 128]
        W = [0] * 128
        W[0:16] = [int.from_bytes(S[i:i + 8], 'big') for i in range(0, 128, 8)]

        for i in range(16, 80):
            s0 = RR(W[i - 15], 1) ^ RR(W[i - 15], 8) ^ (W[i - 15] >> 7)
            s1 = RR(W[i - 2], 19) ^ RR(W[i - 2], 61) ^ (W[i - 2] >> 6)
            W[i] = (W[i - 16] + s0 + W[i-7] + s1) & FF

        A, B, C, D, E, F, G, H = DG

        for i in range(80):
            A, B, C, D, E, F, G, H = Sha512CF(W[i], Const.K1[i], A, B, C, D, E, F, G, H)
        DG = [(X + Y) & FF for X, Y in zip(DG, (A, B, C, D, E, F, G, H))]
    return b''.join(Di.to_bytes(8, 'big') for Di in DG)



if __name__ == "__main__":

    """hash = Sha224(u'The quick brown fox jumps over the lazy dog')
    hash = ''.join('{:02x}'.format(i) for i in hash)
    print(wrap(hash, 8))

    hash = Sha256(u'The quick brown fox jumps over the lazy dog')
    hash = ''.join('{:02x}'.format(i) for i in hash)
    print(wrap(hash, 8))"""

    hash = Sha512(u'The quick brown fox jumps over the lazy dog')
    hash = ''.join('{:02x}'.format(i) for i in hash)
    print(wrap(hash, 8))
















    h0 = 0xc1059ed8
    h1 = 0x367cd507
    h2 = 0x3070dd17
    h3 = 0xf70e5939
    h4 = 0xffc00b31
    h5 = 0x68581511
    h6 = 0x64f98fa7
    h7 = 0xbefa4fa4
    k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5, 
         0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 
         0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 
         0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967, 
         0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 
         0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070, 
         0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3, 
         0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]
    
    
    
    
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