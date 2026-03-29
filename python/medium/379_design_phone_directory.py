# Max space would be O(n)
class PhoneDirectory:
    _freed: set
    _used: int
    _max: int

    # Time O(1)
    def __init__(self, maxNumbers: int):
        self._freed = set()
        self._used = 0
        self._max = maxNumbers

    # Time O(1)
    def get(self) -> int:
        # Give out an already freed up on
        if self._freed:
            return self._freed.pop()

        # Give out next highest number
        if self._used < self._max:
            self._used += 1
            return self._used - 1

        # No available numbers
        return -1

    # Time O(1)
    def check(self, number: int) -> bool:
        # See if it's in freed set or not yet used
        return bool(number in self._freed or number >= self._used)

    # Time O(1)
    def release(self, number: int) -> None:
        # Make sure the number is used at all
        if number >= self._used or number in self._freed:
            return

        # Free up the number
        self._freed.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
