class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        #solution using XOR ^ operator
        n=0
        for num in nums:
            n = n ^ num
        return n