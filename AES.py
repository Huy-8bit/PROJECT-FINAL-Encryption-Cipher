# AES encryption

def add_round_key(state, round_key):
    for i in range(4):
        for j in range(4):
            state[i][j] ^= round_key[i * 4 + j]




def main():
    print("select key sizes: 128, 192, 256")
    key = 0
    while True:
        key = input("Enter key: ")
        if key == "128" or key == "192" or key == "256":
            break
    print("Key sizes: ", key)
    
main()