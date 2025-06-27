from typing import List


class Solution:
    # Break into 4 problem spaces (neg * neg, pos * pos, neg * pos, pos * neg)
    # Do binary search for number that has less than k products beneath it
    # Time O((n1+n2)logC) where C is range of problem space we are binary searching
    # Space O(1)
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        # Find first index of nums1 and nums2 that are >= 0
        pos1 = pos2 = 0
        while pos1 < n1 and nums1[pos1] < 0:
            pos1 += 1
        while pos2 < n2 and nums2[pos2] < 0:
            pos2 += 1

        # Binary search to find a number that has k smaller products
        left = int(-1e10)
        right = int(1e10)
        while left <= right:
            mid = (left + right) // 2
            count = 0

            # Find all negative times negatives greater than mid
            i1 = 0
            i2 = pos2 - 1
            while i1 < pos1 and i2 >= 0:
                # incrementing i1 actually makes the product smaller
                if nums1[i1] * nums2[i2] > mid:
                    i1 += 1
                # Decrementing i2 makes the product bigger
                # Add all these products that are smaller than mid
                else:
                    count += pos1 - i1
                    i2 -= 1

            # Find all positive times positive greater than mid
            i1 = pos1
            i2 = n2 - 1
            while i1 < n1 and i2 >= pos2:
                # Makes number smaller
                if nums1[i1] * nums2[i2] > mid:
                    i2 -= 1
                # Makes number bigger, also add all products smaller than mid
                else:
                    count += i2 - pos2 + 1
                    i1 += 1

            # Negative times positive greater than mid
            i1 = 0
            i2 = pos2
            while i1 < pos1 and i2 < n2:
                if nums1[i1] * nums2[i2] > mid:
                    i2 += 1
                else:
                    count += n2 - i2
                    i1 += 1

            # Positive times negative greater than mid
            i1 = pos1
            i2 = 0
            while i1 < n1 and i2 < pos2:
                if nums1[i1] * nums2[i2] > mid:
                    i1 += 1
                else:
                    count += n1 - i1
                    i2 += 1

            # Binary search of count
            if count < k:
                left = mid + 1
            else:
                right = mid - 1
        
        # Found number
        return left
    
test_cases = [
    [8, [2,5], [3,4], 2],
    [0, [-4, -2, 0, 3], [2,4], 6],
    [-6, [-2,-1,0,1,2], [-3,-1,2,4,5], 3]
]
solution = Solution()
for expected, nums1, nums2, k in test_cases:
    actual = solution.kthSmallestProduct(nums1, nums2, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums1: {nums1}, nums2: {nums2}, k: {k}")

print("Ran all tests")