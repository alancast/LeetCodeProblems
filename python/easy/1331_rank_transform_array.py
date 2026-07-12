class Solution:
    # Use ordered map and sort
    # Time O(nlogn)
    # Space O(n)
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # Store the rank for each number in arr
        num_to_indices = {k: [] for k in sorted(set(arr))}

        # Create num to indices mapping
        for i, num in enumerate(arr):
            num_to_indices[num].append(i)

        # Create the ranks
        rank = 1
        for num, _ in num_to_indices.items():
            for index in num_to_indices[num]:
                arr[index] = rank
            rank += 1

        return arr

test_cases = [
    [[4,1,2,3], [40,10,20,30]],
    [[1,1,1], [100,100,100]],
    [[5,3,4,2,8,6,7,1,3], [37,12,28,9,100,56,80,5,12]]
]
solution = Solution()
for expected, arr in test_cases:
    actual = solution.arrayRankTransform(arr)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: arr: {arr}")

print("Ran all tests")
