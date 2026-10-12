class Solution:
    # Compute the absolute difference for each pair.
    # Binary search the final max diff, then greedily reduce the largest differences.
    # Time O(n log V)
    # Space O(n)
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # Combine all moves into one total budget.
        total_changes = k1 + k2
        n = len(nums1)

        # Track how far apart each pair is at each index.
        differences = [abs(nums1[i] - nums2[i]) for i in range(n)]
        max_diff = max(differences, default=0)

        # Binary search the best final difference value.
        left, right, best_diff = 0, max_diff, 0
        while left <= right:
            middle = (left + right) // 2
            # If all values above middle can be reduced with the available moves, keep searching lower.
            if sum(num - middle for num in differences if num > middle) <= total_changes:
                right = middle - 1
                best_diff = middle
            else:
                left = middle + 1

        # Save the remaining moves after reducing every value down to best_diff.
        remaining_changes = total_changes
        for num in differences:
            if num > best_diff:
                remaining_changes -= num - best_diff

        # Sort from largest to smallest so the biggest reductions happen first.
        differences.sort(reverse=True)
        answer = 0
        for num in differences:
            # Reduce the current difference as much as possible.
            current_diff = min(num, best_diff)
            if remaining_changes > 0 and current_diff > 0:
                current_diff -= 1
                remaining_changes -= 1
            answer += current_diff * current_diff

        return answer

test_cases = [
    [579, [1, 2, 3, 4], [2, 10, 20, 19], 0, 0],
    [43, [1, 4, 10, 12], [5, 8, 6, 9], 1, 1],
]
solution = Solution()
for expected, nums1, nums2, k1, k2 in test_cases:
    actual = solution.minSumSquareDiff(nums1, nums2, k1, k2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums1: {nums1}, nums2: {nums2}, k1: {k1}, k2: {k2}")

print("Ran all tests")
