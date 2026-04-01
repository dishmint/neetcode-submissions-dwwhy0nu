class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        **USED CLAUDE TO SUGGEST IMPROVEMENTS TO MY LAST SUBMISSION**
        The following is my own prose:
        Major point:
        Remove the inner loop to cut down on runtime
        In removing the inner loop, one needs to figure out how to check each element against the other strings.
        There's no way to do this, afaik, without nesting, so we can ctually solve this by abstracting the problem.

        We save the sorted list of characters for a given string as a key in a dictionary.
        So instead of keeping track of matches, we keep track of the 'character sets (in sort order)' that have been seen.
        Each sorted character set (SCS) is a key in the dict.
        If string n's SCS is a key in the dict, then we add it to that key's data.
        """
        # [1] — Setup anagram dict
        anagrams = {}
        # [2] — iterate over the strings in `strs`
        for s in strs:
            # [1] — create a hashable key for the angaram dict using the characters of `s`
            key = tuple(sorted(s))
            # [^] tuple is used because lists can't be keys; `s` is sorted so the anagram comparison can be made
            # [?] — if the key is not in the anagrams dict, it hasn't been seen (lso, since it's sorted it means neither has any of its anagrams)
            if key not in anagrams:
                # [T] — establish the empty anagram
                anagrams[key] = []
            # [2] — Add `s` to the list of anagrams containing the characters of `key`
            anagrams[key].append(s)
        # [>] list of the anagrams dict values: <list>[ [<av1>], [<av2>], [<av3>] ]
        return list(anagrams.values())