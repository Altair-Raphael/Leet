class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # create a bijective mapping between characters of s and t using two hashmaps
        mapST, mapTS = {}, {}

        
        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            # verify if the current pair violates the established bijection
            if ((c1 in mapST and mapST[c1] != c2) or
                (c2 in mapTS and mapTS[c2] != c1)):
                return False

            # register the bijection for the current characters
            mapST[c1] = c2
            mapTS[c2] = c1

        return True