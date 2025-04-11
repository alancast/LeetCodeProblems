class Solution:
    # Time O(n) where n is range between low and high
    # Space O(1) no extra space
    def countSymmetricIntegers_brute_force(self, low: int, high: int) -> int:
        self.validate_inputs(low, high)

        symmetric_ints = 0
        for i in range(low, high + 1):
            # 3 digit numbers can be ignored
            if i >= 100 and i < 1000:
                continue

            # 2 digit number just needs first to equal last
            if i < 100:
                if i // 10 == i % 10:
                    symmetric_ints += 1
            # 4 digit number see if ones plus tens equals hundreds plus thousands
            elif i >= 1000:
                ones = i % 10
                tens = ((i // 10) % 10)
                hundreds = ((i // 100) % 10)
                thousands = i // 1000
                if (hundreds + thousands) == (ones + tens):
                    symmetric_ints += 1

        return symmetric_ints
    
    def validate_inputs(self, low: int, high: int) -> None:
        if low < 1 or low > 10000:
            raise ValueError("low must be between 1 and 10000")
        if high < 1 or high > 10000:
            raise ValueError("high must be between 1 and 10000")
        if high < low:
            raise ValueError("high must be less than low")
    
test_cases = [
    [9, 1, 100],
    [1, 1000, 1001],
    [1, 1001, 1002],
    [4, 1200, 1230]
]
solution = Solution()
for expected, low, high in test_cases:
    actual = solution.countSymmetricIntegers_brute_force(low, high)
    if actual != expected:
        print(f"TEST FAILED! Expected {expected} but got {actual}")
        print(f"\tINPUTS: low: {low}, high: {high}")