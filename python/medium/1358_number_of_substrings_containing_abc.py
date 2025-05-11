class Solution:
    # Time O(n) as we just go over s once
    # Space O(1) as we keep a map which can only consist of 3 chars
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        newest_a = newest_b = newest_c = -1

        count = 0
        for i in range(n):
            char = s[i]
            if char == 'a':
                newest_a = i
            elif char == 'b':
                newest_b = i
            else:
                newest_c = i

            # Add all substrings that end here, have all the chars (so how far forward left can go)
            # If don't have all chars the min will be -1 so will add 0
            count += min(newest_a, newest_b, newest_c) + 1
    
        return count
    
test_cases = [
    [10, "abcabc"],
    [3, "aaacb"],
    [1, "abc"],
    [0, "aaaaaab"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.numberOfSubstrings(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")