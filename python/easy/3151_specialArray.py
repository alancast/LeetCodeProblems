class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        return self.isArraySpecialBitwise(nums)

    # Check each pair via bitwise XOR
    # Time O(n), space O(1)
    def isArraySpecialBitwise(self, nums: list[int]) -> bool:
        for i in range(len(nums)-1):  # noqa: SIM110
            # Compare the parities using bitwise operations
            if ((nums[i] & 1) ^ (nums[i + 1] & 1)) == 0:
                # If the two adjacent numbers have the same parity, return False
                return False

        return True

    # Intuitive check each pair via modulo
    # Time O(n), space O(1)
    def isArraySpecialIntuitive(self, nums: list[int]) -> bool:
        for i in range(len(nums)-1):
            # if both odd return False
            if (nums[i] % 2) == 1 and (nums[i+1] % 2) == 1:
                return False
            # if both even return False
            if (nums[i] % 2) == 0 and (nums[i+1] % 2) == 0:
                return False

        return True

testCases = [
    [[1], True],
    [[2,1,4], True],
    [[4,3,1,6], False]
]
solution = Solution()
for nums, expected in testCases:
    answer = solution.isArraySpecial(nums)
    if answer != expected:
        print(f"TEST FAILED: Expected {expected} but got {answer}. Input: {nums}")

print("Ran all tests")
