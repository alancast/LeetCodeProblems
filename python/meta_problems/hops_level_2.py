# At first thought was sort the array then just do N - num - len for each one
# But realized each frog you hop over needs to hop as well
# So though you skip one there you just add it back when it hops
# So really all you need to do is find the min pad
# Time O(F) as we just go over the array once to find the min
# Space O(1) for sorting algorithm
def getSecondsRequired(N: int, F: int, P: list[int]) -> int:
    return N - min(P)

test_cases = [
    [2, 3, 1, [1]],
    [4, 6, 3, [5,2,4]]
]
for expected, N, F, P in test_cases:
    actual = getSecondsRequired(N, F, P)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: N: {N}, F: {F}, P: {P}")

print("Ran all tests")
