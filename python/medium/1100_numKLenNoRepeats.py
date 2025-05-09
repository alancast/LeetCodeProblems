from collections import Counter


class Solution:
    # Sliding window and set
    # Time O(n) as just go through string once
    # Space O(1) as make set of size k but 26 chars so O(26) so 1
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        char_set = set()
        n = len(s)
        left = right = count = 0

        while right < n:
            char = s[right]

            # if char is already in set move left forward until it's removed
            while char in char_set:
                left_char = s[left]
                char_set.remove(left_char)
                left += 1
            
            # Add char
            char_set.add(char)

            # Add onto count if this substring works
            if len(char_set) >= k:
                count += 1

            right += 1

        return count
    
    # Could be more optimized by moving the window boundaries
    # until the offending dupe is gone. But eh 🤷‍♂️ not doing it
    def numKLenSubstrNoRepeats_counter(self, s: str, k: int) -> int:
        if k > len(s):
            return 0

        count = 0
        chars = Counter(s[:k])
        for i in range(k, len(s)):
            if len(chars) == k:
                count += 1
            addingChar = s[i]
            removingChar = s[i-k]

            chars[removingChar] -= 1
            if chars[removingChar] == 0:
                del chars[removingChar]
            chars[addingChar] = chars.get(addingChar, 0) + 1

        # Check the final set to see if last k chars count
        if len(chars) == k:
            count += 1

        return count

testCases = [
    ["havefunonleetcode", 5, 6],
    ["a", 2, 0],
    ["abcde", 1, 5],
    ["abcde", 2, 4],
    ["aabcde", 1, 6],
    ["aabcde", 2, 4]
]
solution = Solution()
for s, k, expected in testCases:
    answer = solution.numKLenSubstrNoRepeats(s, k)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected}, got {answer}. INPUTS: s: {s}, k: {k}")

print("Ran all tests")