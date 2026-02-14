class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        ranges = []
        startNum = nums[0]
        previousNum = nums[0]
        for num in nums[1:]:
            if num == previousNum + 1:
                previousNum = num
                continue

            # We need to add a new range
            # Range of 1
            if previousNum == startNum:
                ranges.append(str(previousNum))
            # Range of larger than one
            else:
                ranges.append(f"{startNum}->{previousNum}")

            previousNum = num
            startNum = num

        # Add final range
        # Range of 1
        if previousNum == startNum:
            ranges.append(str(previousNum))
        # Range of larger than one
        else:
            ranges.append(f"{startNum}->{previousNum}")

        return ranges

testCases = [
    [[0,1,2,4,5,7], ["0->2","4->5","7"]],
    [[0,2,3,4,6,8,9], ["0","2->4","6","8->9"]],
    [[], []],
    [[-1,0], ["-1->0"]],
    [[-1,0, 2], ["-1->0", "2"]],
    [[1], ["1"]]
]
implementation = Solution()
for nums, expected in testCases:
    answer = implementation.summaryRanges(nums)
    if answer != expected:
        print(f"FAILED TEST: Got {answer} but expected {expected}. INPUT: {nums}")

print("Ran all tests")
