from typing import List


# Compute time in tunnel for each lap and time outside of tunnel for each lap
# Time O(nlogn) as we have to sort A and B and then go through them at most twice
# Space O(1)
def getSecondsElapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
    # Sort A and B for tunnel ordering
    A.sort()
    B.sort()
    # Compute tunnel time per lap
    tunnel_time_per_lap = 0
    for i in range(N):
        start = A[i]
        end = B[i]
        tunnel_time_per_lap += end - start

    # Compute how many laps until getting to last lap
    laps_before_last = K // tunnel_time_per_lap

    # We go around the track this many times and it takes C seconds
    answer = laps_before_last * C
    # How much of K is left
    K -= laps_before_last * tunnel_time_per_lap

    ## If remaining tunnel time is exactly 0, we can end at the end of the final
    if K == 0:
        return answer - C + B[-1]

    # Compute how long on last lap
    tunnel_index = 0
    end = 0
    while K > 0:
        start = A[tunnel_index]
        end = B[tunnel_index]
        tunnel_index += 1
        # Subtract this tunnel from K
        K -= end - start

    # We had to get to the last end but if K is negative we can add some back
    answer += end + K
    
    return answer

test_cases = [
    [22, 10, 2, [1,6], [3,7], 7],
    [49, 50, 3, [39,19,28], [49,27,35], 25],
    [35, 50, 3, [39,19,28], [49,27,35], 15]
]
for expected, C, N, A, B, K in test_cases:
    actual = getSecondsElapsed(C, N, A, B, K)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: C: {C}, N: {N}, A: {A}, B: {B}, K: {K}")

print("Ran all tests")