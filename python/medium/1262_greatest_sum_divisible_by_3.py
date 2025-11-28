from typing import List


class Solution:
    # Track the two smallest mod 1 and mod 2. Sum it all then remove whatever
    # Time O(n)
    # Space O(1)
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = 0
        
        # Track smallest 2 of mod1, mod2
        smallest_mod_1 = [float('inf'), float('inf')]
        smallest_mod_2 = [float('inf'), float('inf')]
        
        # Add all nums to total and populate the smallest arrays
        for num in nums:
            total += num
            remainder = num % 3
            
            # See if this is one of the two smallest mod 1s
            if remainder == 1:
                if num < smallest_mod_1[0]:
                    smallest_mod_1[1] = smallest_mod_1[0]
                    smallest_mod_1[0] = num
                elif num < smallest_mod_1[1]:
                    smallest_mod_1[1] = num
            # See if this is one of the two smallest mod 2s
            elif remainder == 2:
                if num < smallest_mod_2[0]:
                    smallest_mod_2[1] = smallest_mod_2[0]
                    smallest_mod_2[0] = num
                elif num < smallest_mod_2[1]:
                    smallest_mod_2[1] = num
        
        # Case 1: total divisible by 3, just return total
        if total % 3 == 0:
            return total
        
        # Case 2: need remove something 
        # either smallest mod 1 or two smallest mod 2
        if total % 3 == 1:
            mod_one = smallest_mod_1[0]
            mod_twos = smallest_mod_2[0] + smallest_mod_2[1]
            return total - min(mod_one, mod_twos) # type: ignore

        # Case 3: total %3 == 2 need remove something 
        # either smallest mod 2 or both mod 1s
        mod_two = smallest_mod_2[0]
        mod_ones = smallest_mod_1[0] + smallest_mod_1[1]
        return total - min(mod_two, mod_ones) # type: ignore

    # Dynamic programming of what's the max sum for a mod
    # Time O(n)
    # Space O(1)
    def maxSumDivThree_dp(self, nums: List[int]) -> int:
        # Max sum of mod == 0, 1, and 2
        f = [0, -float("inf"), -float("inf")]

        # Go over all nums and update ranges
        for num in nums:
            # Create temp array
            g = f[:]

            for i in range(3):
                g[(i + num % 3) % 3] = max(g[(i + num % 3) % 3], f[i] + num)

            # Update array
            f = g
        
        # Return max with no remainder
        return f[0]

    # Sort into arrays of remainder 1, and 2
    # Add in as many numbers as you can
    # All nums are positive so just keep all
    # Time O(nlogn) for sort
    # Space O(n)
    def maxSumDivThree_sort(self, nums: List[int]) -> int:
        # Create sorted arrays of remainder 0, 1, and 2
        rem_zero = [x for x in nums if x % 3 == 0]
        rem_one = sorted([x for x in nums if x % 3 == 1], reverse=True)
        rem_two = sorted([x for x in nums if x % 3 == 2], reverse=True)

        answer = 0
        len_one = len(rem_one)
        len_two = len(rem_two)

        # Choose all the elements, or all minus one, or all minus two
        for count_one in [len_one - 2, len_one - 1, len_one]:
            # Make sure there are this many elements in the array
            if count_one >= 0:
                # Choose all the elements, or all minus one, or all minus two
                for count_two in [len_two - 2, len_two - 1, len_two]:
                    # Make sure there are this many elements 
                    # And that this combo of rem_1 and rem_2 mods to 0
                    if count_two >= 0 and (count_one - count_two) % 3 == 0:
                        # See if this number combination is the max
                        answer = max(answer, sum(rem_one[:count_one]) + sum(rem_two[:count_two]))

        return answer + sum(rem_zero)

test_cases = [
    [18, [3,6,5,1,8]],
    [0, [4]],
    [12, [1,2,3,4,4]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.maxSumDivThree(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")