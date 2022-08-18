def HeapBottomUp(H):
    n = len(H) - 1  # The first element will be 0 and it will not be included
    strt = n // 2
    print("Beginning:", n, H)
    for i in range(strt, 0, -1):
        k = i
        v = H[k]
        heap = False

        while not heap and k * 2 <= n:
            j = 2 * k
            if j < n:  # there are 2 children
                if H[j] < H[j + 1]:
                    j = j + 1
            if v >= H[j]:
                heap = True
            else:

                H[k] = H[j]

                k = j

        H[k] = v
    return H


HA = [0, 2, 9, 7, 6, 5, 8]
print(HeapBottomUp(HA))

n = len(HA) - 1
print(HA[1])
i = 2
while i <= n:
    print(HA[i : i * 2])
    i *= 2

arr = [0, 12, 11, 13, 5, 6, 7]

print(HeapBottomUp(arr))

n = len(arr) - 1
print(arr[1])
i = 2
while i <= n:
    print(arr[i : i * 2])
    i *= 2
