from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    # Same logic as below but improved binary search bounds by keeping track
    # Of position we've seen in previous rows
    # N is length for row, M is num rows
    # Time O(n*m*logn)
    # Space O(m) as we store lower bound for each row
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        # Store lower_bound indexes we've already been to for each row
        lower_bounds = [0] * m

        for candidate_num in mat[0]:
            in_all = True
            for i in range(1, m):
                other_row = mat[i]

                # Use bisect to binary search for candidate_num in other_row
                # This returns where to insert the candidate num into the other row
                # So if idx == n that means it's bigger than all in row
                # If other_row[idx] != num then it doesn't exist in the row
                idx = bisect_left(other_row, candidate_num, lower_bounds[i])

                # Update lower bound for this row
                lower_bounds[i] = idx

                # If this num is bigger than everything in the row no sense in checking
                # Any nums after as they will also all be too big
                if idx == n:
                    return -1
                
                # The num doesn't exist in the row
                if other_row[idx] != candidate_num:
                    in_all = False
                    break

            if in_all:
                return candidate_num

        return -1

    # Go over first row
    # For each num in row do binary search for if it's in other rows
    # First time one is in all rows return that num
    # If get to end of first row return -1
    # Time O(n*m*logn)
    # Space O(1)
    def smallestCommonElement_binary_search(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        for candidate_num in mat[0]:
            in_all = True
            for i in range(1, m):
                other_row = mat[i]

                # Use bisect to binary search for candidate_num in other_row
                # This returns where to insert the candidate num into the other row
                # So if idx == n that means it's bigger than all in row
                # If other_row[idx] != num then it doesn't exist in the row
                idx = bisect_left(other_row, candidate_num)
                # If this num is bigger than everything in the row no sense in checking
                # Any nums after as they will also all be too big
                if idx == n:
                    return -1
                
                # The num doesn't exist in the row
                if other_row[idx] != candidate_num:
                    in_all = False
                    break

            if in_all:
                return candidate_num

        return -1
    
    # Go over all nums and compute count
    # Then go over counts map and see which num is smallest that has full count
    # Time O(nm)
    # Space O(nm) if they are all different nums
    def smallestCommonElement_num_counts(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        # Compute num counts
        num_counts = defaultdict(int)
        for i in range(m):
            for j in range(n):
                num_counts[mat[i][j]] += 1

        answer = -1
        for key, value in num_counts.items():
            # Make sure the num has the correct count
            if value == m:
                if answer == -1:
                    answer = key
                elif key < answer:
                    answer = key

        return answer
    
test_cases = [
    [5, [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]],
    [2, [[1,2,3],[2,3,4],[2,3,5]]],
    [-1, [[1,2,3],[2,3,4],[1,4,5]]]
]
solution = Solution()
for expected, mat in test_cases:
    actual = solution.smallestCommonElement(mat)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: mat: {mat}")

print("Ran all tests")