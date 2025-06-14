class Solution:
    # N is len of num
    # Time O(n) as we go through the full num once
    # Space O(n) as we store a copy of the num
    def minMaxDifference(self, num: int) -> int:
        max_str = str(num)
        min_str = str(num)

        n = len(max_str)
        pos = 0
        # Find the first non 9 to replace
        while pos < n and max_str[pos] == "9":
            pos += 1
        # If num is all 9's then it already is the max
        if pos < n:
            max_str = max_str.replace(max_str[pos], "9")

        # Swapping the first num to 0 will always guarantee min
        min_str = min_str.replace(min_str[0], "0")

        # Do the math
        return int(max_str) - int(min_str)
    
test_cases = [
    [99009, 11891],
    [99, 90]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minMaxDifference(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")