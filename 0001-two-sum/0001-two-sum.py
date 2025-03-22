class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}  # Create a dictionary to store numbers and their indices
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]  # Return the indices if complement is found
            num_map[num] = i  # Store the current number and its index

        return [] # return empty list if no solution is found.