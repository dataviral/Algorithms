def quicksort(arr, l, r):
    if l < r:
        k = partition(arr, l, r)
        quicksort(arr, l, k-1)
        quicksort(arr, k+1, r)

def partition(arr, l, r):
    x = arr[r]
    i = l-1
    j = l
    while j < r:
        if arr[j] <= x:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
        j += 1
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

arr = [9, 5, 8, 7, 4, 2, 6, 11, 21, 13, 19, 12]

print("Before Sorting  : ", *arr, sep = " ")
quicksort(arr, 0, len(arr)-1)
print("After Sorting   : ", *arr, sep = " ")
