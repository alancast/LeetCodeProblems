class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_map = {}
        for char in s:
            s_map[char] = s_map.get(char, 0) + 1

        for char in t:
            if char not in s_map:
                return char

            s_map[char] -= 1
            if s_map[char] == 0:
                del s_map[char]

        raise Exception("Something went wrong, no difference was found")

testCases = [
    ["abcd", "abcde", "e"],
    ["", "y", "y"],
    ["aa", "aaa", "a"]
]
solution = Solution()
for s, t, expected in testCases:
    answer = solution.findTheDifference(s, t)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} got {answer}. S: {s}, t: {t}")

print("Ran all tests")
