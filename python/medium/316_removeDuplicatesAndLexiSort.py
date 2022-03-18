class Solution:
    def removeDuplicateLetters(self, s) -> int:
        stack = []
        in_stack = set()

        last_occurrence = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            # Add to stack if not already in there
            if c not in in_stack:
                # Pop from stack if current letter is less than top of stack
                # And what's on top of stack shows up again later
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    in_stack.remove(stack.pop())

                in_stack.add(c)
                stack.append(c)

        return ''.join(stack)

testCases = [
    ["bcabc", "abc"],
    ["cbacdcbc", "acdb"]
]
implementation = Solution()
for s, expected in testCases:
    answer = implementation.removeDuplicateLetters(s)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUT: {s}")