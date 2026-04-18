class Solution:
    BIG_INT = 39393939393939

    # Space optimized DP
    # Bottom up DP, but all we cared about with that was previous row
    # So space optimized to only keep that
    # Go in reverse order of robots deciding whether to place or skip at each factory
    # Go in reverse order of factory as well
    # Time Oy(n^2 * f)
    # Space O(f)
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        # Sort robot and factory by position
        robot.sort()
        factory.sort()

        # Flatten factory positions according to their capacities
        # E.g. if a factory has a capacity of 3, put it in there 3 times
        factory_positions = []
        for fact in factory:
            for _ in range(fact[1]):
                factory_positions.append(fact[0])

        robot_count = len(robot)
        factory_count = len(factory_positions)

        # The two rows we care about for DP
        # Current is the current state we are filling
        # Next holds the results from the previous iteration
        next_dist = [0 for _ in range(factory_count + 1)]
        current = [0 for _ in range(factory_count + 1)]

        # Set final factory to massively large int in case we never place robot
        # This makes sure all robots get placed
        current[factory_count] = self.BIG_INT

        # Fill DP table using two rows for optimization
        # Go over all robots (from end to start)
        for r in range(robot_count - 1, -1, -1):
            # Go over all factories (from end to start)
            for f in range(factory_count - 1, -1, -1):
                # Distance if assigning current robot to current factory
                # Distance to this factory + bump previous robot to different factory
                assign = (abs(robot[r] - factory_positions[f]) + next_dist[f + 1])

                # Distance if current factory is skipped for this robot
                skip = current[f + 1]
                # Take the minimum option
                current[f] = min(assign, skip)

            # Move to next robot
            next_dist = current[:]

        # Return minimum distance starting from the first robot
        return current[0]

test_cases = [
    [4, [0,4,6], [[2,2],[6,2]]],
    [2, [1,-1], [[-2,1],[2,1]]]
]
solution = Solution()
for expected, robot, factory in test_cases:
    actual = solution.minimumTotalDistance(robot, factory)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: robot: {robot}, factory: {factory}")

print("Ran all tests")

