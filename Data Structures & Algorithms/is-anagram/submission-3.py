class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # [S]: a string
        # [T]: a string
        
        # [1] — Get unique characters
        # [2] — Iterate [1] as [C]
            # [1] — Count [C] in [S], [T]
        if len(s) != len(t):
            return False
        sort_s = sorted(s)
        sort_t = sorted(t)

        zipped = zip(sort_s, sort_t)
        for (ss, tt) in zipped:
            if ss != tt:
                return False
        return True


                