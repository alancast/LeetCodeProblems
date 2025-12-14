from typing import List


class Solution:
    # Because the bounds of the problem are very small we can "counter sort"
    # This just initializes arrays of nums and keeps count of that num at each index
    # Then just go over and do multiplication that way
    # Time O(n + k) where k is max num (in this case 100)
    # Space O(k)
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        counter1 = [0] * 101
        counter2 = [0] * 101

        # Record the number of occurrence of elements in nums1 and nums2.
        for i in range(n):
            counter1[nums1[i]] += 1
            counter2[nums2[i]] += 1
        
        # Initialize two pointers p1 = 1, p2 = 100.
        # Stands for counter1[1] and counter2[100], respectively.
        p1 = 1
        p2 = 100
        answer = 0
        
        # While the two pointers are in the valid range.
        while p1 <= 100 and p2 > 0:

            # If counter1[p1] == 0, meaning there is no element equals p1 in counter1,
            # thus we shall increment p1 by 1.
            while p1 <= 100 and counter1[p1] == 0:
                p1 += 1

            # If counter2[p2] == 0, meaning there is no element equals p2 in counter2,
            # thus we shall decrement p2 by 1.
            while p2 > 0 and counter2[p2] == 0:
                p2 -= 1

            # If any of the pointer goes beyond the border, we have finished the 
            # iteration, break the loop.
            if p1 == 101 or p2 == 0:
                break

            # Otherwise, we can make at most min(counter1[p1], counter2[p2]) 
            # pairs {p1, p2} from nums1 and nums2, let's call it occ. 
            # Each pair has product of p1 * p2, thus the cumulative sum is 
            # incresed by occ * p1 * p2. Update counter1[p1] and counter2[p2].
            occ = min(counter1[p1], counter2[p2])
            answer += occ * p1 * p2
            counter1[p1] -= occ
            counter2[p2] -= occ
        
        return answer     

    # Sort nums1 ascending and nums2 descending, just take the pairs
    # Time O(nlogn) for sort
    # Space O(n) for sort
    def minProductSum_sort(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        nums1.sort()
        nums2.sort(reverse=True)
        
        answer = 0
        
        # Iterate over two sorted arrays and calculate the cumulative product sum. 
        for i in range(n):
            answer += nums1[i] * nums2[i]

        return answer

test_cases = [
    [40, [5,3,4,2], [4,2,2,5]],
    [65, [2,1,4,5,7], [3,2,4,8,6]]
]
solution = Solution()
for expected, nums1, nums2 in test_cases:
    actual = solution.minProductSum(nums1, nums2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums1: {nums1}, nums2: {nums2}")

print("Ran all tests")