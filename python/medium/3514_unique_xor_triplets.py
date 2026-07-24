class Solution:
    # DP where we store what numbers are getable with 1 xor, then 2, then 3
    # Time O(nm)
    # Space O(m)
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        m = max(nums)
        u = 1
        while u <= m:
            u <<= 1

        # Is the value x_or able with just one, two, or three nums
        one = [False] * u
        two = [False] * u
        three = [False] * u

        # Populate one and two
        for num in nums:
            one[num] = True
            for x in range(u):
                if one[x]:
                    two[x ^ num] = True

        # Go over nums again and use it to populate three
        for num in nums:
            for x in range(u):
                if two[x]:
                    three[x ^ num] = True

        # Count how many show up in 3
        return sum(1 for b in three if b)

test_cases = [
    [2, [1,3]],
    [4, [6,7,8,9]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.uniqueXorTriplets(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
