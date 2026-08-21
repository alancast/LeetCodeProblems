class Solution:
    # See if there is a middle and sort
    # Can optimize sort to O(n) using counting sort since alphabet is finite in size
    # Time O(n)
    # Space O(1) 26
    def smallestPalindrome(self, s: str) -> str:
        # Since s is a palindrome we get all the info we need just from first half
        partition = len(s) // 2

        # Find counts of each char
        char_counts = [0] * 26
        for i in range(partition):
            char_counts[ord(s[i]) - 97] += 1

        # Build sorted left half (already sorted by count nature)
        left = "".join(
            [chr(i + 97) * char_counts[i] for i in range(26) if char_counts[i] > 0]
        )

        # If odd number make sure we have same middle
        mid = s[partition] if len(s) % 2 != 0 else ""

        # Right must just be left reversed
        right = left[::-1]

        return left + mid + right

test_cases = [
    ["z", "z"],
    ["abbba", "babab"],
    ["acddca", "daccad"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.smallestPalindrome(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
