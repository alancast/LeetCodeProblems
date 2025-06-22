from typing import List


# Time O(M) as we do O(1) math operation for each entry
# Space O(1)
def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    answer = 0
    previous = 1

    for digit in C:
        #  See if it's faster to go around 1 or not
        direct = abs(digit - previous)
        answer += min(direct, N - direct)
        previous = digit
        
    return answer

test_cases = [
    [2, 3, 3, [1,2,3]],
    [11, 10, 4, [9,4,4,8]]
]
for expected, N, M, C in test_cases:
    actual = getMinCodeEntryTime(N, M, C)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: N: {N}, M: {M}, C: {C}")

print("Ran all tests")