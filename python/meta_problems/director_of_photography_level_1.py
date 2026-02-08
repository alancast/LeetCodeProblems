# Time O(c^3) as we have a triple nested for loop
# Space O(C) as we store potentially each char in C in a separate array
def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:  # noqa: PLR0912
  photographers = []
  actors = []
  backdrops = []

  # Populate indexes of lists above then iterate through and find combos
  for index, char in enumerate(C):
    if char == 'P':
      photographers.append(index)
    elif char == 'A':
      actors.append(index)
    elif char == 'B':
      backdrops.append(index)

  # Loop through the combos
  answer = 0
  for p_index in photographers:
    for a_index in actors:
      # actor is too far away
      if a_index > p_index + Y:
        break
      # actor is within range
      a_p_distance = abs(a_index - p_index)
      if a_p_distance < X or a_p_distance > Y:
        continue

      # determine if backdrop must be below or above actor
      need_lower_backdrop = False
      if a_index < p_index:
        need_lower_backdrop = True


      # Now loop over backdrops
      for b_index in backdrops:
        # backdrop is too far or not behind actor
        if b_index > a_index + Y or (need_lower_backdrop and b_index > a_index - X):
          break
        # backdrop is within range
        a_b_distance = abs(a_index - b_index)
        if a_b_distance < X or a_b_distance > Y:
          continue

        # Make sure actor is between photographer and backdrop
        if not need_lower_backdrop and b_index < a_index:
          continue


        # This is a valid combo
        answer += 1

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
