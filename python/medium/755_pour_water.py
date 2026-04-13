class Solution:
    # Just try all spots for each attempt
    # Time O(volume * n)
    # Space O(1)
    def pourWater(self, heights: list[int], volume: int, k: int) -> list[int]:
        n = len(heights)

        for _ in range(volume):
            # Try to left of k
            index = k
            min_height = heights[k]
            min_left = k + 1
            while index >= 0:
                # We will not go further left than this
                if heights[index] > min_height:
                    break

                # New min height found
                if heights[index] < min_height:
                    min_height = heights[index]
                    min_left = index

                index -= 1

            # Fill spot to left
            if min_left < k:
                heights[min_left] += 1
                continue

            # Try to right of k
            index = k
            min_height = heights[k]
            min_right = k - 1
            while index < n:
                # We will not go further right than this
                if heights[index] > min_height:
                    break

                # New min height found
                if heights[index] < min_height:
                    min_height = heights[index]
                    min_right = index

                index += 1

            # Fill spot to right
            if min_right > k:
                heights[min_right] += 1
                continue

            # Just keep right there
            heights[k] += 1

        return heights

test_cases = [
    [[2,2,2,3,2,2,2], [2,1,1,2,1,2,2], 4, 3],
    [[2,3,3,4], [1,2,3,4], 2, 2],
    [[4,4,4], [3,1,3], 5, 1]
]
solution = Solution()
for expected, heights, volume, k in test_cases:
    actual = solution.pourWater(heights, volume, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: heights: {heights}, volume: {volume}, k: {k}")

print("Ran all tests")
