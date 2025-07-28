from functools import cache
from typing import List


class Solution:
    # Recursive and memoized implementation. 
    # Pretty similar to brute force but slight optimizations
    # Time O(2^n)
    # Space O(n) for recursive callstack
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)

        # Calculate the maximum possible OR value
        max_or_value = 0
        for num in nums:
            max_or_value |= num

        # Recursive see if subset is max or not
        @cache
        def recur(cur_or, i):
            # Base case: Reached end and not right number
            if i == n and cur_or != max_or_value:
                return 0
            
            # Base case: Reached max, so all possible subsets after this valid
            if cur_or == max_or_value:
                return 2 ** (n-i)
            
            cnt = 0
            # Include num
            cnt += recur(cur_or|nums[i], i+1)
            # Don't include num
            cnt += recur(cur_or, i +1)

            return cnt
        
        answer = recur(0, 0)
        return answer

    # Memory efficient implementation but slow
    # Finds max or value and then does bitwise manipulation to count subsets that equal it
    # Time O(n * 2^n) as there are 2^n possible subsets and we go through full computation on all
    # Space O(1)
    def countMaxOrSubsets_space_efficient(self, nums: List[int]) -> int:
        # Calculate the maximum possible OR value
        max_or_value = 0
        for num in nums:
            max_or_value |= num

        total_subsets = 1 << len(nums)  # 2^n subsets
        subsets_with_max_or = 0

        # Iterate through all possible subsets
        # 2^n here represents numbers 101 means first and 3rd included in subset
        # So we go over all possible subsets going from 0 to 2^n
        for subset_mask in range(total_subsets):
            current_or_value = 0

            # Calculate OR value for the current subset
            for i in range(len(nums)):
                if (subset_mask >> i) & 1:
                    current_or_value |= nums[i]

            # If current subset's OR equals max_or_value, increment count
            if current_or_value == max_or_value:
                subsets_with_max_or += 1

        return subsets_with_max_or

    # Same approach as brute force below but memo if we have already completed
    # A subset problem to prune recursing down that path
    # Time O(n*maxvalue) as there are at most n*maxvalue entries in memo array and O(1)
    # Space O(n*maxvalue)
    def countMaxOrSubsets_memo(self, nums: List[int]) -> int:
        # Find Max value by or-ing full array
        max_or_value = 0
        n = len(nums)
        for num in nums:
            max_or_value |= num

        # Initialize memo with -1
        # Memo array is -1 for values (0,max) for all n indices in nums
        # It's filled with how many subsets possible if you get to that state
        memo = [[-1] * (max_or_value + 1) for _ in range(n)]

        return self._count_subsets_memo(nums, 0, 0, max_or_value, memo)

    def _count_subsets_memo(
        self,
        nums: List[int],
        index: int,
        current_or: int,
        target_or: int,
        memo: List[List[int]],
    ) -> int:
        # Base case: reached the end of the array
        if index == len(nums):
            return 1 if current_or == target_or else 0

        # Check if the result for this state is already memoized
        if memo[index][current_or] != -1:
            return memo[index][current_or]

        # Don't include the current number
        count_without = self._count_subsets_memo(
            nums, index + 1, current_or, target_or, memo
        )

        # Include the current number
        count_with = self._count_subsets_memo(
            nums, index + 1, current_or | nums[index], target_or, memo
        )

        # Memoize and return the result
        memo[index][current_or] = count_without + count_with
        return memo[index][current_or]

    # Recursive brute force simple. Find max value then go over all subsets
    # And see if they equal max value or not
    # Time O(2^n)
    # Space O(n) recursive call stack
    def countMaxOrSubsets_brute(self, nums: List[int]) -> int:
        # Find Max value by or-ing full array
        max_or_value = 0
        for num in nums:
            max_or_value |= num

        # Find how many subsets can add up to this
        return self._count_subsets(nums, 0, 0, max_or_value)

    def _count_subsets(
        self, nums: List[int], index: int, current_or: int, target_or: int
    ) -> int:
        # Base case: reached the end of the array
        if index == len(nums):
            return 1 if current_or == target_or else 0

        # Don't include the current number
        count_without = self._count_subsets(
            nums, index + 1, current_or, target_or
        )

        # Include the current number
        count_with = self._count_subsets(
            nums, index + 1, current_or | nums[index], target_or
        )

        # Return the sum of both cases
        return count_without + count_with

    
test_cases = [
    [2, [3,1]],
    [7, [2,2,2]],
    [6, [3,2,1,5]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.countMaxOrSubsets(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")