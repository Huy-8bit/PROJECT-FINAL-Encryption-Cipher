import hashlib
import gmpy2


def sha_256(data: bytes) -> bytes:
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19
    k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
         0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
         0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
         0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
         0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
         0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
         0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
         0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]
    w = [0] * 64
    data += b'\x80'
    data += b'\x00' * ((56 - len(data) % 64) % 64)
    data += len(data).to_bytes(8, 'big')
    for i in range(0, len(data), 64):
        for j in range(16):
            w[j] = int.from_bytes(data[i + j * 4:i + j * 4 + 4], 'big')
        for j in range(16, 64):
            s0 = (w[j - 15] >> 7 | w[j - 15] << 25) ^ (w[j - 15]
                                                       >> 18 | w[j - 15] << 14) ^ (w[j - 15] >> 3)
            s1 = (w[j - 2] >> 17 | w[j - 2] << 15) ^ (w[j - 2]
                                                      >> 19 | w[j - 2] << 13) ^ (w[j - 2] >> 10)
            w[j] = (w[j - 16] + s0 + w[j - 7] + s1) & 0xffffffff
        a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7
        for j in range(64):
            s0 = (a >> 2 | a << 30) ^ (a >> 13 | a << 19) ^ (a >> 22 | a << 10)
            maj = (a & b) ^ (a & c) ^ (b & c)
            t2 = s0 + maj
            s1 = (e >> 6 | e << 26) ^ (e >> 11 | e << 21) ^ (e >> 25 | e << 7)
            ch = (e & f) ^ ((~e) & g)
            t1 = h + s1 + ch + k[j] + w[j]
            h = g
            g = f
            f = e
            e = (d + t1) & 0xffffffff
            d = c
            c = b
            b = a
            a = (t1 + t2) & 0xffffffff
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff
        h5 = (h5 + f) & 0xffffffff
        h6 = (h6 + g) & 0xffffffff
        h7 = (h7 + h) & 0xffffffff
        return h0.to_bytes(4, 'big') + h1.to_bytes(4, 'big') + h2.to_bytes(4, 'big') + h3.to_bytes(4, 'big') + h4.to_bytes(4, 'big') + h5.to_bytes(4, 'big') + h6.to_bytes(4, 'big') + h7.to_bytes(4, 'big')


def sha_224(data: bytes) -> bytes:
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
    w = [0] * 64
    data += b'\x80'
    data += b'\x00' * ((64 - len(data) % 64) % 64)
    data += len(data).to_bytes(8, 'big')
    for i in range(0, len(data), 64):
        for j in range(16):
            w[j] = int.from_bytes(data[i + j * 4:i + j * 4 + 4], 'big')
        for j in range(16, 64):
            s0 = (w[j - 15] >> 7 | w[j - 15] << 25) ^ (w[j - 15]
                                                       >> 18 | w[j - 15] << 14) ^ (w[j - 15] >> 3)
            s1 = (w[j - 2] >> 17 | w[j - 2] << 15) ^ (w[j - 2]
                                                      >> 19 | w[j - 2] << 13) ^ (w[j - 2] >> 10)
            w[j] = (w[j - 16] + s0 + w[j - 7] + s1) & 0xffffffff
        a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7
        for j in range(64):
            s0 = (a >> 2 | a << 30) ^ (a >> 13 | a << 19) ^ (a >> 22 | a << 10)
            maj = (a & b) ^ (a & c) ^ (b & c)
            t2 = s0 + maj
            s1 = (e >> 6 | e << 26) ^ (e >> 11 | e << 21) ^ (e >> 25 | e << 7)
            ch = (e & f) ^ ((~e) & g)
            t1 = h + s1 + ch + k[j] + w[j]
            h = g
            g = f
            f = e
            e = (d + t1) & 0xffffffff
            d = c
            c = b
            b = a
            a = (t1 + t2) & 0xffffffff
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff
        h5 = (h5 + f) & 0xffffffff
        h6 = (h6 + g) & 0xffffffff
        h7 = (h7 + h) & 0xffffffff
    return h0.to_bytes(4, 'big') + h1.to_bytes(4, 'big') + h2.to_bytes(4, 'big') + h3.to_bytes(4, 'big') + h4.to_bytes(4, 'big') + h5.to_bytes(4, 'big') + h6.to_bytes(4, 'big')


# def sha_384(data: bytes) -> bytes:
#     h0 = gmpy2.mpz(0xcbbb9d5dc1059ed8)
#     h1 = gmpy2.mpz(0x629a292a367cd507)
#     h2 = gmpy2.mpz(0x9159015a3070dd17)
#     h3 = gmpy2.mpz(0x152fecd8f70e5939)
#     h4 = gmpy2.mpz(0x67332667ffc00b31)
#     h5 = gmpy2.mpz(0x8eb44a8768581511)
#     h6 = gmpy2.mpz(0xdb0c2e0d64f98fa7)
#     h7 = gmpy2.mpz(0x47b5481dbefa4fa4)
#     k = [gmpy2.mpz(0x428a2f98d728ae22), gmpy2.mpz(0x7137449123ef65cd), gmpy2.mpz(0xb5c0fbcfec4d3b2f), gmpy2.mpz(0xe9b5dba58189dbbc), gmpy2.mpz(0x3956c25bf348b538),
#          gmpy2.mpz(0x59f111f1b605d019), gmpy2.mpz(0x923f82a4af194f9b), gmpy2.mpz(0xab1c5ed5da6d8118), gmpy2.mpz(0xd807aa98a3030242), gmpy2.mpz(0x12835b0145706fbe),
#          gmpy2.mpz(0x243185be4ee4b28c), gmpy2.mpz(0x550c7dc3d5ffb4e2), gmpy2.mpz(0x72be5d74f27b896f), gmpy2.mpz(0x80deb1fe3b1696b1), gmpy2.mpz(0x9bdc06a725c71235),
#          gmpy2.mpz(0xc19bf174cf692694), gmpy2.mpz(0xe49b69c19ef14ad2), gmpy2.mpz(0xefbe4786384f25e3), gmpy2.mpz(0x0fc19dc68b8cd5b5), gmpy2.mpz(0x240ca1cc77ac9c65),
#          gmpy2.mpz(0x2de92c6f592b0275), gmpy2.mpz(0x4a7484aa6ea6e483), gmpy2.mpz(0x5cb0a9dcbd41fbd4), gmpy2.mpz(0x76f988da831153b5), gmpy2.mpz(0x983e5152ee66dfab),
#          gmpy2.mpz(0xa831c66d2db43210), gmpy2.mpz(0xb00327c898fb213f), gmpy2.mpz(0xbf597fc7beef0ee4), gmpy2.mpz(0xc6e00bf33da88fc2), gmpy2.mpz(0xd5a79147930aa725),
#          gmpy2.mpz(0x06ca6351e003826f), gmpy2.mpz(0x142929670a0e6e70), gmpy2.mpz(0x27b70a8546d22ffc), gmpy2.mpz(0x2e1b21385c26c926), gmpy2.mpz(0x4d2c6dfc5ac42aed),
#          gmpy2.mpz(0x53380d139d95b3df), gmpy2.mpz(0x650a73548baf63de), gmpy2.mpz(0x766a0abb3c77b2a8), gmpy2.mpz(0x81c2c92e47edaee6), gmpy2.mpz(0x92722c851482353b),
#          gmpy2.mpz(0xa2bfe8a14cf10364), gmpy2.mpz(0xa81a664bbc423001), gmpy2.mpz(0xc24b8b70d0f89791), gmpy2.mpz(0xc76c51a30654be30), gmpy2.mpz(0xd192e819d6ef5218),
#          gmpy2.mpz(0xd69906245565a910), gmpy2.mpz(0xf40e35855771202a), gmpy2.mpz(0x106aa07032bbd1b8), gmpy2.mpz(0x19a4c116b8d2d0c8), gmpy2.mpz(0x1e376c085141ab53),
#          gmpy2.mpz(0x2748774cdf8eeb99), gmpy2.mpz(0x34b0bcb5e19b48a8), gmpy2.mpz(0x391c0cb3c5c95a63), gmpy2.mpz(0x4ed8aa4ae3418acb), gmpy2.mpz(0x5b9cca4f7763e373),
#          gmpy2.mpz(0x682e6ff3d6b2b8a3), gmpy2.mpz(0x748f82ee5defb2fc), gmpy2.mpz(0x78a5636f43172f60), gmpy2.mpz(0x84c87814a1f0ab72), gmpy2.mpz(0x8cc702081a6439ec),
#          gmpy2.mpz(0x90befffa23631e28), gmpy2.mpz(0xa4506cebde82bde9), gmpy2.mpz(0xbef9a3f7b2c67915), gmpy2.mpz(0xc67178f2e372532b), gmpy2.mpz(0xca273eceea26619c),
#          gmpy2.mpz(0xd186b8c721c0c207), gmpy2.mpz(0xeada7dd6cde0eb1e), gmpy2.mpz(0xf57d4f7fee6ed178), gmpy2.mpz(0x06f067aa72176fba), gmpy2.mpz(0x0a637dc5a2c898a6),
#          gmpy2.mpz(0x113f9804bef90dae), gmpy2.mpz(0x1b710b35131c471b), gmpy2.mpz(0x28db77f523047d84), gmpy2.mpz(0x32caab7b40c72493), gmpy2.mpz(0x3c9ebe0a15c9bebc),
#          gmpy2.mpz(0x431d67c49c100d4c), gmpy2.mpz(0x4cc5d4becb3e42b6), gmpy2.mpz(0x597f299cfc657e2a), gmpy2.mpz(0x5fcb6fab3ad6faec), gmpy2.mpz(0x6c44198c4a475817)]
#     data += b'\x80'
#     data = data + b'\x80'
#     while len(data) % 128 != 112:
#         data = data + b'\x00'
#     data = data + len(data).to_bytes(8, byteorder='big')
#     blocks = len(data) // 128
#     for i in range(blocks):
#         block = data[i*128:(i+1)*128]
#         w = []
#         for j in range(16):
#             w.append(gmpy2.mpz(int.from_bytes(block[j*8:(j+1)*8], byteorder='big')))
#         for j in range(16, 80):
#             s0 = gmpy2.mpz((gmpy2.bit_scan1(w[j-15]) - 31) % 32)
#             s1 = gmpy2.mpz((gmpy2.bit_scan1(w[j-2]) - 31) % 32)
#             w.append(gmpy2.mpz((w[j-16] + gmpy2.mpz(2)**s0 + w[j-7] + gmpy2.mpz(2)**s1) % gmpy2.mpz(2)**32))
#         a = h0
#         b = h1
#         c = h2
#         d = h3
#         e = h4
#         f = h5
#         g = h6
#         h = h7
#         for j in range(80):
#             s0 = gmpy2.mpz((gmpy2.bit_scan1(a) - 31) % 32)
#             s1 = gmpy2.mpz((gmpy2.bit_scan1(e) - 31) % 32)
#             ch = gmpy2.mpz((e & f) ^ ((~e) & g))
#             maj = gmpy2.mpz((a & b) ^ (a & c) ^ (b & c))
#             temp1 = gmpy2.mpz((h + gmpy2.mpz(2)**s1 + ch + k[j] + w[j]) % gmpy2.mpz(2)**32)
#             temp2 = gmpy2.mpz((gmpy2.mpz(2)**s0 + maj) % gmpy2.mpz(2)**32)
#             h = g
#             g = f
#             f = e
#             e = gmpy2.mpz((d + temp1) % gmpy2.mpz(2)**32)
#             d = c
#             c = b
#             b = a
#             a = gmpy2.mpz((temp1 + temp2) % gmpy2.mpz(2)**32)
#         h0 = gmpy2.mpz((h0 + a) % gmpy2.mpz(2)**32)
#         h1 = gmpy2.mpz((h1 + b) % gmpy2.mpz(2)**32)
#         h2 = gmpy2.mpz((h2 + c) % gmpy2.mpz(2)**32)
#         h3 = gmpy2.mpz((h3 + d) % gmpy2.mpz(2)**32)
#         h4 = gmpy2.mpz((h4 + e) % gmpy2.mpz(2)**32)
#         h5 = gmpy2.mpz((h5 + f) % gmpy2.mpz(2)**32)
#         h6 = gmpy2.mpz((h6 + g) % gmpy2.mpz(2)**32)
#         h7 = gmpy2.mpz((h7 + h) % gmpy2.mpz(2)**32)
#     return h0.to_bytes(4, byteorder='big') + h1.to_bytes(4, byteorder='big') + h2.to_bytes(4, byteorder='big') + h3.to_bytes(4, byteorder='big') + h4.to_bytes(4, byteorder='big') + h5.to_bytes(4, byteorder='big') + h6.to_bytes(4, byteorder='big') + h7.to_bytes(4, byteorder='big')


# data = "nguyen gia huy"
# sha256 = hashlib.sha256()
# sha256.update(data.encode())
# print("After hash using sha256 in library: ", sha256.hexdigest())
# print("After hash using sha256 my code: ", sha_256(data.encode()).hex())
# sha224 = hashlib.sha224()
# sha224.update(data.encode())
# print("After hash using sha224 in library: ", sha224.hexdigest())
# print("After hash using sha224 my code: ", sha_224(data.encode()).hex())
# sha384 = hashlib.sha384()
# sha384 = hashlib.sha384()
# print("After hash using sha384 in library: ", sha384.hexdigest())
# print("After hash using sha384 my code: ", sha_384(data.encode()).hex())

def encode(data, change):
   # print("hash using sha256 my code")
    if change == 224:
        return sha_224(data.encode()).hex()
    elif change == 256:
        return sha_256(data.encode()).hex()
    elif change == 384:
        sha384 = hashlib.sha384()
        sha384.update(data.encode())
        return sha384.hexdigest()
    elif change == 512:
        sha512 = hashlib.sha512()
        sha512.update(data.encode())
        return sha512.hexdigest()
    
