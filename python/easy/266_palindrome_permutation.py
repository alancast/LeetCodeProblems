class Solution:
    # Time O(n) as we go through the string once
    # Space O(1) as we have a set with at most 26 entries
    def canPermutePalindrome(self, s: str) -> bool:
        # If we have an even length string all characters must appear an even number of times
        # If odd we must have one character show up an odd amount but that's it
        char_set = set()

        for char in s:
            if char in char_set:
                char_set.remove(char)
            else:
                char_set.add(char)

        # If odd len it has to be 1, if even len it must be 0 at least 2
        return len(char_set) <= 1
    
test_cases = [
    [False, "code"],
    [True, "aab"],
    [True, "carerac"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.canPermutePalindrome(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")