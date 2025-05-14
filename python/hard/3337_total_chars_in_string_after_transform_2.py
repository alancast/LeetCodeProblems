from collections import defaultdict
from typing import List


# This exceeds the time limit, but the other solution is just matrix math not worth understanding
class SolutionUnderstandable:
    MOD = 10**9 + 7

    # Time Limit exceeds with long s, high t, and large nums
    # Time O(n + t*num) get count of each char and then iterate
    # Space O(1) store multiple 26 int lists
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # Create map for char index and what it goes to
        # key: char index value: list of chars that get added
        transformation_map = defaultdict(list)
        for i in range(26):
            for j in range(1, nums[i] + 1):
                # Take care of wraparound
                offset = i + j
                if i + j > 25:
                    offset -= 26
                transformation_map[i].append(offset)

        # Initialize char count array
        char_count = [0] * 26
        for ch in s:
            char_count[ord(ch) - ord('a')] += 1   

        # Go through every transformation and create new char counts
        for round in range(t):
            nxt = [0] * 26

            for i, count in enumerate(char_count):
                for next_char in transformation_map[i]:
                    nxt[next_char] += count
                    nxt[next_char] %= self.MOD

            char_count = nxt 

        return sum(char_count) % self.MOD

MOD = 10**9 + 7
L = 26


class Mat:
    def __init__(self, copy_from: "Mat" = None) -> None:
        self.a: List[List[int]] = [[0] * L for _ in range(L)]
        if copy_from:
            for i in range(L):
                for j in range(L):
                    self.a[i][j] = copy_from.a[i][j]

    def __mul__(self, other: "Mat") -> "Mat":
        result = Mat()
        for i in range(L):
            for j in range(L):
                for k in range(L):
                    result.a[i][j] = (result.a[i][j] + self.a[i][k] * other.a[k][j]) % MOD
        return result


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        T = Mat()
        for i in range(26):
            for j in range(1, nums[i] + 1):
                T.a[(i + j) % 26][i] = 1

        res = self.quickmul(T, t)

        f = [0] * 26
        for ch in s:
            f[ord(ch) - ord("a")] += 1

        ans = 0
        for i in range(26):
            for j in range(26):
                ans = (ans + res.a[i][j] * f[j]) % MOD

        return ans
    
    # identity matrix
    def I(self) -> Mat:
        m = Mat()
        for i in range(L):
            m.a[i][i] = 1
        return m


    # matrix exponentiation by squaring
    def quickmul(self, x: Mat, y: int) -> Mat:
        ans = self.I()
        cur = x
        while y:
            if y & 1:
                ans = ans * cur
            cur = cur * cur
            y >>= 1
        return ans


test_cases = [
    [7, "abcyy", 2, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]],
    [8, "azbk", 1, [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
]
solution = Solution()
for expected, s, t, nums in test_cases:
    actual = solution.lengthAfterTransformations(s, t, nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}, t: {t}, nums: {nums}")

print("Ran all tests")