class Solution:
    # Just do the math
    # Time O(n)
    # Space O(1)
    def reverseDegree(self, s: str) -> int:
        answer = 0

        # Go over chars and do the math (start at index "1")
        for i, char in enumerate(s, start=1):
            answer += (26 - (ord(char) - ord("a"))) * i

        return answer

test_cases = [
    [148, "abc"],
    [160, "zaza"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.reverseDegree(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
