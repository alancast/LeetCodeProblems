from collections import Counter, defaultdict


class FreqStack:

    def __init__(self):
        # Frequencies of each item
        self.frequencies = Counter()
        # Key is frequency count, value is list of values with that frequency
        self.values_at_frequency = defaultdict(list)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        # Update count for this element
        new_frequency = self.frequencies[val] + 1
        self.frequencies[val] = new_frequency

        # Check if element is new leader
        if new_frequency > self.maxfreq:
            self.maxfreq = new_frequency
        
        # Add value to list of values with this frequency
        self.values_at_frequency[new_frequency].append(val)

    def pop(self) -> int:
        # Pop most frequent item and decrement it's frequency count
        x = self.values_at_frequency[self.maxfreq].pop()
        self.frequencies[x] -= 1

        # See if any other items left at max freq after pop
        # If not decrement last freq count
        if not self.values_at_frequency[self.maxfreq]:
            self.maxfreq -= 1

        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()