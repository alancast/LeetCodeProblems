class Solution:
    # Math, find smallest bit of 0 in num and set prior bit to 0
    # Time O(nlogm)
    # Space O(1)
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        answer = []

        # Go over all nums and do operation
        for num in nums:
            # If no way to do it -1 is the answer
            res = -1
            bit_set = 1

            # Find smallest bit that is a 0 in num
            while (num & bit_set) != 0:
                res = num - bit_set
                bit_set <<= 1

            answer.append(res)

        return answer

test_cases = [
    [[-1,1,4,3], [2,3,5,7]],
    [[9,12,15], [11,13,31]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minBitwiseArray(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
