class Solution:
    # Go over string once and keep count of streaks
    # Time O(n)
    # Space O(1)
    def countBinarySubstrings(self, s: str) -> int:
        curr_char = "c"
        curr_char_count = last_char_count = 0

        # Go over every char
        answer = 0
        for char in s:
            if char == curr_char:
                curr_char_count += 1
                continue

            # New char
            answer += min(curr_char_count, last_char_count)
            last_char_count = curr_char_count
            curr_char_count = 1
            curr_char = char

        # Make sure to count last ones
        answer += min(curr_char_count, last_char_count)
        return answer

test_cases = [
    [6, "00110011"],
    [4, "10101"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.countBinarySubstrings(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
