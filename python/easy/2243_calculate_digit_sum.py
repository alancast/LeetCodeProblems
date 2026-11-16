class Solution:
    # Keep reducing the string until each section is at most k digits long
    # Time O(n)
    # Space O(n)
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            tmp = []  # The digits from the next round after summing each chunk
            n = len(s)
            for i in range(0, n, k):
                val = 0
                for j in range(i, min(i + k, n)):
                    val += int(s[j])
                tmp.append(str(val))
            s = "".join(tmp)
        return s

test_cases = [
    ["135", "11111222223", 3],
    ["000", "00000000", 3],
]
solution = Solution()
for expected, s, k in test_cases:
    actual = solution.digitSum(s, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}, k: {k}")

print("Ran all tests")
