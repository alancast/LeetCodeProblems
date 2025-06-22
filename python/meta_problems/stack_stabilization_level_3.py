from typing import List


# Thorough explanation here
# https://github.com/justin-qu/Meta_Coding_Challenges/blob/main/Level%203/Stack_Stabilization_2.py
# Time O(n^2)
# Space O(N)
def getMinimumSecondsRequired(N: int, R: List[int], A: int, B: int) -> int:
    # Transform radii to simplify stability check (redefine problem)
    adjusted = [r - i for i, r in enumerate(R)]

    # Coordinate compression of all possible target radii
    # These are all the possible radii that the discs could be adjusted to
    key_radii = {max(1, r) for r in adjusted}
    key_radii = list(key_radii)
    key_radii.sort()

    cost_for_radius = [0] * len(key_radii)

    # For each disc, compute cost to adjust to each key radius
    # Pick a disk
    for r in adjusted:
        # Figure out it's cost for every single key radii
        for i, key_radius in enumerate(key_radii):
            delta = key_radius - r
            cost = 0
            
            # If we are inflating use A
            if delta > 0:
                cost = delta * A
            # Deflating use B
            else:
                cost = -delta * B
            
            # Update costs required to make change
            if i == 0:
                cost_for_radius[0] += cost
            else:
                cost_for_radius[i] = min(cost_for_radius[i-1], cost_for_radius[i] + cost)

    # All disks have been processed, so last value is final cost 
    return cost_for_radius[-1]

test_cases = [
    [5, 5, [2,5,3,6,5], 1, 1],
    [5, 3, [100, 100, 100], 2, 3],
    [9, 3, [100, 100, 100], 7, 3],
    [19, 4, [6,5,4,3], 10, 1],
    [207, 4, [100, 100, 1, 1], 2, 1]
]
for expected, N, R, A, B in test_cases:
    actual = getMinimumSecondsRequired(N, R, A, B)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: N: {N}, R: {R}, A: {A}, B: {B}")

print("Ran all tests")