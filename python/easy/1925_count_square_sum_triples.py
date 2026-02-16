class Solution:
    # Create set of all squares. Go over all pairs and see if third exists
    # Time O(n^2)
    # Space O(n)
    def countTriples(self, n: int) -> int:
        # Create a set of all squares from 1 to n
        squares = set()
        for i in range(1, n + 1):
            squares.add(i * i)

        # Go over all number combos and see if c is there
        answer = 0
        for i in range(1, n+1):
            for j in range(i + 1, n+1):
                target = (i*i) + (j*j)
                if target in squares:
                    # Add two because would also work if j and i are switched
                    answer += 2

        return answer

test_cases = [
    [2, 5],
    [4, 10]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.countTriples(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
