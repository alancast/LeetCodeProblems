class Solution:
    # Just go over list from right to left and store max height
    # Then reverse list for answer
    # Time O(n)
    # Space O(1) just for answer (can swap in place)
    def findBuildings(self, heights: list[int]) -> list[int]:
        n = len(heights)

        # Go over all buildings from right to left and see which ones have ocean view
        answer = []
        max_height = float('-inf')
        for i in range(n-1, -1, -1):
            # See if this building has an ocean view
            if heights[i] > max_height:
                answer.append(i)
                max_height = heights[i]

        # Reverse list to make sure ordering is right
        return answer[::-1]

test_cases = [
    [[0,2,3], [4,2,3,1]],
    [[0,1,2,3], [4,3,2,1]],
    [[3], [1,3,2,4]]
]
solution = Solution()
for expected, heights in test_cases:
    actual = solution.findBuildings(heights)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: heights: {heights}")

print("Ran all tests")
