from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for x in range(1, n + 1):
            ans[x] = ans[x // 2] + (x % 2) 

        return ans

testCases = [
    [2, [0,1,1]],
    [5, [0,1,1,2,1,2]]   
]
implementation = Solution()
for n, expected in testCases:
    answer = implementation.countBits(n)
    if answer != expected:
        print(f"FAILED TEST: n: {n} Got {answer} but expected {expected}")