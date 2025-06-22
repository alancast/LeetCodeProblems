from typing import List


# Time O(n) as we just go through the full list of scores once
# Space O(1)
def getMinProblemCount(N: int, S: List[int]) -> int:
    num_two_points = num_one_points = 0

    for score in S:
        num_two_points = max(num_two_points, score//2)
        num_one_points = max(num_one_points, score % 2)
    
    return num_two_points + num_one_points

test_cases = [
    [4, 6, [1,2,3,4,5,6]],
    [4, 6, [1,2,3,4,6]],
    [3, 4, [4,3,3,4]],
    [4, 4, [2,4,6,8]]
]
for expected, N, S in test_cases:
    actual = getMinProblemCount(N, S)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: N: {N}, S: {S}")

print("Ran all tests")