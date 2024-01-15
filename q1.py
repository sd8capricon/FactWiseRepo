def removeDuplicates(nums):
    counter = 0
    if len(nums) == 0:
        return 0
    for i in range(1, len(nums)):
        if nums[i] != nums[counter]:
            counter += 1
            nums[counter] = nums[i]

    return counter + 1


arr = [0, 0, 1, 4, 4, 5, 5]
k = removeDuplicates(arr)
print(arr[0:k])
