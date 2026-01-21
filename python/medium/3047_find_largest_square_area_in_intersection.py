from typing import List


class Solution:
    # Brute force n^2 implementation
    # For every point, evaluate all other points and see max overlap
    # Same as below but much simpler inner loop
    # Time O(n^2)
    # Space O(1)
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side = 0

        for i in range(n):
            one_x_low, one_y_low = bottomLeft[i]
            one_x_high, one_y_high = topRight[i]
            for j in range(i+1, n):
                two_x_low, two_y_low = bottomLeft[j]
                two_x_high, two_y_high = topRight[j]

                vertical_overlap = min(one_y_high, two_y_high) - max(one_y_low, two_y_low)
                horizontal_overlap = min(one_x_high, two_x_high) - max(one_x_low, two_x_low)
                max_side = max(max_side, min(vertical_overlap, horizontal_overlap))

        return max_side * max_side

    # Brute force n^2 implementation
    # For every point, evaluate all other points and see max overlap
    # Time O(n^2)
    # Space O(1)
    def largestSquareArea_long(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_area = 0

        for i in range(n):
            one_x_low, one_y_low = bottomLeft[i]
            one_x_high, one_y_high = topRight[i]
            for j in range(i+1, n):
                two_x_low, two_y_low = bottomLeft[j]
                two_x_high, two_y_high = topRight[j]

                vertical_overlap = 0
                horizontal_overlap = 0
                # Find vertical overlap
                # No vertical overlap
                if one_y_high <= two_y_low or one_y_low >= two_y_high:
                    continue
                # One inside two
                if one_y_low >= two_y_low and one_y_high <= two_y_high:
                    vertical_overlap = one_y_high - one_y_low
                # Two inside one
                elif two_y_low >= one_y_low and two_y_high <= one_y_high:
                    vertical_overlap = two_y_high - two_y_low
                # One top above two base
                elif one_y_high > two_y_low and one_y_low < two_y_low:
                    vertical_overlap = one_y_high - two_y_low
                # One base below two top
                elif one_y_low < two_y_high:
                    vertical_overlap = two_y_high - one_y_low

                # Find horizontal overlap
                # No horizontal overlap
                if one_x_high <= two_x_low or one_x_low >= two_x_high:
                    continue
                # One inside two
                if one_x_low >= two_x_low and one_x_high <= two_x_high:
                    horizontal_overlap = one_x_high - one_x_low
                # Two inside one
                elif two_x_low >= one_x_low and two_x_high <= one_x_high:
                    horizontal_overlap = two_x_high - two_x_low
                # One right right of two left
                elif one_x_high > two_x_low and one_x_low < two_x_low:
                    horizontal_overlap = one_x_high - two_x_low
                # One left left of two right
                elif one_x_low < two_x_high:
                    horizontal_overlap = two_x_high - one_x_low
                
                square_side = min(vertical_overlap, horizontal_overlap)
                max_area = max(max_area, square_side * square_side)

        return max_area

test_cases = [
    [1, [[1,1],[2,2],[3,1]], [[3,3],[4,4],[6,6]]],
    [4, [[1,1],[1,3],[1,5]], [[5,5],[5,7],[5,9]]],
    [1, [[1,1],[2,2],[1,2]], [[3,3],[4,4],[3,4]]],
    [0, [[1,1],[3,3],[3,1]], [[2,2],[4,4],[4,2]]]
]
solution = Solution()
for expected, bottom_left, top_right in test_cases:
    actual = solution.largestSquareArea(bottom_left, top_right)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: bottom_left: {bottom_left}, top_right: {top_right}")

print("Ran all tests")
