from collections import Counter


class Solution:
    # Math stuff where you map each set of a, and b chars to 00, 01, 10, 11
    # Where 0 represents even count and 1 represents odd, so we only care about 10
    # Go over all char sets ab and for each one use two pointers for count
    # Time O(n * e^2) where e is the char set
    # Space O(1)
    def maxDifference(self, s: str, k: int) -> int:
        # Map count_a cound_b to either 00, 01, 10, 11
        # We only care about 10
        def getStatus(cnt_a: int, cnt_b: int) -> int:
            return ((cnt_a & 1) << 1) | (cnt_b & 1)

        n = len(s)
        ans = float("-inf")
        # Enumerate all ab pairs
        for a in ["0", "1", "2", "3", "4"]:
            for b in ["0", "1", "2", "3", "4"]:
                # Skip if a and b are same as that's not a valid solution
                if a == b:
                    continue

                best = [float("inf")] * 4
                cnt_a = cnt_b = 0
                prev_a = prev_b = 0
                left = -1
                # Move right pointer forward
                for right in range(n):
                    cnt_a += s[right] == a
                    cnt_b += s[right] == b
                    # Make sure substring is greater than k and are at least 2 b's in str
                    while right - left >= k and cnt_b - prev_b >= 2:
                        left_status = getStatus(prev_a, prev_b)
                        best[left_status] = min(best[left_status], prev_a - prev_b)
                        left += 1
                        prev_a += s[left] == a
                        prev_b += s[left] == b

                    right_status = getStatus(cnt_a, cnt_b)
                    if best[right_status ^ 0b10] != float("inf"):
                        ans = max(ans, cnt_a - cnt_b - best[right_status ^ 0b10])

        return ans

test_cases = [
    [-1, "12233", 4],
    [1, "1122211", 3],
    [-1, "110", 3]
]
solution = Solution()
for expected, s, k in test_cases:
    actual = solution.maxDifference(s, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}, k: {k}")

print("Ran all tests")