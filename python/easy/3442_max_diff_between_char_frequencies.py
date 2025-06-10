from collections import Counter, defaultdict


class Solution:
    # Exact same logic as below but sped up by use of python defaults
    # Time O(n) as we go through each letter once (and then constant space search for array)
    # Space O(1) store at most 26 things (assuming english char set)
    def maxDifference(self, s: str) -> int:
        char_counts = Counter(s)

        # find min even and max odd
        max_odd = 0
        min_even = float('inf')
        for char in char_counts:
            if char_counts[char] % 2 != 0:
                max_odd = max(max_odd, char_counts[char])
            if char_counts[char] % 2 == 0:
                min_even = min(min_even, char_counts[char])

        return max_odd - min_even
    

    # Time O(n) as we go through each letter once (and then constant space search for array)
    # Space O(1) store at most 26 things (assuming english char set)
    def maxDifference_slower(self, s: str) -> int:
        char_counts = defaultdict(int)
        for char in s:
            char_counts[char] += 1

        # find min even and max odd
        max_odd = 0
        min_even = float('inf')
        for _, value in char_counts.items():
            if value % 2 == 0:
                if value < min_even:
                    min_even = value
            else:
                if value > max_odd:
                    max_odd = value

        return max_odd - min_even
    
test_cases = [
    [3, "aaaaabbc"],
    [1, "abcabcab"],
    [-3, "yzyyys"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.maxDifference(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")