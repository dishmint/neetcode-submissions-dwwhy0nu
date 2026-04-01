class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # TODO: algo doesn't work for empty strings
        # [^] need to keep track of indices, that way an empty string at 0 is considered different than an empty string at 1
        # [V]: seen indices
        seen_indices = set()
        # [R]: result array
        res = []
        # [1] — for each string in strs
        for i, s in enumerate(strs):
            # [?] — index in [V]
            if i in seen_indices:
                # [T] — go to next loop iter
                continue
            
            # [2] — Init anagram set with string `s`
            sub_gen = [s]
            # [3] — Add the `s`'s index to [V]
            seen_indices.add(i)
            
            # [4] — sort the characters of s
            s_sorted = sorted(s)
            # [5] — compare to the rest of the strings
            for j in range(i + 1, len(strs)):
                # [1] — st is string at `j`
                st = strs[j]
                # [2] — if the index hasn't been visited, the strings are equal length, and the sort of their chars is the same
                if j not in seen_indices and len(s) == len(st) and s_sorted == sorted(st):
                    # [1] — append `st` (the anagram) to sub_gen
                    sub_gen.append(st)
                    # [2] — mark index `j` as seen
                    seen_indices.add(j)
            # [6] — Append anagram set to result list
            res.append(sub_gen)
        # [>] return results list
        return res