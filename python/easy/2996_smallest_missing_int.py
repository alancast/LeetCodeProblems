class Solution:
    # Go over array once to find largest set and prefix num and create set of nums
    # Then just keep counting from sum til one isn't hit
    # Time O(n)
    # Space O(n)
    def missingInteger(self, nums: list[int]) -> int:
        n = len(nums)
        nums_set = set()

        # Process first num
        nums_set.add(nums[0])
        seq_sum = nums[0]
        # Are we still searching for seq
        seq_cont = True

        # Go over array and count seqs and find sum
        # Turns out we only care about seq starting at index 0
        for i in range(1,n):
            num = nums[i]
            nums_set.add(num)

            # Are we still checking for seq
            if seq_cont:
                # Continued seq
                if num == nums[i-1] + 1:
                    seq_sum += num
                # Broken seq so stop checking for it
                else:
                    seq_cont = False

        # Starting from seq_sum find answer
        while seq_sum in nums_set:
            seq_sum += 1

        return seq_sum

test_cases = [
    [6, [1,2,3,2,5]],
    [15, [3,4,5,1,12,14,13]],
    [38, [37,1,2,9,5,8,5,2,9,4]],
    [15, [14,9,6,9,7,9,10,4,9,9,4,4]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.missingInteger(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
