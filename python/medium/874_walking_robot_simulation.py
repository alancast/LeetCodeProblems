class Solution:
    CLOCKWISE = -1
    COUNTER_CLOCKWISE = -2

    # Fully do the simulation. Create a set of obstacles and make the moves
    # Time O(n)
    # Space O(o)
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # Create obstacle set
        obstacle_set = set()
        for x, y in obstacles:
            obstacle_set.add((x,y))

        # Set up variables
        answer = x = y = 0
        # What to add to x and y [N, W, S, E]
        dirs = [(0,1), (-1,0), (0,-1), (1,0)]
        dir_index = 0

        # Process each move
        for command in commands:
            if command == self.CLOCKWISE:
                dir_index -= 1
                if dir_index == -1:
                    dir_index = 3
            if command == self.COUNTER_CLOCKWISE:
                dir_index += 1
                if dir_index == 4:  # noqa: PLR2004
                    dir_index = 0

            # Make the moves
            x_add = dirs[dir_index][0]
            y_add = dirs[dir_index][1]
            for _ in range(command):
                next_x = x + x_add
                next_y = y + y_add

                # We can no longer go in that direction
                if (next_x, next_y) in obstacle_set:
                    break

                x = next_x
                y = next_y

            # See if new max
            answer = max(answer, (x*x) + (y*y))

        return answer

test_cases = [
    [25, [4, -1, 3], []],
    [65, [4,-1,4,-2,4], [[2,4]]],
    [36, [6,-1,-1,6], [[0,0]]]
]
solution = Solution()
for expected, commands, obstacles in test_cases:
    actual = solution.robotSim(commands, obstacles)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: commands: {commands}, obstacles: {obstacles}")

print("Ran all tests")
