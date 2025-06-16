class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSum = []
        for num in nums:
            if (len(runningSum) == 0):
                runningSum.append(num)
            else:
                runningSum.append(num + runningSum[-1]) # Access the last element
        return runningSum