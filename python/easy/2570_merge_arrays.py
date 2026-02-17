class Solution:
    # Time O(n+m) where n and m are lengths of the arrays
    # Space O(n+m)
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        index1 = index2 = 0
        len1 = len(nums1)
        len2 = len(nums2)

        merged_array = []
        while index1 < len1 and index2 < len2:
            id1 = nums1[index1][0]
            id2 = nums2[index2][0]

            if id1 < id2:
                merged_array.append(nums1[index1])
                index1 += 1
            elif id2 < id1:
                merged_array.append(nums2[index2])
                index2 += 1
            else:
                merged_array.append([id1, nums1[index1][1] + nums2[index2][1]])
                index1 += 1
                index2 += 1

        # Still have nums1 to append
        while index1 < len1:
            merged_array.append(nums1[index1])
            index1 += 1

        # Still have nums2 to append
        while index2 < len2:
            merged_array.append(nums2[index2])
            index2 += 1

        return merged_array

test_cases = [
    [[[1,6],[2,3],[3,2],[4,6]], [[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]],
    [[[1,3],[2,4],[3,6],[4,3],[5,5]], [[2,4],[3,6],[5,5]], [[1,3],[4,3]]]
]
solution = Solution()
for expected, nums1, nums2 in test_cases:
    actual = solution.mergeArrays(nums1, nums2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums1: {nums1}, nums2: {nums2}")

print("Ran all tests")
