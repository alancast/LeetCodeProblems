# Dynamic programming, try moving each one and see which leads to better answer
# Time O(2^M) as it's possible each entry doubles the problem space
# Space O(2^M)
def getMinCodeEntryTime(N: int, M: int, C: list[int]) -> int:
    # Initialize the dp array with base case of moving the left dial
    # Initialize DP state: (left_pos, right_pos) → total time
    tree = {(C[0], 1): calculate_min_distance(1, C[0], N)}

    for target_digit in C[1:]:
        next_tree = {}

        for state, value in tree.items():
            # Option 1: use the left wheel to move to the digit
            left_state = (target_digit, state[1])
            left_distance = calculate_min_distance(state[0], target_digit, N)
            # Make sure we have min value for how to get to this state from all previous branches
            if left_state in next_tree:
                next_tree[left_state] = min(value + left_distance, next_tree[left_state])
            else:
                next_tree[left_state] = value + left_distance

            # Option 2: use the right wheel to move to the digit
            right_state = (state[0], target_digit)
            right_distance = calculate_min_distance(state[1], target_digit, N)
            # Make sure we have min value for how to get to this state from all previous branches
            if right_state in next_tree:
                next_tree[right_state] = min(value + right_distance, next_tree[right_state])
            else:
                next_tree[right_state] = value + right_distance

        # Purge values from previous iteration, and set them to the new one
        tree = next_tree

    # We have gotten to the final key, so just return min value for how to get there
    return min(tree.values())

# Calculates the min distance to rotate to a given digit
def calculate_min_distance(target_digit: int, previous: int, size: int) -> int:
    direct = abs(target_digit - previous)
    wraparound = size - direct
    return min(direct, wraparound)

test_cases = [
    [2, 3, 3, [1,2,3]],
    [6, 10, 4, [9,4,4,8]]
]
for expected, N, M, C in test_cases:
    actual = getMinCodeEntryTime(N, M, C)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: N: {N}, M: {M}, C: {C}")

print("Ran all tests")
