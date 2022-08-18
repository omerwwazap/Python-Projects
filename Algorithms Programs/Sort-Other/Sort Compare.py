# Compare Sorts
# selection_sort
# insertionSort
# bubblesort
# short_bubble_sort
# quickSort
# mergeSort
#

import random
import time


def selection_sort(a_list):
    for i in range(len(a_list) - 1, 0, -1):
        max_pos = 0
        for location in range(1, i + 1):
            if a_list[location] > a_list[max_pos]:
                max_pos = location
        a_list[i], a_list[max_pos] = a_list[max_pos], a_list[i]
    return a_list


def insertionSort(a):
    for i in range(len(a)):
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = v
    return a


def bubblesort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def short_bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
        pass_num = pass_num - 1
    return a_list


def quickSort(A, l, r):
    if l < r:
        splitpoint = partition(A, l, r)
        quickSort(A, l, splitpoint - 1)
        quickSort(A, splitpoint + 1, r)


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


def mergeSort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        M = arr[:middle]
        L = arr[middle:]
        mergeSort(M)
        mergeSort(L)
        merge(arr, M, L)


def merge(arr, M, L):
    i = j = k = 0
    while i < len(M) and j < len(L):
        if M[i] < L[j]:
            arr[k] = M[i]
            i += 1
        else:
            arr[k] = L[j]
            j += 1
        k += 1
    while i < len(M):
        arr[k] = M[i]
        i += 1
        k += 1
    while j < len(L):
        arr[k] = L[j]
        j += 1
        k += 1


a = []

for j in range(10000):
    a.append(random.randrange(0, 1000))

start_time = time.time()

a = insertionSort(a)

end_time = time.time() - start_time

print("insertion", end_time)

a = []
for j in range(10000):
    a.append(random.randrange(0, 1000))


start_time = time.time()

a = short_bubble_sort(a)

end_time = time.time() - start_time

print("Short-bubble", end_time)

a = []
for j in range(10000):
    a.append(random.randrange(0, 1000))


start_time = time.time()

a = bubblesort(a)

end_time = time.time() - start_time

print("bubble", end_time)


a = []
for j in range(10000):
    a.append(random.randrange(0, 1000))

start_time = time.time()

a = selection_sort(a)

end_time = time.time() - start_time

print("Selection", end_time)

a = []

for j in range(10000):
    a.append(random.randrange(0, 1000))

start_time = time.time()

quickSort(a, 0, len(a) - 1)

end_time = time.time() - start_time

print("quick", end_time)

a = []

for j in range(10000):
    a.append(random.randrange(0, 1000))

start_time = time.time()

mergeSort(a)

end_time = time.time() - start_time

print("merge", end_time)
