class Solution:
    # Just search in each direction
    # Time O(nL)
    # Space O(1)
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)

        for distance in range((n//2)+1):
            if words[startIndex - distance] == target or words[(startIndex + distance)%n] == target:
                return distance

        return -1

test_cases = [
    [1, ["hello","i","am","leetcode","hello"], "hello", 1],
    [1, ["a","b","leetcode"], "leetcode", 0],
    [-1, ["i","eat","leetcode"], "ate", 0]
]
solution = Solution()
for expected, words, target, start_index in test_cases:
    actual = solution.closestTarget(words, target, start_index)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: words: {words}, target: {target}, start_index: {start_index}")

print("Ran all tests")
