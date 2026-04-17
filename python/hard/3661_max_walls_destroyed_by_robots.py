class Solution:
    # Sort robots, then iterate pointer to see which walls it can attack
    # Time O(nlogn + wlogw)
    # Space O(n + w)
    def maxWalls(self, robots: list[int], distance: list[int], walls: list[int]) -> int:  # noqa: PLR0912
        n = len(robots)

        # Sort robots and their distance by which robot comes first
        robot_dist = list(zip(robots, distance, strict=True))
        robot_dist.sort(key=lambda x: x[0])
        # Sort walls by order as well
        walls.sort()

        w = len(walls)
        right_ptr = left_ptr = curr_ptr = robot_ptr = 0

        prev_right = 0
        sub_left = sub_right = 0

        # Go over each robot
        for i in range(n):
            robot_pos, robot_dist_val = robot_dist[i]

            # Index of the first wall to the right of this robot
            while right_ptr < w and walls[right_ptr] <= robot_pos:
                right_ptr += 1
            pos_1 = right_ptr

            # Index of the first wall this robot would shoot if shooting right
            # Only differs from pos1 if the robot is on a wall
            while curr_ptr < w and walls[curr_ptr] < robot_pos:
                curr_ptr += 1
            pos_2 = curr_ptr

            # What index left can this robot shoot to
            if i >= 1:
                # Whichever is bigger, distance limited or robot to left limited
                left_bound = max(robot_pos - robot_dist_val, robot_dist[i-1][0] + 1)
            else:
                left_bound = robot_pos - robot_dist_val

            # Find the index of leftmost wall this robot can shoot
            while left_ptr < w and walls[left_ptr] < left_bound:
                left_ptr += 1
            left_pos = left_ptr
            # How many walls would be destroyed if we shoot left
            current_left = pos_1 - left_pos

            # Which index right can this robot shoot to
            if i < n - 1:
                # Whichever is smaller, distance limited or robot to right limited
                right_bound = min(robot_pos + robot_dist_val, robot_dist[i+1][0] - 1)
            else:
                right_bound = robot_pos + robot_dist_val

            # Find the index of the first wall to the right of the robot that can not be shot
            while right_ptr < w and walls[right_ptr] <= right_bound:
                right_ptr += 1
            right_pos = right_ptr
            # How many walls would be destroyed if we shoot right
            current_right = right_pos - pos_2

            current_num = 0
            if i > 0:
                # Find the index of the first wall to the right of the previous robot
                while robot_ptr < w and walls[robot_ptr] < robot_dist[i-1][0]:
                    robot_ptr += 1
                pos3 = robot_ptr
                current_num = pos_1 - pos3

            # Figure out which way to shoot
            if i == 0:
                sub_left = current_left
                sub_right = current_right
            else:
                new_sub_left = max(
                    sub_left + current_left,
                    sub_right
                    - prev_right
                    + min(current_left + prev_right, current_num),
                )
                new_sub_right = max(
                    sub_left + current_right, sub_right + current_right
                )
                sub_left = new_sub_left
                sub_right = new_sub_right

            prev_right = current_right

        return max(sub_left, sub_right)

test_cases = [
    [1, [4], [3], [1,10]],
    [3, [10,2], [5,1], [5,2,7]],
    [0, [1,2], [100,1], [10]]
]
solution = Solution()
for expected, robots, distance, walls in test_cases:
    actual = solution.maxWalls(robots, distance, walls)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: robots: {robots}, distance: {distance}, walls: {walls}")

print("Ran all tests")
