from typing import List


class Solution:
    # Go over list once and see if two adjacent k size arrays
    # Time O(n)
    # Space O(1)
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        prev_num = float('-inf')
        count = 0
        looking_for_second = False

        # Go over array
        for num in nums:
            # This is strictly increasing from last
            if num > prev_num:
                count += 1

                # Do we have a second k size subarray
                if count == k and looking_for_second:
                    return True

                # We can just cut this in half and have two adjacent
                if count == 2*k:
                    return True
                    
            # We decreased in number, streak busted so start again
            else:
                if count >= k:
                    looking_for_second = True
                else:
                    looking_for_second = False

                count = 1

            prev_num = num

        # Check for if final number completed streak
        return count == k and looking_for_second

test_cases = [
    [True, [2,5,7,8,9,2,3,4,3,1], 3],
    [True, [19,5], 1],
    [False, [1,2,3,4,4,4,4,5,6,7], 5]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.hasIncreasingSubarrays(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")
