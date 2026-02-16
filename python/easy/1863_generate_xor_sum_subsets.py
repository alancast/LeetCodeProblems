class Solution:
    # Math way to get sum. Described in leet code answer
    # Would not have come up with on my own
    # Time O(n) Space O(1)
    def subsetXORSum_mathed(self, nums: list[int]) -> int:
        result = 0
        # Capture each bit that is set in any of the elements
        for num in nums:
            result |= num
        # Multiply by the number of subset XOR totals that will have each bit set
        return result << (len(nums) - 1)

    # Brute force where all subsets are generated xored
    # Time O(2^n) as each element can be either in our out of subset so a total of 2^n subsets
    # Space O(N) as recursion just reaches depth of n
    def subsetXORSum_optimized_brute_force(self, nums: list[int]) -> int:
        return self.xor_sum(nums, 0, 0)

    def xor_sum(self, nums: list[int], index: int, current_xor: int) -> int:
        if index == len(nums):
            return current_xor

        # Calculate sum of subset xor with current element
        with_element = self.xor_sum(nums, index + 1, current_xor ^ nums[index])

        # Calculate sum of subset xor without current element
        without_element = self.xor_sum(nums, index + 1, current_xor)

        # Return sum of xor totals
        return with_element + without_element

    # Brute force where all subsets are generated and then summed
    # Time and Space O(n * 2^n) as each element can be either in our out of subset
    # So a total of 2^n subsets
    def subsetXORSum_brute_force(self, nums: list[int]) -> int:
        all_subsets = []
        self.generate_subsets(nums, 0, [], all_subsets)

        xor_sum = 0
        for subset in all_subsets:
            # Compute xor of subset
            xor_total = 0
            for num in subset:
                xor_total ^= num

            xor_sum += xor_total

        return xor_sum

    def generate_subsets(self, nums: list[int], index: int, subset: list[int], subsets: list[list[int]]) -> None:
        if index == len(nums):
            subsets.append(subset[:])
            return

        # Include number
        subset.append(nums[index])
        index += 1
        self.generate_subsets(nums, index, subset, subsets)

        # Don't include number
        subset.pop()
        self.generate_subsets(nums, index, subset, subsets)

test_cases = [
    [6, [1,3]],
    [28, [5,1,6]],
    [480, [3,4,5,6,7,8]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.subsetXORSum_mathed(nums)
    if actual != expected:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all test!")
