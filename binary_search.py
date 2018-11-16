#!/usr/bin/env python3
def binary_search(A, value, low, high):
    if high < low:
        return False

    mid = int((low + high) / 2)

    if A[mid] > value:
        return binary_search(A, value, low, mid-1)
    elif A[mid] < value:
        return binary_search(A, value, mid+1, high)
    else:
        return mid


with open("list.txt", "r") as f:
    L = [int(x) for x in f]

print(f"Index = {binary_search(L, 50, 0, 4999)}") # Finnes i lista
print(f"Index = {binary_search(L, 320, 0, 4999)}") # Ikke i lista
