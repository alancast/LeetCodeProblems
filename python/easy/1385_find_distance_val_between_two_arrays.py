class Solution:
    # Count values in arr1 that are more than d away from every value in arr2.
    # Time O(nm)
    # Space O(1)
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        distance_value = 0

        for num in arr1:
            # Count the value only if no value in arr2 is within distance d.
            if all(abs(num - other) > d for other in arr2):
                distance_value += 1

        return distance_value

test_cases = [
    [2, [4, 5, 8], [10, 9, 1, 8], 2],
    [2, [1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3],
    [1, [2, 1, 100, 3], [-5, -2, 10, -3, 7], 6],
]
solution = Solution()
for expected, arr1, arr2, d in test_cases:
    actual = solution.findTheDistanceValue(arr1, arr2, d)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: arr1: {arr1}, arr2: {arr2}, d: {d}")

print("Ran all tests")
