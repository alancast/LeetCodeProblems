class Solution:
    # Precompute first and last index of each char
    # Then go over all chars and compute how many strings can be made
    # Time O(n)
    # Space O(1) (O(26))
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26
        
        # Go over string and compute first and last of each index
        for i in range(len(s)):
            curr = ord(s[i]) - ord("a")
            # Only set first if not done
            if first[curr] == -1:
                first[curr] = i
            
            # Always set last
            last[curr] = i
        
        # Go over all alphabet and see how many palindromes can be made
        answer = 0
        for i in range(26):
            # Make sure this char can be a palindrome
            if first[i] == -1 or last[i] == first[i]:
                continue
                
            # Create a set of all chars between first and last (set because must be unique)
            between = set()
            for j in range(first[i] + 1, last[i]):
                between.add(s[j])
            
            answer += len(between)

        return answer

test_cases = [
    [3, "aabca"],
    [0, "adc"],
    [4, "bbcbaba"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.countPalindromicSubsequence(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")