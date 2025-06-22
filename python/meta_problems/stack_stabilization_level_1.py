from typing import List


# Time O(n) as we go through the disks once
# Space O(1)
def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    # Last disk simply must be biggest
    biggest_possible = R[-1] - 1
    answer = 0

    # Go backwards from second to last until the end
    for i in range(N-2, -1, -1):
        radius = R[i]

        # If this disk is too big we need to shrink it
        if radius > biggest_possible:
            answer += 1

        biggest_possible = min(biggest_possible - 1, radius - 1)

        # Can't deflate to 0 or below 0, so impossible
        if biggest_possible == -1:
            return -1

    return answer

test_cases = [
    [3, 5, [2,5,3,6,5]],
    [3, 5, [2,3,4,4,6]],
    [2, 3, [100, 100, 100]],
    [-1, 4, [6,5,4,3]]
]
for expected, N, R in test_cases:
    actual = getMinimumDeflatedDiscCount(N, R)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: N: {N}, R: {R}")

print("Ran all tests")