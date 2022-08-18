a = [32, 5, 6, 1, 4, 7]
b = [32, 5, 6, 1, 4, 7]


for i in range(len(a) - 2):
    for j in range(len(a) - i - 2):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)


for i in range(len(b) - 2):
    for j in range(len(b) - i - 2):
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]

print(b)
