from collections import defaultdict


class Solution:
    MOD = 10**9 + 7

    # Kinda some magic math here
    # Silly leet code problem I don't think it's worth the time to understand
    # Time O(3^2m * n)
    # Space O(3^2m)
    def colorTheGrid(self, m: int, n: int) -> int:
        # Hash mapping stores all valid coloration schemes for a single row that meet the requirements
        # The key represents mask, and the value represents the ternary string of mask (stored as a list)
        valid = dict()

        # Enumerate masks that meet the requirements within the range [0, 3^m)
        for mask in range(3**m):
            color = []
            mm = mask
            for _ in range(m):
                color.append(mm % 3)
                mm //= 3
            if any(color[i] == color[i + 1] for i in range(m - 1)):
                continue
            valid[mask] = color

        # Preprocess all (mask1, mask2) binary tuples, satisfying mask1 and mask2 When adjacent rows, the colors of the two cells in the same column are different
        adjacent = defaultdict(list)
        for mask1, color1 in valid.items():
            for mask2, color2 in valid.items():
                if not any(x == y for x, y in zip(color1, color2)):
                    adjacent[mask1].append(mask2)

        f = [int(mask in valid) for mask in range(3**m)]
        for i in range(1, n):
            g = [0] * (3**m)
            for mask2 in valid.keys():
                for mask1 in adjacent[mask2]:
                    g[mask2] += f[mask1]
                    if g[mask2] >= self.MOD:
                        g[mask2] -= self.MOD
            f = g

        return sum(f) % self.MOD
    
test_cases = [
    [3, 1, 1],
    [6, 1, 2],
    [6, 2, 1],
    [18, 2, 2],
    [580986, 5, 5]
]
solution = Solution()
for expected, m, n in test_cases:
    actual = solution.colorTheGrid(m, n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: m: {m}, n: {n}")

print("Ran all tests")