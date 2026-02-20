class Solution:
    # Recurse to get string
    # Time O(n^2)
    # Space O(n)
    def makeLargestSpecial(self, s: str) -> str:
        subs = []
        balance = start = 0

        for i, ch in enumerate(s):
            balance += 1 if ch == '1' else -1
            if balance == 0:
                mid = self.makeLargestSpecial(s[start + 1:i])
                subs.append('1' + mid + '0')
                start = i+1

        subs.sort(reverse = True)
        return ''.join(subs)

test_cases = [
    ["11100100", "11011000"],
    ["10", "10"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.makeLargestSpecial(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
