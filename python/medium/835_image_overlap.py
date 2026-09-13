class Solution:
    # Compute every relative shift between every 1 in img1 and every 1 in img2.
    # Each shift corresponds to a possible overlap placement.
    # Time O(n^4) worst case, since there can be O(n^2) ones in each image and we compare all pairs
    # Space O(n^2) for the shift-count grid and the list of 1 positions
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)

        # Store the coordinates of all 1s in each image.
        A = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        B = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]

        # Track how many times each relative shift occurs.
        # We offset by n so that negative/positive deltas can still be indexed.
        cnt = [[0] * (2 * n) for _ in range(2 * n)]
        best = 0

        # For each pixel in img1 and each pixel in img2, compute the shift needed
        # to align them. The count of a shift tells us how many pixels overlap under that offset.
        for ax, ay in A:
            for bx, by in B:
                dx = bx - ax + n
                dy = by - ay + n
                cnt[dx][dy] += 1
                best = max(best, cnt[dx][dy])

        return best

test_cases = [
    [3, [[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]]],
    [1, [[1]], [[1]]],
    [0, [[0]], [[0]]]
]
solution = Solution()
for expected, img_1, img_2 in test_cases:
    actual = solution.largestOverlap(img_1, img_2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: img_1: {img_1}, img_2: {img_2}")

print("Ran all tests")
