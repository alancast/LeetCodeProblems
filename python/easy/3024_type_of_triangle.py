class Solution:
    # Time and space effectively O(1) since everything is just 3
    def triangleType(self, nums: list[int]) -> str:
        nums.sort()

        a = nums[0]
        b = nums[1]
        c = nums[2]

        if a + b <= c:
            return "none"
        if a == c:
            return "equilateral"
        if b in (a, c):
            return "isosceles"

        return "scalene"

test_cases = [
    ["equilateral", [3,3,3]],
    ["isosceles", [3,3,5]],
    ["isosceles", [3,5,5]],
    ["scalene", [3,4,5]],
    ["none", [1,1,2]],
    ["none", [1,1,3]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.triangleType(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
