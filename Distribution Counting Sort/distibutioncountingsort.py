nums = [8,4,2,5,8,4,2,0,1]

def countSort(nums):
    d = [0] * max(nums)
    s = [0] * nums
    for i in range(len(nums)):
        d[nums[i] ] += 1
    for i in range(len(d)) :
        d[j] = d[j-1] + d[j]
    for i in reversed(range(0, len(nums))):
        j = nums[i]
        s[d[j]-1] = nums[i]
        d[j] -=1
    return s

countSort(nums)
