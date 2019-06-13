def HeapTopDown(H, item, index):
    H.append(item)
    
    i=index
    while i!=1 and i//2 >= 1: 
    
        heapify(H,index,i//2)
        i=i//2

    


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
array=[2,9,7,6,5,8] #Just the numbers to be inserted
HA =[0]  #array for heap - the first index will not be used
n=1     #array will be filled starting from index 1

for i in range (len(array)):
    HeapTopDown(HA, array[i],n)
    n=n+1

print(HA)

n=len(HA)-1
print(HA[1])
i=2
while (i <= n):
    print(HA[i:i*2] )
    i*=2

arr = [ 0, 12, 11, 13, 5, 6, 7] 

