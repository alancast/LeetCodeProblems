from typing import List


class Solution:
    MOD = 10**9 + 7

    # Get distance between edges in horizontal and vertical fences
    # See if there is an overlap between the distances (a square)
    # If so take max, if not return -1
    # Time O(v^2 + h^2)
    # Space O(v^2 + h^2) for set
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        # Get all edge lengths
        h_edges = self._get_edges(hFences, m)
        v_edges = self._get_edges(vFences, n)

        # Find max value in both sets
        max_edge = max(h_edges & v_edges, default=0)

        if not max_edge:
            return -1

        return (max_edge * max_edge) % self.MOD

    # Take in the list of fences and what the final border is
    # Return set of all edge lengths possible
    # Time O(f^2)
    # Space O(f^2)
    def _get_edges(self, fences: List[int], border: int) -> set:
        points = sorted([1] + fences + [border])

        edge_lengths = set()
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edge_lengths.add(points[j] - points[i])

        return edge_lengths

test_cases = [
    [4, 4, 3, [2,3], [2]],
    [-1, 6, 7, [2], [4]]
]
solution = Solution()
for expected, n, m, h_fences, v_fences in test_cases:
    actual = solution.maximizeSquareArea(n, m, h_fences, v_fences)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, m: {m}, h_fences: {h_fences}, v_fences: {v_fences}")

print("Ran all tests")
