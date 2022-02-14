def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    records = dict()

    for index, num in enumerate(nums):
        if target - num not in records:
            records[num] = index
        else:
            return [records[target - num], index]


# t_nums = [2, 7, 11, 15]
# t_target = 9

# t_nums = [3, 2, 4]
# t_target = 6

t_nums = [3, 3]
t_target = 6

print(two_sum(t_nums, t_target))
