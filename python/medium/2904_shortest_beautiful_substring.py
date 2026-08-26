class Solution:
    # Sliding window where we keep count of 1's
    # Time O(n^2) because extracting substring is O(n) so worst case it's n^2 as we do that every time
    # Space O(n) substring
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # It's impossible to have k ones, so return empty string
        if s.count("1") < k:
            return ""

        # Move right side of sliding window to end
        answer = s
        left = count = 0
        for right, char in enumerate(s):
            # Add if there is a one
            count += int(char)

            # If we have too many ones or left is 0, move left forward
            while count > k or s[left] == "0":
                count -= int(s[left])
                left += 1

            # We have a beautiful substring so see if it's new answer
            if count == k:
                t = s[left : right + 1]
                # This is the new answer if it's shorter or lexicographically smaller
                if len(t) < len(answer) or (len(t) == len(answer) and t < answer):
                    answer = t

        return answer

test_cases = [
    ["11001", "100011001", 3],
    ["11", "1011", 2],
    ["", "000", 1]
]
solution = Solution()
for expected, s, k in test_cases:
    actual = solution.shortestBeautifulSubstring(s, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}, k: {k}")

print("Ran all tests")
