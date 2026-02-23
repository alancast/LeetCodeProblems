class Solution:
    # Sliding window over string and check set size
    # Time O(n)
    # Space O(2^k)
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        num_set = set()
        max_num = pow(2, k)

        for i in range(n - k + 1):
            # Convert the binary string to an int and add it
            num = int(s[i: (i + k)], 2)
            num_set.add(num)

            # See if we've gotten all combos, if so return true
            if len(num_set) == max_num:
                return True

        # We got through all strings and set wasn't big enough
        return False

test_cases = [
    [True, "00110110", 2],
    [True, "0110", 1],
    [True, "00110", 2],
    [False, "0110", 2]
]
solution = Solution()
for expected, s, k in test_cases:
    actual = solution.hasAllCodes(s, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}, k: {k}")

print("Ran all tests")
