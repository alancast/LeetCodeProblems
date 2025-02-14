# This implementation is just the better efficient version
class ProductOfNumbersEfficient:

    def __init__(self):
        self.products = []
        self.product = 1

    # Time O(1)
    def add(self, num: int) -> None:
        # Clear everything as 0 * anything is 0
        if num == 0:
            self.product = 1
            self.products = []
        else:
            self.product *= num
            self.products.append(self.product)
        
    # Time O(1)
    def getProduct(self, k: int) -> int:
        # Make sure to handle cases for if a 0 was added
        if len(self.products) == 0 or k > len(self.products):
            return 0
        
        # Do the math for the product, write it out on paper if you need an example
        if k == len(self.products):
            return self.product
        else:
            return self.products[-1] // self.products[-(k+1)]

# This implementation takes up more space but lazily computes product efficiently
class ProductOfNumbersLazy:

    def __init__(self):
        self.nums = []
        self.products = []
        self.last_k_computed = 0

    # Time O(1)
    def add(self, num: int) -> None:
        self.nums.append(num)
        self.products.append(num)
        self.last_k_computed = 0
        
    # Time O(k)
    def getProduct(self, k: int) -> int:
        # Already computed
        if k < self.last_k_computed:
            return self.products[-k]
        
        # Need to compute but see if we can start ahead
        if self.last_k_computed != 0:
            for i in range(self.last_k_computed + 1, k + 1):
                self.products[-i] = self.nums[-i] * self.products[-(i-1)]
        # Can't take any optimizations, just do the calculations
        else:
            for i in range(2, k + 1):
                self.products[-i] = self.nums[-i] * self.products[-(i-1)]

        self.last_k_computed = k
        return self.products[-k]

# This implementation prioritizes speed of add
class ProductOfNumbersAdd:

    def __init__(self):
        self.nums = []

    # Time O(1)
    def add(self, num: int) -> None:
        self.nums.append(num)
        
    # Time O(k)
    def getProduct(self, k: int) -> int:
        product = 1
        for i in range(1, k + 1):
            product *= self.nums[-i]

        return product

# This implementation prioritizes speed of getProduct, not add
class ProductOfNumbersGetProduct:

    def __init__(self):
        self.products = []

    # Time O(n) multiplies all products by the number
    def add(self, num: int) -> None:
        for i in range(len(self.products)):
            self.products[i] *= num

        self.products.append(num)
        
    # Time O(1)
    def getProduct(self, k: int) -> int:
        return self.products[-k]
        


testCase = ProductOfNumbersEfficient()
testCase.add(3)
testCase.add(0)
testCase.add(2)
testCase.add(5)
testCase.add(4)
assert testCase.getProduct(2) == 20, f"Expected 20 but got {testCase.getProduct(2)}"
assert testCase.getProduct(3) == 40, f"Expected 40 but got {testCase.getProduct(3)}"
assert testCase.getProduct(4) == 0, f"Expected 0 but got {testCase.getProduct(3)}"
assert testCase.getProduct(5) == 0, f"Expected 0 but got {testCase.getProduct(3)}"
testCase.add(8)
assert testCase.getProduct(2) == 32, f"Expected 32 but got {testCase.getProduct(3)}"
print("Passed all assertions")