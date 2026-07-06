class Solution:
    # Could sort and do in nlogn
    # Or could do two pass and be O(n)
    # First pass is counting how many of each number occur
    # Second pass is see how high we can get number
    # Time O(n)
    # Space O(n)
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        n = len(arr)

        # How many of each value occur
        counts = [0] * (n + 1)
        for num in arr:
            # Can't get above n as we need to start with 1. So cap at n
            counts[min(num, n)] += 1

        # Second pass see how high we can get number to be
        answer = 1
        for num in range(2, n + 1):
            # How high can we get by leveraging all the counts of this num
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
