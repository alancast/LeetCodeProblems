from collections import deque
from typing import List


# Keep a a deque and set of the snake body
# And make computations based off that
class SnakeGame:
    movement = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
    snake: deque
    snake_set: dict
    width: int
    height: int
    food_index: int
    food_queue: List[List[int]]

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = deque([(0,0)])
        self.snake_set = {(0,0) : 1}
        self.width = width
        self.height = height
        self.food_queue = food
        self.food_index = 0

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        
        newHead = (self.snake[0][0] + self.movement[direction][0],
                   self.snake[0][1] + self.movement[direction][1])
        
        # Boundary conditions.
        crosses_boundary1 = newHead[0] < 0 or newHead[0] >= self.height
        crosses_boundary2 = newHead[1] < 0 or newHead[1] >= self.width
        
        # Checking if the snake bites itself and isn't the tail
        bites_itself = newHead in self.snake_set and newHead != self.snake[-1]
     
        # If any of the terminal conditions are satisfied, then we exit with rcode -1.
        if crosses_boundary1 or crosses_boundary2 or bites_itself:
            return -1

        # Note the food list could be empty at this point.
        next_food_item = self.food_queue[self.food_index] if self.food_index < len(self.food_queue) else None
        
        # Either eat food or remove tail
        if self.food_index < len(self.food_queue) and \
            next_food_item[0] == newHead[0] and \
                next_food_item[1] == newHead[1]:
            self.food_index += 1
        else:              
            tail = self.snake.pop()  
            del self.snake_set[tail]
            
        # A new head always gets added
        self.snake.appendleft(newHead)
        
        # Also add the head to the set
        self.snake_set[newHead] = 1

        return len(self.snake) - 1

# Keeps the full grid in memory
class SnakeGameBigMemoryUsage:
    # 0 means open space
    # 1 means food there
    # 2 means snake moving up
    # 3 means snake moving right
    # 4 means snake moving down
    # 5 means snake moving left
    grid: List[List[int]]
    head_x: int
    head_y: int
    tail_x: int
    tail_y: int
    food_queue: List[List[int]]
    score: int

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.head_x = self.head_y = self.tail_x = self.tail_y = self.score = 0

        # Put in reverse order so popping is faster
        self.food_queue = []
        for i in range(len(food) - 1, -1, -1):
            coordinates = food[i]
            self.food_queue.append(coordinates)

        # Put first food down (assume it's not 0,0 but in real life check)
        self._add_next_food()

    def move(self, direction: str) -> int:
        # Figure out what next square is
        next_x = self.head_x
        next_y = self.head_y
        move_value = 0
        if direction == 'R':
            next_x += 1
            move_value = 3
        elif direction == 'L':
            next_x -= 1
            move_value = 5
        elif direction == 'U':
            next_y -= 1
            move_value = 2
        else:
            next_y += 1
            move_value = 4

        # See if it's a valid square, if not return -1
        if next_x < 0 or next_x >= len(self.grid[0]):
            return -1
        if next_y < 0 or next_y >= len(self.grid):
            return -1
        # Snake is already there and it's not the tail
        if self.grid[next_y][next_x] > 1 and not \
            (self.tail_x == next_x and self.tail_y == next_y):
            return -1

        # It is a valid square, so update grid and compute score
        # Update head
        self.grid[self.head_y][self.head_x] = move_value
        self.head_x = next_x
        self.head_y = next_y
        # Check if next space is food and update tail and score accordingly
        need_to_add_food = False
        if self.grid[next_y][next_x] == 1:
            self.score += 1
            need_to_add_food = True
        else:
            # See what direction tail is moving
            tail_value = self.grid[self.tail_y][self.tail_x]
            next_tail_x = self.tail_x
            next_tail_y = self.tail_y
            if tail_value == 2:
                next_tail_y -= 1
            elif tail_value == 3:
                next_tail_x += 1
            elif tail_value == 4:
                next_tail_y += 1
            else:
                next_tail_x -= 1
            
            # Make old tali value now free space
            self.grid[self.tail_y][self.tail_x] = 0
            # Set new tail coordinates
            self.tail_x = next_tail_x
            self.tail_y = next_tail_y

        # Add food as final thing
        if need_to_add_food:
            self._add_next_food()

        return self.score
    
    def _add_next_food(self) -> None:
        for i in range(len(self.food_queue) - 1, -1, -1):
            coordinates = self.food_queue[i]
            if self.grid[coordinates[0]][coordinates[1]] == 0:
                self.grid[coordinates[0]][coordinates[1]] = 1
                self.food_queue.pop(i)
                break
