class Solution:
    def clearDigits(self, s: str) -> str:
        return self.__clear_digits_in_place(s)

    # Time O(n) space O(1)
    def __clear_digits_in_place(self, s: str) -> str:
        answer_length = 0
        chars = list(s)

        for index in range(len(chars)):
            char = chars[index]
            if char.isalpha():
                chars[answer_length] = char
                answer_length += 1
            else:
                answer_length -= 1

        chars = chars[:answer_length]
        return "".join(chars)

    # Time O(n) space O(n)
    def __clear_digits_stack(self, s: str) -> str:
        final_string = []
        for char in s:
            if char.isalpha():
                final_string.append(char)
            else:
                final_string.pop()

        return "".join(final_string)

testCases = [
    ["a1b2c3", ""],
    ["ab12", ""],
    ["abc", "abc"],
    ["dab12c", "dc"]
]
solution = Solution()
for s, expected in testCases:
    answer = solution.clearDigits(s)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. Input {s}")

print("Ran all tests")
