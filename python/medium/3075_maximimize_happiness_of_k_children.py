from typing import List


class Solution:
    # Sort happiness and take the top k
    # Time O(nlogn)
    # Space O(n) for sort
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)

        answer = 0
        for i in range(k):
            answer += max(happiness[i]-i, 0)

        return answer

test_cases = [
    [4, [1,2,3], 2],
    [1, [1,1,1,1], 2],
    [5, [2,3,4,5], 1]
]
solution = Solution()
for expected, happiness, k in test_cases:
    actual = solution.maximumHappinessSum(happiness, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: happiness: {happiness}, k: {k}")

print("Ran all tests")