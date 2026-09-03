class Solution:
    # Just go over array once and if even and odd find min odd
    # Time O(n)
    # Space O(1)
    def uniformArray(self, nums1: list[int]) -> bool:
        min_num = 9999999
        hasOdd = False

        # Go over all nums and find min num and if there is an odd
        for num in nums1:
            min_num = min(min_num, num)

            # See if there is an odd
            if num & 1:
                hasOdd = True

        # If min num is odd this is possible, if it's even then must all be even
        if min_num & 1:
            return True

        return not hasOdd

test_cases = [
    [True, [1,4,7]],
    [False, [2,3]],
    [True, [4,6]]
]
solution = Solution()
for expected, nums1 in test_cases:
    actual = solution.uniformArray(nums1)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums1: {nums1}")

print("Ran all tests")
