class Solution:
    # This problem is silly, no trick, just use sorting on ones
    # Can write custom comparator or just use the built in
    # Time O(nlogn)
    # Space O(n)
    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort(key = lambda num: (num.bit_count(), num))
        return arr

test_cases = [
    [[0,1,2,4,8,3,5,6,7], [0,1,2,3,4,5,6,7,8]],
    [[1,2,4,8,16,32,64,128,256,512,1024], [1024,512,256,128,64,32,16,8,4,2,1]]
]
solution = Solution()
for expected, arr in test_cases:
    actual = solution.sortByBits(arr)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: arr: {arr}")

print("Ran all tests")
