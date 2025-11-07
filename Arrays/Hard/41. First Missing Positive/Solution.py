class Solution:

    #solution using input array as memory
    def firstMissingPositive(self, nums: List[int]) -> int:

        #first iteration gets rid of negative numbers
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=0

        #second iteration marks negative index in the input array to identify what numbers appeared
        for i in range (len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if  nums[val -1]>0:
                    nums[val-1] = -1*nums[val-1]
                elif nums[val-1] == 0:
                    nums[val-1] = -1*(len(nums)+1)

        #third iteration verify the first missing positive
        for i in range (1, len(nums)+1, +1):
            if nums[i-1] >= 0:
                return i
        return len(nums)+1