class Solution:
    # Just go over the string once and keep track of counts
    # Time O(n)
    # Space O(1)
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        min_adds_required = 0

        # Go over each char in string and update counts
        for char in s:
            if char == "(":
                open_brackets += 1
            elif open_brackets > 0:
                open_brackets -= 1
            else:
                min_adds_required += 1

        # Add the remaining open brackets as closing brackets would be required.
        return min_adds_required + open_brackets

test_cases = [
    [1, "())"],
    [3, "((("]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.minAddToMakeValid(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
