def insertion_sort(nums):
    l = len(nums)
    for i in range(1, l):
        j = i-1
        curr = nums[i]
        while j >= 0 and nums[j] > curr :
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = curr

nums = [4,5,2,4,1,1,9,6]

insertion_sort(nums)
print(nums)
