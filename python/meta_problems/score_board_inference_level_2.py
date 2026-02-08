# Time O(n) as we just go through the full list of scores once
# Space O(1)
def getMinProblemCount(N: int, S: list[int]) -> int:
    one_remainder_there = two_remainder_there = max_score = second_max_score = 0
    one_there = False

    # Find top 2 max scores
    # see if there is a remainder of 1 and 2 ever present and see if 1 is present
    for score in S:
        if score % 3 == 1:
            if score == 1:
                one_there = True
            one_remainder_there = 1
        elif score % 3 == 2:
            two_remainder_there = 1

        if score > max_score:
            second_max_score = max_score
            max_score = score
        elif score != max_score and score > second_max_score:
            second_max_score = score

    threes = max_score//3

    if max_score % 3 == 0:
        # See if there are remainders that force us into using a non 3
        if one_remainder_there > 0 or two_remainder_there > 0:
            return threes + 1

        return threes

    # Shortcut to remove a question (otherwise logic is what's below)
    # If we don't have 1 or max_score - 1 in S, we can replace one 3 with 2 of 2
    if max_score % 3 == 1 and not one_there and second_max_score != max_score - 1:
        return threes + 1

    # Num questions is 3s plus a 1 and a 2 point question (unless can shortcut above)
    return threes + one_remainder_there + two_remainder_there

test_cases = [
    [3, 6, [1,2,3,4,5,6]],
    [3, 6, [1,2,3,4,6]],
    [2, 4, [4,3,3,4]],
    [4, 4, [2,4,6,8]],
    [3, 1, [8]]
]
for expected, N, S in test_cases:
    actual = getMinProblemCount(N, S)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: N: {N}, S: {S}")

print("Ran all tests")
