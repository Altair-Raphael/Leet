class Solution:
    def twoSum(self, nums: list[int], target: int):
        size = len(nums)
        # brute force solution
        for i in range(size):
            for j in range(i+1, size):
                if nums[i]+nums[j]==target:
                    return [i,j] 