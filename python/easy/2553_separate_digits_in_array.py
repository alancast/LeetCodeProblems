class Solution:
    # Reverse traversal of the list then flip at the end
    # Time O(nlogm) where M is max num in list
    # Space O(1)
    def separateDigits(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = []
        # Go from end of array to start (because we reverse and go by ones)
        for i in range(n-1, -1, -1):
            x = nums[i]
            # Add all digits to array and shrink number
            while x > 0:
                answer.append(x % 10)
                x //= 10

        # Reverse order and return
        answer.reverse()
        return answer

test_cases = [
    [[1,3,2,5,8,3,7,7], [13,25,83,77]],
    [[7,1,3,9], [7,1,3,9]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.separateDigits(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
