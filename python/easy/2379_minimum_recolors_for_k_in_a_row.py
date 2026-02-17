class Solution:
    # Sliding window and just return min number of W
    # Time O(n) as we go through all blocks once
    # Space O(1)
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)

        # Create sliding window
        w_count = 0
        for i in range(k):
            char = blocks[i]
            if char == 'W':
                w_count += 1

        answer = w_count
        # Move sliding window and find min
        for i in range(k, n):
            first_char = blocks[i-k]
            if first_char == 'W':
                w_count -= 1

            char = blocks[i]
            if char == 'W':
                w_count += 1

            answer = min(answer, w_count)

        return answer

test_cases = [
    [3, "WBBWWBBWBW", 7],
    [1, "WBB", 3],
    [0, "WBB", 1],
    [0, "WBWBBBW", 2]
]
solution = Solution()
for expected, blocks, k in test_cases:
    actual = solution.minimumRecolors(blocks, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: blocks: {blocks}, k: {k}")

print("Ran all tests")
