class Solution:
    # Go over every fruit and for each one go over baskets list in order
    # After using a basket set it's capacity to zero
    # Time O(n^2) as for every fruit we go through nested basket index
    # Space O(1)
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        n = len(fruits)

        answer = 0
        # Go over all fruits to see what basket they belong in
        for fruit_count in fruits:
            placed = False

            # Go over all baskets
            for i in range(n):
                # Check if this capacity is big enough and use it
                basket_capacity = baskets[i]
                if fruit_count <= basket_capacity:
                    placed = True
                    baskets[i] = 0
                    break

            # See if fruit couldn't be placed
            if not placed:
                answer += 1

        return answer

    # Go over every fruit and for each one go over baskets list in order
    # Keep track of what baskets are used with a hash map
    # Time O(n^2) as for every fruit we go through nested basket index
    # Space O(n) as we keep a full set of indexes used
    def numOfUnplacedFruits_hash(self, fruits: list[int], baskets: list[int]) -> int:
        n = len(fruits)

        used_indexes = set()
        answer = 0
        # Go over all fruits to see what basket they belong in
        for fruit_count in fruits:
            placed = False
            for i in range(n):
                # Make sure basket isn't already used
                if i in used_indexes:
                    continue

                # Check if this capacity is big enough and use it
                basket_capacity = baskets[i]
                if fruit_count <= basket_capacity:
                    placed = True
                    used_indexes.add(i)
                    break

            if not placed:
                answer += 1

        return answer

test_cases = [
    [1, [4,2,5], [3,5,4]],
    [0, [3,6,1], [6,4,7]]
]
solution = Solution()
for expected, fruits, baskets in test_cases:
    actual = solution.numOfUnplacedFruits(fruits, baskets)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: fruits: {fruits}, baskets: {baskets}")

print("Ran all tests")
