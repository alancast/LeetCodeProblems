class Solution:
    # This is a stupid elon musk type joke question
    # Just go over the num from start to end, change the first 6 to a 9
    # Time O(n)
    # Space O(n)
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        changed = False
        answer = []
        for char in str_num:
            # Can break out of this earlier but this question is not worth the time
            if changed:
                answer.append(char)
                continue

            # Make the first 6 a 9
            if char == '6':
                answer.append('9')
                changed = True
            else:
                answer.append(char)

        return int(''.join(answer))

test_cases = [
    [9969, 9669],
    [9999, 9996],
    [9999, 9999]
]
solution = Solution()
for expected, num in test_cases:
    actual = solution.maximum69Number(num)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: num: {num}")

print("Ran all tests")