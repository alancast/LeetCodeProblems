from typing import List


class Solution:
    # Time O(n!) as we backtrack all n! possibilities
    # Space O(n) as recursion stack can only go to depth n and they all share same structures of size n
    def constructDistancedSequence(self, n: int) -> List[int]:
        len_sequence = (2*n) - 1
        answer = [-1] * len_sequence
        available_nums = []
        for i in range(n):
            available_nums.append(i+1)

        _ = self.sequence_is_possible(answer, available_nums, 0)

        return answer
    
    # Try backtracking starting from biggest to smallest num
    # As soon as we get one that works that's the answer
    def sequence_is_possible(self, sequence: List[int], available_nums: List[int], index: int) -> bool:
        # Base case, we've gotten to final index
        if index == len(sequence):
            return True
        
        # This index is already taken, so go to next free one with nums left
        if sequence[index] != -1:
            return self.sequence_is_possible(sequence, available_nums, index + 1)
        
        # See what's the highest number you can put in the next location to get the sequence to work
        for i in range(len(available_nums)-1,-1,-1):
            # number is already used
            if available_nums[i] == -1:
                continue

            num = available_nums[i]
            if num == 1:
                sequence[index] = num
            elif index + num >= len(sequence) or sequence[index + num] != -1:
                continue
            else:
                sequence[index] = num
                sequence[index+num] = num

            available_nums[i] = -1
            if self.sequence_is_possible(sequence, available_nums, index + 1):
                return True
            
            # This placement of n didn't work so undo changes
            sequence[index] = -1
            if num != 1:
                sequence[index+num] = -1
            available_nums[i] = num

        return False
    
test_cases = [
    [[1], 1],
    [[2,1,2], 2],
    [[3,1,2,3,2], 3],
    [[4,2,3,2,4,3,1], 4],
    [[5,3,1,4,3,5,2,4,2], 5]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.constructDistancedSequence(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")