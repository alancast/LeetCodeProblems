from collections import deque


# Use a deque and just count size
class HitCounter:
    _hit_queue: deque

    def __init__(self):
        self._hit_queue = deque()

    # Time O(1)
    def hit(self, timestamp: int) -> None:
        self._hit_queue.append(timestamp)
        
    # Purge old hits then return deque size
    def getHits(self, timestamp: int) -> int:
        while self._hit_queue and self._hit_queue[0] <= timestamp - 300:
            self._hit_queue.popleft()
        
        return len(self._hit_queue)
