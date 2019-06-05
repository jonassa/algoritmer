def digit(n, i):
    return int(n/10**(i-1)) % 10

def counting_sort(A, k, D):
    n = len(A)
    B = [None] * n
    C = [0] * (k+1)
    for i,_ in enumerate(A):
        C[D[i]] += 1
    for j in range(1, k+1):
        C[j] = C[j] + C[j-1]
    for j in range(n-1, -1, -1):
        import pdb; pdb.set_trace()
        B[C[D[j]]] = A[j]
        C[D[j]] -= 1
    return B

def radix_sort(A, d):
    for i in range(1, d+1):
        D = [digit(e, i) for e in A]
        A = counting_sort(A, 9, D)

