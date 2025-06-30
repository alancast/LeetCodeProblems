from typing import List


# Do DFS of nodes and keep a visited nodes list
# Iterate over all nodes until done
# Time O(n) as each node is visited once-ish
# Space O(n) as we keep multiple size n data fields
def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
    # N+1 because all of these are 1 indexed (annoying)
    page_id = [0] * (N + 1)
    max_visitable_from_page = [0] * (N + 1)

    # If page hasn't been visited yet, run DFS starting at page
    for page in range(1, N + 1):
        # This page has already been explored
        if page_id[page] != 0:
            continue

        starting_page = page
        pages_visited = 0

        # DFS until we reach a page that has already been visited.
        # Set the ID of each page visited to the starting page.
        while page_id[page] == 0:
            pages_visited += 1
            page_id[page] = starting_page
            max_visitable_from_page[page] = pages_visited
            page = L[page - 1]

        # If the page_id is the same as the starting page, the DFS has looped back into itself.
        if page_id[page] == starting_page:
            pages_in_cycle = pages_visited - max_visitable_from_page[page] + 1

            # Set the max_visitable value of each page in the cycle to pages_in_cycle.
            while page_id[page] != -starting_page:
                page_id[page] = -starting_page
                max_visitable_from_page[page] = pages_in_cycle
                page = L[page - 1]

        # If the page_id is different from the starting page, the DFS has
        # reached a page visited in a previous DFS run.
        else:
            pages_visited += max_visitable_from_page[page]

        # Run DFS again and set the max_visitable value of each page to
        # pages_visited while decrementing pages_visited for each page visited.
        page = starting_page
        while page_id[page] == starting_page:
            max_visitable_from_page[page] = pages_visited
            pages_visited -= 1
            page = L[page - 1]

    return max(max_visitable_from_page)

test_cases = [
    [4, 4, [4,1,2,1]],
    [3, 5, [4,3,5,1,2]],
    [4, 5, [2,4,2,2,3]]
]
for expected, N, L in test_cases:
    actual = getMaxVisitableWebpages(N, L)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: N: {N}, L: {L}")

print("Ran all tests")