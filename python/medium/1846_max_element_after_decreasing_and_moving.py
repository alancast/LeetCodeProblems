class Solution:
    # Two pass
    # Time O(n)
    # Space O(n)
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        n = len(arr)
        counts = [0] * (n + 1)

        for num in arr:
            counts[min(num, n)] += 1

        answer = 1
        for num in range(2, n + 1):
            answer = min(answer + counts[num], num)

        return answer

test_cases = [
    [2, [2,2,1,2,1]],
    [3, [100,1,1000]],
    [5, [1,2,3,4,5]]
]
solution = Solution()
for expected, arr in test_cases:
    actual = solution.maximumElementAfterDecrementingAndRearranging(arr)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: arr: {arr}")

print("Ran all tests")
