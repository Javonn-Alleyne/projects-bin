import random

co_ords = []
beg,end = -45000,45000

for i in range (1000):
    x = random.randint(beg,end)
    while x == 0:
        x = random.randint(beg,end)

    y = random.randint(beg,end)
    while y == 0:
        y = random.randint(beg,end)

    z = random.randint(beg,end)
    while z == 0:
        z = random.randint(beg,end)

    # co_ords.append([x, y, z])
    print(x, y, z)

