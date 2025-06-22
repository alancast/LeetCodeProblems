from collections import deque
from typing import List


# Time O(d) as we go over full dishes and do O(1) operations on it
# Space O(k) as we store last k dishes eaten
def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    last_k_eaten_set = set()
    last_k_eaten_deque = deque()
    answer = 0
    for dish in D:
        # Already eaten so go to next dish
        if dish in last_k_eaten_set:
            continue

        # New dish to eat
        answer += 1
        last_k_eaten_deque.append(dish)
        last_k_eaten_set.add(dish)

        # See if need to remove from last k eaten
        if len(last_k_eaten_deque) > K:
            last_k_eaten_set.remove(last_k_eaten_deque.popleft())
     
    return answer

test_cases = [
    [5, 6, [1,2,3,3,2,1], 1],
    [4, 6, [1,2,3,3,2,1], 2],
    [2, 7, [1,2,2,2,1,2,1,2,1], 2],
    [2, 7, [1,2,1,2,1,2,1], 2]
]
for expected, N, D, K in test_cases:
    actual = getMaximumEatenDishCount(N, D, K)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: N: {N}, D: {D}, K: {K}")

print("Ran all tests")