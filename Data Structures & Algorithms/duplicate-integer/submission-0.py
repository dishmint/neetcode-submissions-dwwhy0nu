class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # unique = set(nums)
        # numbers = {num: 0 for num in unique}
        # for n in nums:
        #     numbers[n] += 1

        # print(numbers)
        
        # for key in numbers:
        #     if numbers[key] > 1:
        #         return True
        
        # return False

        # What I really want to do is:
        """
        Check if the number has been seen, if it hasn't is it in the rest of the array? Yes? then you're done.
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
            