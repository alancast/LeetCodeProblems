class Solution:
    # Two pointers, just go over each array once and find max distance
    # Time O(n + m)
    # Space O(1)
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        answer = 0

        num_2_idx = 0
        # Evaluate each number in nums1
        for num_1_idx in range(n):
            num1 = nums1[num_1_idx]

            # Find the furthest away num2 bigger than this one
            while num_2_idx < m and num1 <= nums2[num_2_idx]:
                num_2_idx += 1

            # See if we have a new max distance
            num2 = nums2[num_2_idx - 1]
            if num2 >= num1:
                # Subtract 1 because we went too far on nums2 to get out of while loop
                answer = max(answer, num_2_idx - num_1_idx - 1)

            # If we are at the end of nums2 we won't beat this answer
            if num_2_idx == m:
                break

        return answer

test_cases = [
    [2, [55,30,5,4,2], [100,20,10,10,5]],
    [1, [2,2,2], [10,10,1]],
    [2, [30,29,19,5], [25,25,25,25,25]]
]
solution = Solution()
for expected, nums1, nums2 in test_cases:
    actual = solution.maxDistance(nums1, nums2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums1: {nums1}, nums2: {nums2}")

print("Ran all tests")
