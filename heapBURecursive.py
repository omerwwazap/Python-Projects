def HeapBottomUp(H):
    n=len(H)-1  # The first element will be 0 and it will not be included 
    strt=n//2
    print("Beginning:",n,H)
    for i in range (strt, 0,-1):
        heapify(H,n,i)

    return H


# To heapify subtree rooted at index i. n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i      # left = 2*i 
    r = 2 * i+1     # right = 2*i + 1
     # See if left child of root exists and is greater than root
    if l <= n and arr[i] < arr[l]:
        largest = l
     # See if right child of root exists and is greater than root
    if r <= n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)

#main part
HA=[0,2,9,7,6,5,8]
print(HeapBottomUp(HA))

n=len(HA)-1
print(HA[1])
i=2
while (i <= n):
    print(HA[i:i*2] )
    i*=2

arr = [ 0, 12, 11, 13, 5, 6, 7] 

