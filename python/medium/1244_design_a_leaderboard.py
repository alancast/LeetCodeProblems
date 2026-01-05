from collections import defaultdict
from heapq import heappop, heappush

class Leaderboard:
    _score_map: defaultdict

    def __init__(self):
        self._score_map = defaultdict(int)

    # Time O(1)
    def addScore(self, playerId: int, score: int) -> None:
        # Since using default dict if not in there just makes 0 
        self._score_map[playerId] += score
        
    # Time O(n log k)
    # Can do in O(K) time if we make the other functions O(logn)
    def top(self, K: int) -> int:
        min_heap = []

        # Get top K scores in heap
        for x in self._score_map.values():
            heappush(min_heap, x)

            # Pops smallest (so outside top k)
            if len(min_heap) > K:
                heappop(min_heap)

        return sum(min_heap)

    # Time O(1)
    def reset(self, playerId: int) -> None:
        del self._score_map[playerId]
