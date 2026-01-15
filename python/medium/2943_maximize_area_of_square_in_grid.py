from typing import List


class Solution:
    # Find most consecutive bars that can be removed either h or v
    # Whichever that is is answer
    # Time O(hlogh + vlogv)
    # Space O(logh + log v) for sorts
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        # Sort the bars
        hBars.sort()
        vBars.sort()

        # Find longest horizontal streak
        h_max = h_curr = 1
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i - 1] + 1:
                h_curr += 1
            else:
                h_curr = 1

            h_max = max(h_max, h_curr)

        # Find longest vertical streak
        v_max = v_curr = 1
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i - 1] + 1:
                v_curr += 1
            else:
                v_curr = 1

            v_max = max(v_max, v_curr)

        # See what's shorter vertical or horizontal, as that's the limit
        side = min(h_max, v_max) + 1
        # Area of square is what needs to be returned
        return side * side

test_cases = [
    [4, 2, 1, [2,3], [2]],
    [4, 1, 1, [2], [2]],
    [4, 2, 3, [2,3], [2,4]]
]
solution = Solution()
for expected, n, m, h_bars, v_bars in test_cases:
    actual = solution.maximizeSquareHoleArea(n, m, h_bars, v_bars)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, m: {m}, h_bars: {h_bars}, v_bars: {v_bars}")

print("Ran all tests")
