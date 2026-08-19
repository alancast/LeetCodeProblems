from collections import defaultdict


class Solution:
    # Do bitwise operations to see seats
    # Time O(r)
    # Space O(r)
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # The possible seat combinations
        left, middle, right = 0b11110000, 0b11000011, 0b00001111

        # Go over list and update what seats are taken
        occupied = defaultdict(int)
        for seat in reservedSeats:
            if 2 <= seat[1] <= 9:  # noqa: PLR2004
                occupied[seat[0]] |= 1 << (seat[1] - 2)

        # Start by knowing that all rows that are empty can be sat in (twice)
        answer = (n - len(occupied)) * 2

        # Go over all occupied rows and see if there is a place a family could sit
        for _, bitmask in occupied.items():
            if (
                (bitmask | left) == left
                or (bitmask | middle) == middle
                or (bitmask | right) == right
            ):
                answer += 1

        return answer

test_cases = [
    [4, 3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]],
    [4, 4, [[4,3],[1,4],[4,6],[1,7]]]
]
solution = Solution()
for expected, n, reserved_seats in test_cases:
    actual = solution.maxNumberOfFamilies(n, reserved_seats)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, reserved_seats: {reserved_seats}")

print("Ran all tests")
