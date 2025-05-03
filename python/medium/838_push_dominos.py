class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        return self._push_dominoes_three_pass(dominoes)

    # See if entry is closer to left or right falling domino
    # Time O(n) as we go through dominoes 3 times
    # Space O(n) as we keep an n size array for from left and right
    def _push_dominoes_three_pass(self, dominoes: str) -> str:
        n = len(dominoes)
        final_str = []
        # How far is this index from a L or R that could impact it
        from_left = [float('inf')] * n
        from_right = [float('inf')] * n

        # populate from_right
        distance = 0
        counting = False
        for i in range(n):
            char = dominoes[i]
            if char == 'R':
                from_right[i] = distance = 0
                counting = True
            elif char == 'L':
                from_right[i] = distance = 0
                # From the right of here will never fall Right due to this
                counting = False
            elif counting:
                distance += 1
                from_right[i] = distance

        # populate from_left
        distance = 0
        counting = False
        for i in range(n-1, -1, -1):
            char = dominoes[i]
            if char == 'L':
                from_left[i] = distance = 0
                counting = True
            elif char == 'R':
                from_left[i] = distance = 0
                # From the left of here will never fall left due to this
                counting = False
            elif counting:
                distance += 1
                from_left[i] = distance

        # Create string
        for i in range(n):
            char = dominoes[i]
            if char == 'L' or char == 'R':
                final_str.append(char)
            else:
                if from_left[i] < from_right[i]:
                    final_str.append('L')
                elif from_right[i] < from_left[i]:
                    final_str.append('R')
                else:
                    final_str.append('.')

        return ''.join(final_str)

    # Time O(n^2) as we could go through dominoes n times
    # Space O(1) as we take up no extra space other than the answer string
    def _push_dominoes_iterative(self, dominoes: str) -> str:
        n = len(dominoes)
        changed = True
        next_dominoes = []
        while changed:
            changed = False
            # Go through the string and see if standing dominoes fall
            for i in range(n):
                if dominoes[i] == 'L' or dominoes[i] == 'R':
                    next_dominoes.append(dominoes[i])
                # Standing domino so check what's around it
                else:
                    next_char = '.'
                    # Check if it will be pushed right
                    if i - 1 >= 0 and dominoes[i-1] == 'R':
                        next_char = 'R'
                    # Check if it will be pushed left
                    if i + 1 < n and dominoes[i+1] == 'L':
                        # Make sure it's not being pushed left and right
                        if next_char == 'R':
                            next_char = '.'
                        else:
                            next_char = 'L'

                    if next_char != '.':
                        changed = True

                    # Append the new char
                    next_dominoes.append(next_char)

            dominoes = ''.join(next_dominoes)
            next_dominoes.clear()

        return dominoes
    
test_cases = [
    ["LLL.", "LLL."],
    ["RR.L", "RR.L"],
    ["RRLL", "R..L"],
    ["LL.RR.LLRRLL..", ".L.R...LR..L.."]
]
solution = Solution()
for expected, dominoes in test_cases:
    actual = solution.pushDominoes(dominoes)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: dominoes: {dominoes}")

print("Ran all tests")