from typing import List


class Solution:
    # Go over all bottom widths and compute area until it's half
    # Time O(nlogn) for sorting horizontal_lines
    # Space O(n)
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        horizontal_lines = []

        for _, y, length in squares:
            total_area += length * length
            # First one is lower line, second one is top
            horizontal_lines.append((y, length, 1))
            horizontal_lines.append((y + length, length, -1))

        # Sort by y-coordinate increasing
        horizontal_lines.sort(key=lambda x: x[0])
        # Sum of all bottom edges under the current scanning line
        covered_width = 0.0
        curr_area = 0.0 
        prev_height = 0.0

        # Go over all the horizontal lines until total area is proper
        for y, l, delta in horizontal_lines:
            # Height gap from this to previous line
            diff = y - prev_height
            # Newly added area
            new_area = covered_width * diff
            # If this newly added area exceeds more than half of the total area
            # Then the line is within that
            if 2 * (curr_area + new_area) >= total_area:
                answer = prev_height + (total_area - (2 * curr_area)) / (2 * covered_width)
                return round(answer, 5)

            # Still more area to add so updated width below line and add area
            # If it's the top line the delta will be -1 
            # So it removes as we've added all area for that square
            covered_width += delta * l
            curr_area += new_area
            prev_height = y

        # This will never happen, as we are guaranteed to get to half the total area
        return 0.0

    # Binary search to find the answer
    # Pick a number between 0 and max y and see if it's right
    # Time O(nlogn)
    # Space O(1)
    def separateSquares_binary_search(self, squares: List[List[int]]) -> float:
        # Find the max y and total area
        max_y = total_area = 0
        for _, y, l in squares:
            total_area += l**2
            max_y = max(max_y, y + l)

        # See if more than half of the total area is below limit_y
        def more_than_half(limit_y: float) -> bool:
            area = 0
            for _, y, l in squares:
                if y < limit_y:
                    area += l * min(limit_y - y, l)

            return area >= total_area / 2

        low = 0
        high = max_y
        sig_digs = 1e-5
        # Binary search until we are within the proper amount of clarity
        while abs(high - low) > sig_digs:
            mid = (high + low) / 2
            if more_than_half(mid):
                high = mid
            else:
                low = mid

        return round(high, 5)

test_cases = [
    [1.00000, [[0,0,1],[2,2,1]]],
    [1.16667, [[0,0,2],[1,1,1]]]
]
solution = Solution()
for expected, squares in test_cases:
    actual = solution.separateSquares(squares)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: squares: {squares}")

print("Ran all tests")
