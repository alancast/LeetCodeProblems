class Solution:
    # Binary search with a minor twist of multiple answers so take lowest
    # Time O(logn)
    # Space O(1)
    def fixedPoint(self, arr: list[int]) -> int:
        left = 0
        right = len(arr) - 1

        # In case no answer exists
        answer = -1
        # Do the binary search
        while left <= right:
            # To avoid overflow
            mid = left + ((right - left) // 2)
            num = arr[mid]

            # Since array is sorted we know everything right of this won't be valid
            if num > mid:
                right = mid - 1
            # Similarly we know everything left of this won't be valid either
            elif num < mid:
                left = mid + 1
            # A potential answer (as num == mid), but lower ones could exist
            else:
                right = mid - 1
                answer = mid

        return answer

testCases = [
    [[-10,-5,0,3,7], 3],
    [[0,2,5,8,17], 0],
    [[-10,-5,3,4,7,9], -1],
    [[0,1,2,3,4,5], 0],
    [[-10,-5,-2,0,4,5,6,7,8,9,10], 4]
]
implementation = Solution()
for nums, expected in testCases:
    answer = implementation.fixedPoint(nums)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUT: {nums}")

print("Ran all tests")
