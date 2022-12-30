import random


def is_prime(n, k=1000):
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


n = random.getrandbits(512)
if is_prime(int(n)):
    print(n, "is prime")
else:
    print(n, "is not prime")
