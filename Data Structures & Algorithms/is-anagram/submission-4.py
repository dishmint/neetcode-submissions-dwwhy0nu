class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # [1] — if s and t are different lengths they can't anagrammize
        if len(s) != len(t):
            return False
        # [2] — Sort the chars of s and t
        sort_s = sorted(s)
        sort_t = sorted(t)

        # [3] — zip the strings
        zipped = zip(sort_s, sort_t)
        
        # [4] — if any pairing is a mismatch, no anagram
        for (ss, tt) in zipped:
            if ss != tt:
                return False
        return True


                