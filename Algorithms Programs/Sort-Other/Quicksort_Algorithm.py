def quicksort(A, l, r):
    if l <= r:
        s = partition(A, l, r)

        quicksort(A, l, s - 1)
        quicksort(A, s + 1, r)


def partition(A, l, r):
    p = A[l]
    i = l + 1
    j = r
    flag = True

    while flag:
        while i <= j and A[i] <= p:
            i += 1
        while j >= i and A[j] >= p:
            j -= 1
        if i >= j:
            flag = False
        else:
            A[i], A[j] = A[j], A[i]
    if p > A[j]:
        A[l], A[j] = A[j], A[l]

    return j


A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 85, 90, 543]

quicksort(A, 0, len(A) - 1)

print(A)

A = [5, 2, 7, 3, 9, 1, 4, 8]

quicksort(A, 0, len(A) - 1)

print(A)

A = [9, 2, 5, 7, 1, 4, 36, 87, 14, 78, 90]

quicksort(A, 0, len(A) - 1)

print(A)

A = [10, 15, 3, 55, 42, 2, 36, 25, 1]

quicksort(A, 0, len(A) - 1)

print(A)
