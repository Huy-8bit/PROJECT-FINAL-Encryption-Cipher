import random


def gcd(a, b):
    """
    Computes the greatest common divisor of two integers using the Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a


def inverse(a, m):
    """
    Computes the modular inverse of a modulo m using the extended Euclidean algorithm.
    """
    m0 = m
    x0 = 0
    x1 = 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t
    if x1 < 0:
        x1 = x1 + m0
    return x1


# Generate two prime numbers
p = random.randint(2**1023, 2**1024-1)
q = random.randint(2**1023, 2**1024-1)

# Compute n and phi(n)
n = p * q
phi_n = (p - 1) * (q - 1)

# Choose an integer e such that 1 < e < phi(n) and e and phi(n) are coprime
e = random.randint(2, phi_n-1)
while gcd(e, phi_n) != 1:
    e = random.randint(2, phi_n-1)

# Compute the secret exponent d such that d * e = 1 (mod phi(n))
d = inverse(e, phi_n)

# The private key is (n, d)
private_key = (n, d)

# The public key is (n, e)
public_key = (n, e)

# Print the private key
print(f"Private key: {private_key}")

# Print the public key
print(f"Public key: {public_key}")
