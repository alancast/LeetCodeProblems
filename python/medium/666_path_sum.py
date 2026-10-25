class Solution:
    # Just BFS
    # Time O(n)
    # Space O(n)
    def pathSum(self, nums: list[int]) -> int:
        # Store each node value by its depth and position.
        node_values = {}

        # Separate each node's coordinates from its value.
        for element in nums:
            coordinates = element // 10
            value = element % 10
            node_values[coordinates] = value

        # Start the queue with the root and its value as the current path sum.
        root = nums[0] // 10
        queue = [(root, node_values[root])]
        total_sum = 0

        # Visit each node and track the sum from the root to that node.
        while queue:
            coordinates, current_sum = queue.pop(0)
            level = coordinates // 10
            position = coordinates % 10

            left = (level + 1) * 10 + position * 2 - 1
            right = (level + 1) * 10 + position * 2

            # Add the path sum when the node has no children.
            if left not in node_values and right not in node_values:
                total_sum += current_sum

            # Add existing children with their values included in the path sum.
            if left in node_values:
                queue.append((left, current_sum + node_values[left]))

            if right in node_values:
                queue.append((right, current_sum + node_values[right]))

        return total_sum

test_cases = [
    [12, [113,215,221]],
    [4, [113,221]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.pathSum(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
