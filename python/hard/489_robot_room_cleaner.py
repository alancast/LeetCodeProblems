"""
This is the robot's control interface.
You should not implement it, or speculate about its implementation
"""
class Robot:
   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """

   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """

class Solution:
    # This was a tricky one. Keep a pattern, always turn right
    # When you visit something mark it as an obstacle
    # Backtrack until from every cell you've explored in all directions
    # Time O(m*n) as you just visit each cell a few times
    # Space O(m*n) to keep track of visited as well as the stack
    def cleanRoom(self, robot: Robot) -> None:
        # Turn around 180 degrees, move back one space, then turn back around
        def go_back() -> None:
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell, direction):
            # Clean this cell and mark it as marked
            visited.add(cell)
            robot.clean()

            # Go forward in all directions
            for i in range(4):
                new_d = (direction + i) % 4
                new_cell = (cell[0] + directions[new_d][0], cell[1] + directions[new_d][1])

                # Make sure the cell isn't visited and the robot can move there
                # If so move there and then come back
                if new_cell not in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()

                # Turn the robot right and go from there
                robot.turnRight()

        # 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # Set of visited cells
        visited = set()
        # Start from starting point and backtrack
        backtrack((0,0), 0)
