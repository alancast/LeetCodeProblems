class Solution:
    # Stack of letters and greedily keeping longest
    # Time O(n) as go over characters just once
    # Space O(alphabet)
    def smallestSubsequence(self, s: str) -> str:
        # Find counts of each char
        char_counts = [0] * 26
        for char in s:
            char_counts[ord(char) - ord("a")] += 1


        vis = [0] * 26
        stack = []
        # Go over every char in string
        for char in s:
            idx = ord(char) - ord("a")
            if not vis[idx]:
                while stack and stack[-1] > char:
                    top_idx = ord(stack[-1]) - ord("a")
                    if char_counts[top_idx] > 0:
                        vis[top_idx] = 0
                        stack.pop()
                    else:
                        break
                vis[idx] = 1
                stack.append(char)
            char_counts[idx] -= 1

        return "".join(stack)

test_cases = [
    ["abc", "bcabc"],
    ["acdb", "cbacdcbc"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.smallestSubsequence(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
