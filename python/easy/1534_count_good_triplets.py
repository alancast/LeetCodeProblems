class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        self.validate_input(arr, a, b, c)
        return self.count_good_triplets_brute_force(arr, a, b, c)

    # Time O(n^3) as we iterate the whole list 3 times
    # Space O(1)
    def count_good_triplets_brute_force(self, arr: list[int], a: int, b: int, c: int) -> int:
        n = len(arr)

        count_good = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                # Some minor optimizations that can prune searching
                if abs(arr[i] - arr[j]) > a:
                    continue

                for k in range(j + 1, n):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count_good += 1

        return count_good

    def validate_input(self, arr: list[int], a: int, b: int, c: int) -> None:
        if a < 0 or a > 1000:  # noqa: PLR2004
            raise ValueError("a must be between 0 and 1000")
        if b < 0 or b > 1000:  # noqa: PLR2004
            raise ValueError("b must be between 0 and 1000")
        if c < 0 or c > 1000:  # noqa: PLR2004
            raise ValueError("c must be between 0 and 1000")
        if len(arr) < 3 or len(arr) > 100:  # noqa: PLR2004
            raise ValueError("The length of arr must be between 3 and 100")

test_cases = [
    [4, [3,0,1,1,9,7], 7, 2, 3],
    [0, [1,1,2,2,3], 0, 0, 1]
]
solution = Solution()
for expected, arr, a, b, c in test_cases:
    actual = solution.countGoodTriplets(arr, a, b, c)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: arr: {arr}, a: {a}, b: {b}, c: {c}")

print("Ran all tests")
