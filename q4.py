def searchNinsert(nums, target):
    i = 0
    j = len(nums) - 1

    while i <= j:
        mid = i + (j - i) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            i = mid + 1
        else:
            j = mid - 1


nums = [1, 3, 5, 6]
target = 5
print(searchNinsert(nums, target))
