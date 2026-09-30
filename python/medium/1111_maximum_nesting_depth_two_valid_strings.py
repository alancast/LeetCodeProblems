class Solution:
    # Just go over string once and keep depth counter
    # Time O(n)
    # Space O(1)
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        answer = []

        # Go over each char and compute depth
        depth = 0
        for char in seq:
            if char == "(":
                depth += 1
                answer.append(depth % 2)
            elif char == ")":
                answer.append(depth % 2)
                depth -= 1

        return answer

test_cases = [
    [[1,0,0,0,0,1], "(()())"],
    [[1,0,1,1,0,0,0,1], "((())())"],
    [[1,1,1,0,0,1,1,1], "()(())()"]
]
solution = Solution()
for expected, seq in test_cases:
    actual = solution.maxDepthAfterSplit(seq)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: seq: {seq}")

print("Ran all tests")
