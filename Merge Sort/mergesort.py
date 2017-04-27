from copy import deepcopy

def mergesort(arr):
    l = len(arr)
    if l > 1:
        b = deepcopy(arr[ : l//2])
        c = deepcopy(arr[ l//2 : ])
        mergesort(b)
        mergesort(c)
        return merge(b,c,arr)


def merge(b, c, a):
    i = j = k = 0;
    while i < len(b) and j < len(c):
        if b[i] < c[j] :
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
        k += 1

    if i == len(b):
        while j < len(c):
            a[k] = c[j]
            k += 1
            j += 1
    else:
        while i <len(b):
            a[k] = b[i]
            i += 1
            k += 1

arr = [4,3,5,2,9, 1]

mergesort(arr)
print(arr)
