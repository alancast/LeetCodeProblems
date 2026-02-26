class Solution:
    # Go over string once from back to front
    # Time O(n)
    # Space O(1)
    def numSteps(self, s: str) -> int:
        N = len(s)

        operations = 0
        # Never reset carry to 0 because once it's carried once it will always be
        carry = 0
        # Go from end of string to front (smallest bit to biggest)
        for i in range(N - 1, 0, -1):
            # Make sure to take into account the carry of added ones
            digit = int(s[i]) + carry

            # If odd we add one then divide by 2 (so 2 ops)
            if digit % 2 == 1:
                operations += 2
                carry = 1
            # If even we just divide by 2
            else:
                operations += 1

        # Add carry one last time because might have needed to
        return operations + carry

test_cases = [
    [1, "10"],
    [0, "1"],
    [6, "1101"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.numSteps(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
