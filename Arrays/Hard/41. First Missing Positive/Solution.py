class Solution:
    #solution using input array as memory
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=0
        
        for i in range (len(nums)):
            if 1 <= nums[i] <= len(nums):
                val = abs(nums[i])

                if  nums[val -1]>0:
                    nums[val-1] = -1*nums[val-1]
                elif nums[val-1] == 0:
                    nums[val-1] = -1*(len(nums)+1)

        