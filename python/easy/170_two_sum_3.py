class TwoSum:

    def __init__(self) -> None:
        self.num_counts = {}

    def add(self, number: int) -> None:
        if number in self.num_counts:
            self.num_counts[number] += 1
        else:
            self.num_counts[number] = 1

    def find(self, value: int) -> bool:
        # Go through all keys and see if other half is there
        for num in self.num_counts:
            needed = value - num
            if num != needed:
                if needed in self.num_counts:
                    return True
            elif self.num_counts[num] > 1:
                return True

        return False
