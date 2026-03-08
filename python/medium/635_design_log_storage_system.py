from bisect import bisect_left, bisect_right
from collections import defaultdict


class LogSystem:
    sorted_timestamps: list
    timestamp_to_ids: dict

    def __init__(self):
        self.sorted_timestamps = []
        self.timestamp_to_ids = defaultdict(set)

    # Time O(logn)
    def put(self, id: int, timestamp: str) -> None:
        # Figure out where timestamp belongs in sorted array
        idx = bisect_left(self.sorted_timestamps, timestamp)

        # Put timestamp in correct spot in array
        if idx == len(self.sorted_timestamps):
            self.sorted_timestamps.append(timestamp)
        else:
            self.sorted_timestamps.insert(idx, timestamp)

        # Store the timestamp to ID mapping
        self.timestamp_to_ids[timestamp].add(id)

    # Time O(logn)
    def retrieve(self, start: str, end: str, granularity: str) -> list[int]:
        # Create start and end indexes based on granularity
        if granularity == 'Year':
            start = start[:4] + ':01:01:00:00:00'
            end = end[:4] + ':12:31:23:59:59'
        elif granularity == 'Month':
            start = start[:7] + ':01:00:00:00'
            end = end[:7] + ':31:23:59:59'
        elif granularity == 'Day':
            start = start[:10] + ':00:00:00'
            end = end[:10] + ':23:59:59'
        elif granularity == 'Hour':
            start = start[:13] + ':00:00'
            end = end[:13] + ':59:59'
        elif granularity == 'Minute':
            start = start[:16] + ':00'
            end = end[:16] + ':59'

        # Take start and end index and get all the ID's
        start_idx = bisect_left(self.sorted_timestamps, start)
        end_idx = bisect_right(self.sorted_timestamps, end)
        ids = set()
        # Make sure to stay in bounds with end checking
        for i in range(start_idx, min(len(self.sorted_timestamps), end_idx)):
            # Add all ids from this timestamp
            ids = ids.union(self.timestamp_to_ids[self.sorted_timestamps[i]])

        return list(ids)


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
