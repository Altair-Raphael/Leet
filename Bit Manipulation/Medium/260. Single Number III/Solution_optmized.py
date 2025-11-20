class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all elements to eliminate duplicates.
        # The result 'xor' represents (a ^ b), where 'a' and 'b' are the unique numbers.
        # Any bit set to 1 in 'xor' means 'a' and 'b' have different bits at that position.
        xor = 0
        xor = 0

        for n  in nums: 
            xor ^= n


        # Step 2: Find a "separator" bit (mask).
        # We need to find any bit that is 1 in 'xor'.
        # We start checking from the least significant bit (1) and shift left (<<)
        # until we find a bit that is set in 'xor'.
        mask = 1

        while not (xor & mask): 
            mask = mask << 1

        # Step 3: Partition the numbers into two groups and recover the unique numbers.
        # We split the array based on the 'mask' bit.
        # - Group A: Numbers where the mask bit is 1.
        # - Group B: Numbers where the mask bit is 0.
        # Since 'a' and 'b' differ at this bit, they will end up in different groups.
        x, y = 0, 0
        for n in nums:
            if mask & n:
                x = x^n # XORing the first group retrieves the first unique number
            else:
                y = y^n # XORing the second group retrieves the second unique number
        return [x,y]
