class Fancy:
    MOD = 10**9 + 7
    values: list
    additive: int
    multiplicative: int

    def __init__(self):
        self.values = []
        self.multiplicative = 1
        self.additive = 0

    # fast exponentiation
    def quickmul(self, x: int, y: int) -> int:
        return pow(x, y, self.MOD)

    # multiplicative inverse
    def inv(self, x: int) -> int:
        return self.quickmul(x, self.MOD - 2)

    # Append the value taking into account the additive and multiplicative
    # Time O(logm)
    def append(self, val: int) -> None:
        self.values.append((val - self.additive) * self.inv(self.multiplicative) % self.MOD)

    # Update purely the additive values
    # Time O(1)
    def addAll(self, inc: int) -> None:
        self.additive = (self.additive + inc) % self.MOD

    # Update the multiplicative and additive values
    # Time O(1)
    def multAll(self, m: int) -> None:
        self.multiplicative = self.multiplicative * m % self.MOD
        self.additive = self.additive * m % self.MOD

    # Time O(1)
    def getIndex(self, idx: int) -> int:
        # Make sure index has value
        if idx >= len(self.values):
            return -1

        # Compute and return the value
        return (self.multiplicative * self.values[idx] + self.additive) % self.MOD

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
