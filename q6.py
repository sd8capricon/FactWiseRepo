def circularRobber(nums):
    if len(nums) == 0:
        return 0
    prev_max = 0
    current_max = 0
    for num in nums:
        temp = current_max
        current_max = max(current_max, prev_max + num)
        prev_max = temp
    return current_max


nums = [1, 2, 3, 1]
print(circularRobber(nums))
