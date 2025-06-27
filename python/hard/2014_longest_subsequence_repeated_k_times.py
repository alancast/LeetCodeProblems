from collections import Counter, deque


class Solution:
    # Brute force go through combos
    # Time O(n*(n//k)!)
    # Space O((n//k)!)
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        answer = ""

        # In order for a char to be in the answer it must appear at least k times in string
        # Create a list of all possible characters
        char_counts = Counter(s)
        candidate_chars = []
        for char, count in char_counts.items():
            if count >= k:
                candidate_chars.append(char)

        # Sorted in reverse order to meet answer constraint of 
        # if tie sort lexicographically largest
        candidate_chars.sort(reverse=True)

        # Try to build all answers and see which one is longest
        q = deque(candidate_chars)
        while q:
            # Start with largest char and try to build subsequence from there on
            curr = q.popleft()
            if len(curr) > len(answer):
                answer = curr

            # generate the next candidate string
            for char in candidate_chars:
                nxt = curr + char

                # Iterator makes sure that we are checking in order
                it = iter(s)
                # This checks to make sure that nxt appears in order in s k times
                # nxt * k makes the string nxt repeated k times
                # all char in it makes sure every char in that string is in it 
                # in order (as s is iterated over)
                if all(char in it for char in nxt * k):
                    q.append(nxt)

        return answer
    
test_cases = [
    ["let", "letsleetcode", 2],
    ["b", "bb", 2],
    ["", "ab", 2]
]
solution = Solution()
for expected, s, k in test_cases:
    actual = solution.longestSubsequenceRepeatedK(s, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}, k: {k}")

print("Ran all tests")