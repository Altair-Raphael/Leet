class Solution:
    #solution using string and list methods
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        wordsfinal = " ".join(words)
        return wordsfinal