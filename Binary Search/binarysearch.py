def binarysearch(arr, l, r , k):
    if l < r:
        m = (l+r)//2
        if k == arr[m]: return m
        if k < arr[m]:  return binarysearch(arr, l, m-1, k)
        if k > arr[m]: return binarysearch(arr, m+1, r, k)
    return -1

arr = [1,2,3,4,8,12,32,44]

ind = binarysearch(arr, 0, len(arr), 44)
print(ind)
