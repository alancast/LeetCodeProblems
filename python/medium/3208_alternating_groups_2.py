from typing import List


class Solution:
    # Same exact logic as below but removes modulo as that's an expensive thing
    # Time O(n + k) as we loop over colors n once then an extra k
    # Space O(1)
    def numberOfAlternatingGroups_two_pass(self, colors: List[int], k: int) -> int:
        n = len(colors)

        num_groups = 0
        alternating_colors = 1
        last_color = colors[0]
        for i in range(1, n):
            # Same color so restart
            if colors[i] == last_color:
                alternating_colors = 1
                continue

            alternating_colors += 1
            last_color = colors[i]
            
            if alternating_colors >= k:
                num_groups += 1

        # Loop around to include first k
        for i in range(k-1):
            # Same color and already looped around, so just end
            if colors[i] == last_color:
                break

            alternating_colors += 1
            last_color = colors[i]
            
            if alternating_colors >= k:
                num_groups += 1

        return num_groups
    
    # Time O(n + k) as we just loop over colors once
    # Space O(1)
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)

        num_groups = left = streak = 0
        while left < n:
            while streak < k - 1:
                # Alternating colors
                if colors[(left+streak)%n] != colors[(left+streak + 1)%n]:
                    streak += 1
                # Same color, so restart search from new left
                else:
                    left += streak
                    streak = 0
                    break

            # We have an alternating group, so count it and move left forward
            if streak == k - 1:
                num_groups += 1
                streak -= 1
            
            left += 1

        return num_groups
    
test_cases = [
    [3, [0,1,0,1,0], 3],
    [0, [0,0,0,0,0], 3],
    [2, [0,1,0,0,1,0,1], 6]
]
solution = Solution()
for expected, colors, k in test_cases:
    actual = solution.numberOfAlternatingGroups_two_pass(colors, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: colors: {colors}, k: {k}")

print("Ran all tests")