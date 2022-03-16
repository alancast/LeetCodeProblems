from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        index = 0
        stack = []
        for entry in pushed:
            stack.append(entry)
            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1

        return len(stack) == 0

testCases = [
    [[1,2,3,4,5], [4,5,3,2,1], True],
    [[1,2,3,4,5], [4,3,5,1,2], False]
]
implementation = Solution()
for pushed, popped, expected in testCases:
    answer = implementation.validateStackSequences(pushed, popped)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUT: Pushed:{pushed}, Popped: {popped}")