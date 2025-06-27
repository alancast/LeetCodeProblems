class Solution:
    # Time O(n) as we go over the string once with two pointers
    # Space O(1)
    def longestSubsequence(self, s: str, k: int) -> int:
        current_num = answer = subsequence_len = last_removed = 0

        # Loop over string and do calculations
        for index, char in enumerate(s):
            current_num *= 2
            current_num += int(char)
            subsequence_len += 1

            if current_num <= k:
                answer = max(answer, subsequence_len)
                continue

            # Remove leftmost 1s until below k
            while current_num > k:
                remove_char = s[last_removed]
                last_removed += 1

                # Subtract value if need be
                if remove_char == '1':
                    subsequence_len -= 1
                    current_num -= pow(2, index - last_removed + 1)

        return answer
    
test_cases = [
    [5, "1001010", 5],
    [6, "00101001", 1]
]
solution = Solution()
for expected, s, k in test_cases:
    actual = solution.longestSubsequence(s, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}, k: {k}")

print("Ran all tests")