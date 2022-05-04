
"""
Given an array of integers, return indices of the 
two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def numbers(nums, num_search):
    for each_number in nums:
        for other_number in nums:
            if (each_number+other_number) == num_search:
                winner = set([nums.index(each_number), nums.index(other_number)])
    return list(winner)






print(numbers([11, 2, 7, 3, 4, 5, 6, 7, 1, 2, 15, 54, 23, 44, 92], 22))



