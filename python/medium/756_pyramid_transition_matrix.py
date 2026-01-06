from collections import defaultdict
from typing import List


class Solution:
    # Inverse DFS, starting from bottom and see if it's possible to get to top
    # Somewhat confusing, very hard for a medium
    # Time O(A^n) where n is length of bottom and A is alphabet size
    # Space O(n^2)
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Create a dictionary of for this left and right, what can be on top
        tab = defaultdict(set)
        for left, right, top in allowed:
            tab[left, right].add(top)

        def add_neighbor(node: str) -> List[str]:
            neighbor = ['']

            # Go over all bottom pairs and see who can be on top
            for i in range(1, len(node)):
                tops = tab[(node[i - 1], node[i])]
                if tops:
                    neighbor = [a + e for e in tops for a in neighbor]
                else:
                    return []

            return neighbor
        
        visited = set()

        def dfs(node: str) -> bool:
            # If we got to the top then we pass
            if len(node) == 1:
                return True
            
            # If we have already seen this node and didn't get to top, fail
            if node in visited:
                return False

            for next in add_neighbor(node):
                if dfs(next):
                    return True

            visited.add(node)
            return False

        return dfs(bottom)

test_cases = [
    [True, "BCD", ["BCC","CDE","CEA","FFF"]],
    [False, "AAAA", ["AAB","AAC","BCD","BBE","DEF"]]
]
solution = Solution()
for expected, bottom, allowed in test_cases:
    actual = solution.pyramidTransition(bottom, allowed)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: bottom: {bottom}, allowed: {allowed}")

print("Ran all tests")