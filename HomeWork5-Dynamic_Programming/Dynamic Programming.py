
def minimumTotal(A):
    n = len(A)
    minimums = A[n - 1]
    
    for row in reversed(range(n - 1)):
        for col, value in enumerate(A[row]):
            minimums[col] = min(minimums[col], minimums[col + 1]) + value
    
    return minimums[0]


# Driver Code 
A = [[ 2 ], 
    [3, 9 ], 
    [1, 6, 7 ]] 
print(minimumTotal(A))

B = [[2],
    [5, 4],
    [1, 4, 7],
    [8, 6, 9, 6]]
print(minimumTotal(B))

C = [[2],
    [5, 4],
    [7, 4, 1],
    [8, 2, 9, 6],
    [11, 3, 8, 8, 6]]
print(minimumTotal(C))