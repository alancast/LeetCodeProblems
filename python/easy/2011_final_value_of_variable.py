class Solution:
    # Just go over all things in operations list
    # Time O(n)
    # Space O(1)
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        answer = 0
        for op in operations:
            if op[1] == '-':
                answer -= 1
            else:
                answer += 1

        return answer

test_cases = [
    [1, ["--X","X++","X++"]],
    [3, ["++X","++X","X++"]],
    [0, ["X++","++X","--X","X--"]]
]
solution = Solution()
for expected, operations in test_cases:
    actual = solution.finalValueAfterOperations(operations)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: operations: {operations}")

print("Ran all tests")
