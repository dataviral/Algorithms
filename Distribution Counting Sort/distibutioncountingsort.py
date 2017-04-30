nums = [8,4,2,5,8,4,2,6,1,0]

def countSort(nums):
    m = max(nums)
    l = len(nums)
    d = [0] * (m+1)
    s = [0] * l
    for i in range(l):
        d[ nums[i] ] += 1
    for i in range(1, m+1) :
        d[i] = d[i-1] + d[i]
    for i in reversed(range(0, l)):
        j = nums[i]
        s[d[j]-1] = nums[i]
        d[j] -= 1
    return s

s = countSort(nums)

print(s)
