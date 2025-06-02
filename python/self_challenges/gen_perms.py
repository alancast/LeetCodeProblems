from collections import deque
from typing import List


# Generate all permutations using a stack (DFS) and a queue (BFS)
# Time Complexity: O(n! * n) for both stack (DFS) and queue (BFS) approaches, where n is the length of nums.
#   - There are n! permutations, and each permutation is constructed in O(n) time.
# Space Complexity: O(n! * n) for storing all permutations in the call stack/queue at peak, plus O(n) for each permutation being built.
#   - The stack or queue can hold up to O(n! * n) elements in the worst case.
def gen_perms(nums: List[int]) -> None:
    print('Permutations using stack (DFS):')
    stack = [([], nums)]  # (current_perm, remaining)
    while stack:
        curr_perm, remaining = stack.pop()
        if not remaining:
            print(curr_perm)
        else:
            for i in range(len(remaining)):
                stack.append((curr_perm + [remaining[i]], remaining[:i] + remaining[i+1:]))

    print('\nPermutations using queue (BFS):')
    queue = deque([([], nums)])
    while queue:
        curr_perm, remaining = queue.popleft()
        if not remaining:
            print(curr_perm)
        else:
            for i in range(len(remaining)):
                queue.append((curr_perm + [remaining[i]], remaining[:i] + remaining[i+1:]))

gen_perms([1,2,3])