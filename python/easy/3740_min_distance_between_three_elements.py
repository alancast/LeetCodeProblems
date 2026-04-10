class Solution:
    MAX_INT = 3939393939

    # Keep a map of first index and last
    # Time O(n)
    # Space O(n)
    def minimumDistance(self, nums: list[int]) -> int:
        # First and last index of a num
        first = {}
        last = {}

        answer = self.MAX_INT
        for idx, num in enumerate(nums):
            if num not in first:
                first[num] = idx
                continue
            if num not in last:
                last[num] = idx
                continue

            # Num is already in first and last, so compute score and update
            score = (idx - last[num]) + (idx - first[num]) + (last[num] - first[num])
            answer = min(score, answer)

            first[num] = last[num]
            last[num] = idx

        # No pair existed
        if answer == self.MAX_INT:
            return -1

        return answer

test_cases = [
    [6, [1,2,1,1,3]],
    [8, [1,1,2,3,2,1,2]],
    [-1, [1]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minimumDistance(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
