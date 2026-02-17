class Solution:
    # Time O(n) as we go through all digits
    # Space O(1)
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        digit_map = [0] * 10
        for digit in digits:
            digit_map[digit] += 1

        answer = []
        for first_digit in range(1,10,1):
            if digit_map[first_digit] == 0:
                continue

            for second_digit in range(0,10,1):
                if digit_map[second_digit] == 0:
                    continue

                # Don't have enough first and second digit
                if second_digit == first_digit and digit_map[second_digit] < 2:  # noqa: PLR2004
                    continue

                for third_digit in range(0,10,2):
                    if digit_map[third_digit] == 0:
                        continue

                    # Make sure enough digit perms
                    if (
                        (first_digit == third_digit and digit_map[third_digit] < 2) or  # noqa: PLR2004
                        (second_digit == third_digit and digit_map[third_digit] < 2) or  # noqa: PLR2004
                        (first_digit == third_digit and second_digit == third_digit and digit_map[third_digit] < 3)  # noqa: PLR2004
                    ):
                        continue

                    number = (100 * first_digit) + (10 * second_digit) + third_digit
                    answer.append(number)

        return answer

test_cases = [
    [[102,120,130,132,210,230,302,310,312,320], [2,1,3,0]],
    [[222,228,282,288,822,828,882], [2,2,8,8,2]],
    [[], [3,7,5]]
]
solution = Solution()
for expected, digits in test_cases:
    actual = solution.findEvenNumbers(digits)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: digits: {digits}")

print("Ran all tests")
