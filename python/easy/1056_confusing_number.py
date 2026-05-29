class Solution:
    # Build inverted number and see if they are equal
    # Time O(logn)
    # Space O(logn)
    def confusingNumber(self, n: int) -> bool:
        # What each char maps to when rotated
        invert_map = {0:0, 1:1, 8:8, 6:9, 9:6}
        invert_number = 0
        n_copy = n

        # Get every digit of 'n_copy' by taking the remainder of it to 10.
        while n_copy:
            remainder = n_copy % 10

            # Number is invalid to rotate
            if remainder not in invert_map:
                return False

            # Build inverted number and then shrink n_copy
            invert_number = (invert_number * 10) + invert_map[remainder]
            n_copy //= 10

        # If inverted number is same (e.g. 11) then not confusing, otherwise is
        return invert_number != n

test_cases = [
    [True, 6],
    [True, 89],
    [False, 11]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.confusingNumber(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")