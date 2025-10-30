class Solution(object):

#solution by in-place modifying the list
    def moveZeroes(self, nums: List[int]):
        x=0
        for y in range(len(nums)):
            if nums[y]!=0:
                nums[x], nums[y] = nums[y], nums[x]
                x=x+1
        return nums