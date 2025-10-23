class Solution:
    # Just do the computations
    # Could do with O(1) space with editing in place
    # Time O(n^2)
    # Space O(n)
    def hasSameDigits(self, s: str) -> bool:
        digits = []
        for char in s:
            digits.append(int(char))
        
        # Keep processing until there are only 2 digits left
        while len(digits) > 2:
            temp_digits = []
            for i in range(len(digits) - 1):
                next = digits[i] + digits[i+1]
                temp_digits.append(next%10)

            digits = temp_digits

        return digits[0] == digits[1]

test_cases = [
    [True, "3902"],
    [False, "34789"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.hasSameDigits(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")