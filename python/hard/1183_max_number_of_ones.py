class Solution:
    # Just tricky math
    # Time O(1)
    # Space O(1)
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        # First fill in all the squares with max_ones
        num_squares = (height // sideLength) * (width // sideLength)
        answer = maxOnes * num_squares

        # Figure out how many 1s we can put in remaining smaller squares
        remain = maxOnes
        cnt1 = min((height % sideLength) * (width % sideLength), remain)
        # Ones to right, ones below, and one to bottom and right
        num_smaller_squares = (height // sideLength) + (width // sideLength) + 1
        answer += num_smaller_squares * cnt1
        remain -= cnt1

        # Fill remainders still left (depending on which one has more)
        if height // sideLength > width // sideLength:
            cnt2 = min(((width % sideLength) * sideLength) - ((height % sideLength) * (width % sideLength)), remain)
            answer += (height // sideLength) * cnt2
            remain -= cnt2
            cnt3 = min(((height % sideLength) * sideLength) - ((height % sideLength) * (width % sideLength)), remain)
            answer += (width // sideLength) * cnt3
            remain -= cnt3
        else:
            cnt2 = min(((height % sideLength) * sideLength) - ((height % sideLength) * (width % sideLength)), remain)
            answer += (width // sideLength) * cnt2
            remain -= cnt2
            cnt3 = min(((width % sideLength) * sideLength) - ((height % sideLength) * (width % sideLength)), remain)
            answer += (height // sideLength) * cnt3
            remain -= cnt3

        return answer

test_cases = [
    [4, 3, 3, 2, 1],
    [6, 3, 3, 2, 2]
]
solution = Solution()
for expected, width, height, side_len, max_ones in test_cases:
    actual = solution.maximumNumberOfOnes(width, height, side_len, max_ones)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: width: {width}, height: {height}")
        print(f"\tINPUTS: side_length: {side_len}, max_ones: {max_ones}")

print("Ran all tests")
