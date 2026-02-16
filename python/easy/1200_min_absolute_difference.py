class Solution:
    # Sort array, find min difference, and create array as going
    # Time O(nlogn) for sort
    # Space O(n) for sort
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        n = len(arr)

        arr.sort()

        min_diff = float('inf')
        answer = []
        # Go over and find min difference and update array
        for i in range(n-1):
            # If a new min_diff is found reset array
            if arr[i+1] - arr[i] < min_diff:
                min_diff = arr[i+1] - arr[i]
                answer = []

            # Add this pair to the answer
            if arr[i+1] - arr[i] == min_diff:
                answer.append([arr[i], arr[i+1]])

        return answer

test_cases = [
    [[[1,2], [2,3], [3,4]], [4,2,1,3]],
    [[[1,3]], [1,3,6,10,15]],
    [[[-14,-10], [19,23], [23,27]], [3,8,-10,23,19,-4,-14,27]]
]
solution = Solution()
for expected, arr in test_cases:
    actual = solution.minimumAbsDifference(arr)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: arr: {arr}")

print("Ran all tests")
