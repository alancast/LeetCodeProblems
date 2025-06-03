from collections import deque
from typing import List


class Solution:
    # Time O(n) as we process each box once
    # Space O(n) as worst case all boxes are contained in box so queue is size n
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int]
    ) -> int:
        n = len(status)

        # Boxes we've attempted to open since we last could
        # This is to avoid infinite loop of not having keys
        boxes_attempted_since_opening = 0
        boxes_to_open = deque()
        answer = 0

        # Add to queue all the initial boxes to open
        for box in initialBoxes:
            boxes_to_open.append(box)

        while boxes_to_open:
            box_processing = boxes_to_open.popleft()
            boxes_attempted_since_opening += 1

            # See if we can get into the box
            if status[box_processing] == 1:
                # We have opened a box so reset this
                boxes_attempted_since_opening = 0

                # Notate box is opened and candies added
                answer += candies[box_processing]
                candies[box_processing] = 0

                # Add any keys it gives us access to now
                for contained_key in keys[box_processing]:
                    status[contained_key] = 1

                # Add any new boxes it gives us access to now
                for contained_box in containedBoxes[box_processing]:
                    boxes_to_open.append(contained_box)
            # Couldn't get in, so re-add it to the queue if we get the key later
            # This will infinite loop though, so need a solution to that
            else:
                boxes_to_open.append(box_processing)

            # We have tried to open all the boxes in the queue and can't
            # This won't change so get out of infinite loop
            if boxes_attempted_since_opening == len(boxes_to_open):
                break

        return answer
    
test_cases = [
    [16, [1,0,1,0], [7,5,4,100], [[],[],[1],[]], [[1,2],[3],[],[]], [0]],
    [6, [1,0,0,0,0,0], [1,1,1,1,1,1], [[1,2,3,4,5],[],[],[],[],[]], [[1,2,3,4,5],[],[],[],[],[]], [0]]
]
solution = Solution()
for expected, status, candies, keys, containedBoxes, initialBoxes in test_cases:
    actual = solution.maxCandies(status, candies, keys, containedBoxes, initialBoxes)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: status: {status}, candies: {candies}, keys: {keys}, containedBoxes: {containedBoxes}")

print("Ran all tests")