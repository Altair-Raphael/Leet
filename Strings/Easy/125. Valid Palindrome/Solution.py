class Solution:
    def isPalindrome(self, s: str) -> bool:

        #clean the string
        s_lower = s.lower()
        s_clean = "".join(char for char in s_lower if char.isalnum())

        #palindrome verification
        l = 0
        r = len(s_clean) - 1

        while r > l:
            if s_clean[l] != s_clean[r]:
                return False
            l += 1
            r -= 1

        return True


