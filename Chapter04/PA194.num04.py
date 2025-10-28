s = 0

for a in range(1, 101, 1):
    if a %2 != 0:
        s += a
    else:
        s -= a
print(s)