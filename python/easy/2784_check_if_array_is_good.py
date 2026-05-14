class Solution:
    # Go over array once and see what number are in there
    # Make sure the only one that's twice is the max
    # The code here is more complicated to make sure we only go over list once
    # Can be much simpler if going over list twice
    # Time O(n)
    # Space O(n)
    def isGood(self, nums: list[int]) -> bool:
        seen_nums = set()
        counted_twice = -1
        arr_len = 0
        max_num = -1

        for num in nums:
            if num in seen_nums:
                # If we already have seen a num twice we know array isn't good
                if counted_twice != -1:
                    return False

                # If we have already seen a num bigger than this we know it's not good
                if max_num > num:
                    return False

                # See which one was counted twice, make sure it's the max
                counted_twice = num

            # See if num is greater than the one counted twice (bad)
            if counted_twice != -1 and num > counted_twice:
                return False

            # Update values for next one
            seen_nums.add(num)
            max_num = max(num, max_num)
            arr_len += 1

        # If the one that was counted twice was the max then true, otherwise false
        return arr_len == counted_twice + 1

test_cases = [
    [False, [2,1,3]],
    [True, [1,3,3,2]],
    [True, [1,1]],
    [False, [3,4,4,1,2,1]],
    [False, [14,2,2]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.isGood(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
