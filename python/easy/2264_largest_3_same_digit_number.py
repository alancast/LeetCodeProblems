class Solution:
    # Go over number and find all pairs of 3 and return biggest
    # Time O(n)
    # Space O(1)
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)

        answer_int = -1
        count = 1
        prev = num[0]

        for i in range(1, n):
            char = num[i]

            # This is a new char so can't be part of string of 3
            if char != prev:
                count = 1
                prev = char
                continue

            count += 1

            # Found a string of 3 so see if it's better
            if count == 3 and int(char) > answer_int:  # noqa: PLR2004
                answer_int = int(char)
                # Can't beat 999 so just return if we see that
                if answer_int == 9:  # noqa: PLR2004
                    return "999"

        # No string of 3 was found
        if answer_int == -1:
            return ""

        return str(answer_int) * 3

test_cases = [
    ["777", "6777133339"],
    ["000", "2300019"],
    ["", "2213"],
    ["", "42352338"]
]
solution = Solution()
for expected, num in test_cases:
    actual = solution.largestGoodInteger(num)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: num: {num}")

print("Ran all tests")
