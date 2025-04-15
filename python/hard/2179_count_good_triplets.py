from typing import List

class FenwickTree:
    def __init__(self, size):
        # Fenwick trees always 1 indexed
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        index += 1
        while index <= len(self.tree) - 1:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

class Solution:
    # Time O(nlogn) as the Fenwick tree operations are all logn and we do n of them
    # Space O(n) as we clone the array into a tree
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2, reversedIndexMapping = [0] * n, [0] * n

        # Create index mapping
        for i, num2 in enumerate(nums2):
            pos2[num2] = i

        # Create reversed index mapping
        # Which means pos2[num1] is the index in nums2 where num1 is located
        # So reverseIndexMapping[pos2[num1]] = i means num2 index maps to this nums1 index
        for i, num1 in enumerate(nums1):
            reversedIndexMapping[pos2[num1]] = i

        tree = FenwickTree(n)
        res = 0

        # Go through every number
        for value in range(n):
            # nums2 index "value" is x index in nums1
            # So for 0 pos = index in nums1 of what is nums2[0]
            pos = reversedIndexMapping[value]
            # number of elements left in nums1 of this one that we've processed
            left = tree.query(pos)
            tree.update(pos, 1)
            # number of elements right in nums1 of this one that we've yet to process
            right = (n - 1 - pos) - (value - left)

            # If processed none left then this can't be middle of anything
            # Similarly if processed all right already then this can't be middle of anything
            # But can be middle of how many we've already done to the left and how many are left on the right
            res += left * right

        return res
    
test_cases = [
    [1, [2,0,1,3], [0,1,2,3]],
    [4, [4,0,1,3,2], [4,1,0,2,3]]
]
solution = Solution()
for expected, nums1, nums2 in test_cases:
    actual = solution.goodTriplets(nums1, nums2)
    if expected != actual:
        print(f"FAILED TEST: Expected {expected} but got {actual}")

print("Ran all tests")