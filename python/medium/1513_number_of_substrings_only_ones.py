class Solution:
    MOD = 10**9 + 7

    # Just math of all times we see a string of ones how many substrings
    # Go over string once and every time we see a 1 add substrings
    # Time O(n)
    # Space O(1)
    def numSub(self, s: str) -> int:
        answer = 0
        last_zero_idx = -1
        for i, char in enumerate(s):
            if char == "0":
                last_zero_idx = i
            else:
                answer += i - last_zero_idx
                answer %= self.MOD

        return answer

test_cases = [
    [9, "0110111"],
    [2, "101"],
    [21, "111111"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.numSub(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")