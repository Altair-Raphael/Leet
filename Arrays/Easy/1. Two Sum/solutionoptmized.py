class Solution:

#solution using a hashmap to search for a complementary number
    def twoSum(self, nums:list[int], target: int):
        map = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in map:
                return [map[comp], i]
            map[num] = i