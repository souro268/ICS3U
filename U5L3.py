def swap(B, p, q):
    temp = B[p]
    B[p] = B[q]
    B[q] = temp

def sort(A): # A very inefficient sorting method!
    for i in range(len(A)):
        for j in range(len(A)):
            if (A[i] < A[j]):
                swap(A, i, j)

A = [4, -1, 7, 3, 9, 0, 11, 2, 14]
sort(A)
print(A)
