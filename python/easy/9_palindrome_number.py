class Solution:
    # Negative numbers don't count because negative sign
    # Shrink number while also building up it's counterpart
    # Time O(logn)
    # Space O(1)
    def isPalindrome(self, x: int) -> bool:
        # Special cases:
        # When x < 0, x is not a palindrome cuz negative sign.
        # Also can't end with 0 unless number is 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Build up the reversed number until it's the same (or larger than front half)
        end_num = 0
        while x > end_num:
            end_num = end_num * 10 + x % 10
            x //= 10

        # When the length is an odd number, we can get rid of the middle digit by end_num//10
        # E.g if input is 12321, we get x = 12, end_num = 123
        return x == end_num or x == end_num // 10

test_cases = [
    [True, 121],
    [False, -121],
    [False, 10],
    [True, 0]
]
solution = Solution()
for expected, x in test_cases:
    actual = solution.isPalindrome(x)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: x: {x}")

print("Ran all tests")
