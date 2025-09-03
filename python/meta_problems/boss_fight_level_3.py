from typing import List

# Compute damage each warrior applies
# Pick a warrior then pick the best one to pair them with
# If that is better than previous result, use the paired warrior as next one
# And see if they can form a better pair, keep going until there isn't a better pair found
# Time O(n^2) though worst case this is n^2, in practice it will only take a few iterations
# Space O(n) for storing damage amount
def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
    # Precompute H{i}*D{i} for each warrior {i}
    warrior_damage_seconds = [0] * N
    for i in range(N):
        warrior_damage_seconds[i] = H[i] * D[i]

    max_damage = 0
    # Pick initial best warrior at random
    best_warrior = 0

    # Keep running until the new pair isn't better than the previous pair
    run = True
    while run:
        run = False
        next_best_warrior = 0

        # Go over all potential warriors to pair with to find best one
        for i in range(N):
            # Can't pair with self
            if i == best_warrior:
                continue

            # Must include damage done from second in line
            pair_damage = (
                warrior_damage_seconds[best_warrior]
                + warrior_damage_seconds[i]
                # Which one is better to have in front/behind
                + max(
                    H[best_warrior] * D[i],
                    H[i] * D[best_warrior]
                )
            )

            # We found a pair that does more damage than previous pairing
            if pair_damage > max_damage:
                run = True
                max_damage = pair_damage
                next_best_warrior = i

        best_warrior = next_best_warrior

    # Normalize for time based on how much damage boss does
    return round(max_damage / B, 6)

# Go over all possible pairs and compute how much damage, keep max
# Time O(n^2)
# Space O(1)
def getMaxDamageDealt_brute_force(N: int, H: List[int], D: List[int], B: int) -> float:
    max_damage = 0.0

    # Cycle through first warrior
    for i in range(N):
        first_warrior_survival_time = round(H[i] / B, 6)
        first_warrior_damage = round(first_warrior_survival_time * D[i], 6)

        # Cycle through second warrior
        for j in range(N):
            # Not valid to be paired with self
            if j == i:
                continue

            second_warrior_survival_time = round(H[j] / B, 6)
            second_warrior_damage = (first_warrior_survival_time + second_warrior_survival_time) * D[j]
            second_warrior_damage = round(second_warrior_damage, 6)

            max_damage = max(max_damage, first_warrior_damage + second_warrior_damage)

    return max_damage

test_cases = [
    [6.500000, 3, [2,1,4], [3,1,2], 4],
    [62.750000, 4, [1,1,2,100], [1,2,1,3], 8],
    [62.750000, 4, [1,1,2,3], [1,2,1,100], 8]
]
for expected, N, H, D, B in test_cases:
    actual = getMaxDamageDealt(N, H, D, B)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: N: {N}, H: {H}, D: {D}, B: {B}")

print("Ran all tests")