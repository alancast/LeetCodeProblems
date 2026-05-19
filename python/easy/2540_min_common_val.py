class Solution:
    # Sliding window pointer. Just increment whichever one is smaller
    # Time O(n)
    # Space O(1)
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        p1 = p2 = 0

        while p1 < n and p2 < m:
            num1 = nums1[p1]
            num2 = nums2[p2]

            if num1 == num2:
                return num1

            # Increment whichever pointer is the smaller number
            if num1 < num2:
                p1 += 1
            else:
                p2 += 1

        # This will never happen as we know there is a common num
        # Could throw here
        return -1

test_cases = [
    [2, [1,2,3], [2,4]],
    [2, [1,2,3,6], [2,3,4,5]]
]
solution = Solution()
for expected, nums1, nums2 in test_cases:
    actual = solution.getCommon(nums1, nums2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums1: {nums1}, nums2: {nums2}")

print("Ran all tests")
