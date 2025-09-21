from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from typing import List


class Router:
    memory_limit: int
    # set of packets ([source, destination, timestamp])
    packet_set: set
    # FIFO order of packets
    packet_queue: deque
    # Map of destination to sorted list of timestamps
    packet_counts: defaultdict
    
    
    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.packet_set = set()
        self.packet_counts = defaultdict(list)
        self.packet_queue = deque()

    # Time O(1)
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)

        # Duplicate check
        if key in self.packet_set:
            return False

        # If memory full, forward oldest packet
        if len(self.packet_set) >= self.memory_limit:
            self.forwardPacket()

        # Add packet
        self.packet_set.add(key)
        self.packet_queue.append(key)
        self.packet_counts[destination].append(timestamp)

        return True

    # Time O(1)
    def forwardPacket(self) -> List[int]:
        # If no packets return nothing
        if not self.packet_set:
            return []

        # Get oldest packet
        key = self.packet_queue.popleft()
        self.packet_set.remove(key)

        # Remove this packet from the destination map
        self.packet_counts[key[1]].pop(0)

        return key

    # Time O(logn)
    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.packet_counts[destination]
        if not timestamps:
            return 0

        # Binary search for range
        left = bisect_left(timestamps, startTime)
        right = bisect_right(timestamps, endTime)

        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
