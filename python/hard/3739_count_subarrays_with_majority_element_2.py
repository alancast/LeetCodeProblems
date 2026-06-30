class Solution:
    # Prefix sum of how many instances of target show up so far
    # Time O(n)
    # Space O(n)
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)

        # represents the number of prefixes with prefix sums -n, -(n-1), ..., 0, 1, ..., n, with index offset n
        prefix_sums = [0] * (n * 2 + 1)
        prefix_sums[n] = 1
        cnt = n
        answer = prefix_sum = 0
        for i in range(n):
            if nums[i] == target:
                prefix_sum += prefix_sums[cnt]
                cnt += 1
                prefix_sums[cnt] += 1
            else:
                cnt -= 1
                prefix_sum -= prefix_sums[cnt]
                prefix_sums[cnt] += 1
            answer += prefix_sum

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
