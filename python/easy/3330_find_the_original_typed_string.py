class Solution:
    # Time O(n) as we go over the string once
    # Space O(1)
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        last_char = word[0]
        double_count = 0

        for i in range(1, n):
            char = word[i]
            if char == last_char:
                double_count += 1

            last_char = char

        return double_count + 1
    
test_cases = [
    [5, "abbcccc"],
    [1, "abcd"],
    [4, "aaaa"]
]
solution = Solution()
for expected, word in test_cases:
    actual = solution.possibleStringCount(word)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: word: {word}")

print("Ran all tests")