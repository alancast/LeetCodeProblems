# Time O(SlogS) for sorting
# Space O(S) for sorting algo
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: list[int]) -> int:
  can_add = 0
  S.sort()

  left = 1
  for seat in S:
    # rightmost empty seat
    right = seat - (K + 1)
    can_add += 1 + (right - left) // (K+1)
    left = seat + K + 1

  can_add += 1 + (N - left) // (K+1)

  return can_add

test_cases = [
    [3, 10, 1, 2, [2,6]],
    [1, 15, 2, 3, [11,6,14]]
]
for expected, N, K, M, S in test_cases:
    actual = getMaxAdditionalDinersCount(N, K, M, S)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: N: {N}, K: {K}, M: {M}, S: {S}")

print("Ran all tests")
