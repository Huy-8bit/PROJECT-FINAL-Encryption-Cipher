import random
import os

text = "!@#$%^&*()-_+=|;:',.<>/?0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "


def is_prime(n, k=10000):
    # Special cases for n <= 1 or n is even
    if n <= 1 or n % 2 == 0:
        return False

    # Write n - 1 as 2^s * d where d is odd
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # Test k times
    for _ in range(k):
        # Choose a random integer a in the range [2, n - 2]
        a = random.randint(2, n - 2)

        # Compute x = a^d mod n
        x = pow(a, d, n)

        # If x == 1 or x == n - 1, the test passes
        if x == 1 or x == n - 1:
            continue

        # Check if x^(2^r) mod n == n - 1 for any 0 <= r < s
        for r in range(s):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            # If none of the above conditions are met, n is not prime
            return False

    # If the test passes for all k values, n is probably prime
    return True


def random_prime(size_bit):
    while True:
        # Generate a random number with the specified number of bits
        p = random.getrandbits(size_bit)
        # Set the 2 least significant bits to 1 (to ensure p is odd)
        p |= 3
        if is_prime(p):
            return p


def create_key(key_size_srt):
    key_size_srt = int(key_size_srt)
    p = random_prime(key_size_srt)
    # print("p=", p)
    q = random_prime(key_size_srt)
    # print("q=", q)
    p = int(p)
    q = int(q)
    n = p * q
    phiN = (p-1) * (q-1)
    privateKey = 0
    publicKey = 0
    for i in range(1, 10000):
        if 0 != phiN % i:
            publicKey = round(i)
            break

    for j in range(0, 10000):
        d = 1 + (j * phiN)
        d2 = d // publicKey
        if 0 == d % publicKey:
            privateKey = round(d2)
            break

    return privateKey, n, publicKey


def create_key(key_size_srt):
    key_size = int(key_size_srt)
    p = random_prime(key_size)
    q = random_prime(key_size)
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
        d2 = d // publicKey
        if 0 == d % publicKey:
            privateKey = round(d2)
            break
    return privateKey, n, publicKey


def encode(data, publicKey, n):

    encryptedText = ""
    for k in data:
        m = 0
        for l in text:
            if k == l:
                if m < 10:
                    m = m + 00
                encryptedText = encryptedText + \
                    (str((m ** publicKey) % n)) + " "
                break
            m += 1
    return encryptedText


def decode(encryptedText, n, publicKey):
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

    return decryptedText



# def decode2(encryptedText, n, publicKey, privateKey):
    # decryptedText = ""
    # for s in encryptedText.split(" "):
    #     for k in text:
    #         m = 0
    #         for l in text:
    #             if k == l:
    #                 if s == (str((m ** publicKey) % n)):
    #                     decryptedText = decryptedText + l
    #                 break
    #             m += 1

    # return decryptedText
    