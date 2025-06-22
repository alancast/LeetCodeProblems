# Time O(c) as we go over whole string once then actors but that is less than c
# Space O(C) as we store multiple arrays of length C
def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  answer = 0
  # Keep track of actor indexes and prefix sums and then iterate over actors
  # And find P-A-B combos as well as B-A-P
  actors = []
  
  # Prefix sums: store number of photographers and backdrops seen so far
  photographers_before_pos = [0]
  backdrops_before_pos = [0]

  photographer_count = 0
  backdrop_count = 0
  for i in range(N):
    if C[i] == 'A':
      actors.append(i)
    elif C[i] == 'P':
      photographer_count += 1
    elif C[i] == 'B':
      backdrop_count += 1

    # Append current totals to prefix arrays
    photographers_before_pos.append(photographer_count)
    backdrops_before_pos.append(backdrop_count)

  # For each actor, count valid P and B on both sides within distance [X, Y]
  for a in actors:
    # Calculate left and right bounds for photographer and backdrop
    left_start = max(0, a - Y)
    left_end = max(0, a - X + 1)
    right_start = min(N, a + X)
    right_end = min(N, a + Y + 1)
    
    # Count valid P-A-B arrangements
    answer += (photographers_before_pos[left_end] - photographers_before_pos[left_start]) * (backdrops_before_pos[right_end] - backdrops_before_pos[right_start])
    # Count valid B-A-P arrangements
    answer += (backdrops_before_pos[left_end] - backdrops_before_pos[left_start]) * (photographers_before_pos[right_end] - photographers_before_pos[right_start])

  return answer

test_cases = [
    [1, 5, "APABA", 1, 2],
    [0, 5, "APABA", 2, 3],
    [3, 8, ".PBAAP.B", 1, 3]
]
for expected, N, C, X, Y in test_cases:
    actual = getArtisticPhotographCount(N, C, X, Y)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: N: {N}, C: {C}, X: {X}, Y: {Y}")

print("Ran all tests")