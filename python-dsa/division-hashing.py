# h(x) = x mod M
# Division method to hash

size = 10
ht = []

def init():
    for i in range(size):
        ht.append(-1)

def hash(val):
    key = val % size
    if ht[key] == -1:
        ht[key] = val
    else:
        print("COLLISION !")


if __name__ == "__main__":
    init()
    hash(12)
    hash(11)
    hash(9)
    hash(19)
    print(ht)
