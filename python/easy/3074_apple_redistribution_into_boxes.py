from typing import List


class Solution:
    # Find sum of apples and then reverse sort into boxes
    # Time O(n + mlogm)
    # Space O(m) for sort
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)

        capacity.sort(reverse=True)
        boxes_used = 0
        for cap in capacity:
            total_apples -= cap
            boxes_used += 1
            if total_apples <= 0:
                break

        return boxes_used

test_cases = [
    [2, [1,3,2], [4,3,1,5,2]],
    [4, [5,5,5], [2,4,2,7]]
]
solution = Solution()
for expected, apple, capacity in test_cases:
    actual = solution.minimumBoxes(apple, capacity)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: apple: {apple}, capacity: {capacity}")

print("Ran all tests")