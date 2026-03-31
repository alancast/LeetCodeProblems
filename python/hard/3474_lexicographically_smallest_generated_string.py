class Solution:
    # Handle all instances of T and check they all work
    # Time O(nm) if all T then go over full M every N
    # Space O(1) or n + m, just answer string
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        answer = ["a"] * (n + m - 1)
        fixed = [False] * (n + m - 1)

        # Process all cases of 'T'
        for i, ch in enumerate(str1):
            # Every time we see a T
            if ch == "T":
                # Make sure next m characters are the right characters from str2
                for j, c in enumerate(str2, i):
                    # If we have already set this char and it's wrong, return false
                    if fixed[j] and answer[j] != c:
                        return ""

                    # Set char and fixed (enumerate starts at i so this works)
                    answer[j] = c
                    fixed[j] = True

        # Process all cases of 'F' to make sure not accidental substring
        for i, ch in enumerate(str1):
            if ch == "F":
                # Check if there are already different characters in substring
                if any(str2[j - i] != answer[j] for j in range(i, i + m)):
                    continue

                # If not, find the last modifiable position and change it
                for j in range(i + m - 1, i - 1, -1):
                    if not fixed[j]:
                        answer[j] = "b"
                        break
                # Rarely used for-else block. What happens here is the else only
                # Is triggered if the loop finishes without a "break"
                # If broken, the else doesn't execute
                else:
                    return ""

        return "".join(answer)

test_cases = [
    ["bbbaaa", "TTFFF", "bb"],
    ["awvxyy", "FT", "wvxyy"],
    ["ababa", "TFTF", "ab"],
    ["", "TFTF", "abc"],
    ["a", "F", "d"]
]
solution = Solution()
for expected, str1, str2 in test_cases:
    actual = solution.generateString(str1, str2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: str1: {str1}, k: {str2}")

print("Ran all tests")
