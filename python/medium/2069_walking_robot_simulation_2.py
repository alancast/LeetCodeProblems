# Observe that robot just moves in a loop around the edges
from typing import ClassVar


class Robot:
    # Only because when we reach starting point we could be facing two directions
    moved: bool
    # Where in the positions array we are
    idx: int
    # Just one long array of where we are in the loop
    pos: list[tuple[int,int]]
    # What direction are we facing
    dirs: list[int]

    TO_DIR_NAME: ClassVar[dict[int, str]] = {
        0: "East",
        1: "North",
        2: "West",
        3: "South",
    }

    def __init__(self, width: int, height: int):
        self.moved = False
        self.idx = 0
        self.pos = []
        self.dirs = []

        pos_ = self.pos
        dirs_ = self.dirs

        for i in range(width):
            pos_.append((i, 0))
            dirs_.append(0)
        for i in range(1, height):
            pos_.append((width - 1, i))
            dirs_.append(1)
        for i in range(width - 2, -1, -1):
            pos_.append((i, height - 1))
            dirs_.append(2)
        for i in range(height - 2, 0, -1):
            pos_.append((0, i))
            dirs_.append(3)

        # Direction set to south because that's how we got here
        dirs_[0] = 3

    # Time O(1)
    def step(self, num: int) -> None:
        self.moved = True
        self.idx = (self.idx + num) % len(self.pos)

    # Time O(1)
    def getPos(self) -> list[int]:
        return list(self.pos[self.idx])

    # Time O(1)
    def getDir(self) -> str:
        if not self.moved:
            return "East"

        return Robot.TO_DIR_NAME[self.dirs[self.idx]]


class RobotBad:
    max_height: int
    max_width: int
    dirs: list[tuple[int,int]]
    dir_words: list[str]
    dir_index: int
    x: int
    y: int

    def __init__(self, width: int, height: int):
        self.max_width = width
        self.max_height = height

        # What to add to x and y [E, N, W, S]
        self.dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        self.dir_words = ["East", "North", "West", "South"]

        # Initially facing east starting at 0, 0
        self.dir_index = 0
        self.x = 0
        self.y = 0

    # Time O(num)
    def step(self, num: int) -> None:
        for _ in range(num):
            # Make the moves
            next_x = self.x + self.dirs[self.dir_index][0]
            next_y = self.y + self.dirs[self.dir_index][1]

            # Make sure we are within bounds
            while next_x < 0 or next_x >= self.max_width or next_y < 0 or next_y >= self.max_height:
                # Rotate counterclockwise
                self.dir_index += 1
                if self.dir_index == 4:  # noqa: PLR2004
                    self.dir_index = 0

                # Compute next position
                next_x = self.x + self.dirs[self.dir_index][0]
                next_y = self.y + self.dirs[self.dir_index][1]

            self.x = next_x
            self.y = next_y

    # Time O(1)
    def getPos(self) -> list[int]:
        return [self.x, self.y]

    # Time O(1)
    def getDir(self) -> str:
        return self.dir_words[self.dir_index]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
