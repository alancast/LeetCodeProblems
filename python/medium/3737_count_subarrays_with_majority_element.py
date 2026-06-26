class Solution:
    # Full on enumeration. Evaluate all starting points and for each one all end points
    # Time O(n^2)
    # Space O(1)
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)

        answer = 0
        # Iterate over all starting points
        for i in range(n):
            # For every number in subarray, if it is target add one
            # If it's not subtract one
            # Has majority if count > 0
            net_target_count = 0
            for j in range(i, n):
                if nums[j] == target:
                    net_target_count += 1
                else:
                    net_target_count -= 1

                # See if this subarray has majority target
                if net_target_count > 0:
                    answer += 1

        return answer

test_cases = [
    [5, [1,2,2,3], 2],
    [10, [1,1,1,1], 1],
    [0, [1,2,3], 4]
]
solution = Solution()
for expected, nums, target in test_cases:
    actual = solution.countMajoritySubarrays(nums, target)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, target: {target}")

print("Ran all tests")
