class Solution:
    # Just go over string once and count
    # Time O(n)
    # Space O(1)
    def maxDepth(self, s: str) -> int:
        depth = 0
        answer = 0

        # Go over each char and count parenthesis
        for char in s:
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1

            # See if we have a new max depth
            answer = max(answer, depth)

        return answer

test_cases = [
    [3, "(1+(2*3)+((8)/4))+1"],
    [3, "(1)+((2))+(((3)))"],
    [3, "()(())((()()))"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.maxDepth(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
