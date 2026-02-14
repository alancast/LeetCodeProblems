class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        maxNum = 0
        maxCount = 0
        numCounts = {}
        for num in nums:
            numCounts[num] = numCounts.get(num, 0) + 1
            if numCounts[num] > maxCount:
                maxNum = num
                maxCount = numCounts[num]
                # Optimize when we can break out of for loop
                # Could also break when numLeft < diff from first to second
                # Bud don't want to take the time to implement that
                if maxCount > len(nums) // 2:
                    break

        return maxNum

    # O(n) time, O(1) space
    def majorityElementBayerMoore(self, nums: list[int]) -> int:
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

testCases = [
    [[3,2,3], 3],
    [[2,2,1,1,1,2,2], 2],
    [[1], 1]
]
implementation = Solution()
for nums, expected in testCases:
    answer = implementation.majorityElement(nums)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUT: {nums}")

print("Ran all tests")
