class Solution:
    def countBits(self, n: int) -> List[int]:

# O(n) Dynamic Programming solution using Bit Manipulation

        ans = [0] * (n+1)

        for i in range (1, n+1):
            ans[i] = ans[i>>1] + (i&1)

        return ans