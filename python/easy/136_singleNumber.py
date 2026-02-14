class Solution:
    # Xor method. O(n) runtime. O(1) space
    def singleNumber(self, nums: list[int]) -> int:
        # Num xor itself = 0. Num xor 0 = itself
        # So dupes cancel out and only number left is itself
        xor_num = 0
        for num in nums:
            xor_num ^= num

        return xor_num

    # Math, O(n) time. O(n) storage for the set
    def singleNumberSums(self, nums: list[int]) -> int:
        return (2 * sum(set(nums))) - sum(nums)

    # Hash table. O(n) time, O(n) storage
    def singleNumberHash(self, nums: list[int]) -> int:
        numSet = set()
        for num in nums:
            if num in numSet:
                numSet.remove(num)
            else:
                numSet.add(num)

        for val in numSet:
            return val

        raise Exception("INVALID input, set didn't have duplicate")

testCases = [
    [[2,2,1], 1],
    [[2], 2],
    [[4,1,2,1,2], 4]
]
solution = Solution()
for nums, expected in testCases:
    answer = solution.singleNumber(nums)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected}, but got {answer}. INPUT: {nums}")

print("Ran all tests")
