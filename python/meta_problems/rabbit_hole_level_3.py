# Very difficult problem. Past a leet code hard
# Use Tarjans Strongly Connected Component algorithm to find SCCs
# Then find size of SCCs and find maximum visitable pages
# Time O(N+M) as that's what Tarjans takes
# Space O(N+M)
def getMaxVisitableWebpages(N: int, M: int, A: list[int], B: list[int]) -> int:  # noqa: PLR0912, PLR0915
    scc_id = 1
    page_cluster_id = [0] * (N + 1)
    page_id = [0] * (N + 1)
    max_visitable_from_page = [0] * (N + 1)

    stack        = []
    page_history = []

    links = [set() for _ in range(N + 1)]
    unvisited_links = []

    # Create adjacency list
    for i in range(M):
        links[A[i]].add(B[i])

    # Copy of adjacency lists.
    for i in range(N + 1):
        unvisited_links.append(list(links[i]))

    for page in range(1, N + 1):
        # Skip if node already visited
        if page_id[page] != 0:
            continue

        # Non-recursive Tarjan's SCC Algorithm
        stack.append(page)
        while len(stack) > 0:
            current_page = stack.pop()
            recurse = False

            # First time seeing current_page
            # When we have already seen a page we push to stack it's neg id
            if current_page > 0:
                page_id[current_page] = scc_id
                page_cluster_id[current_page] = scc_id
                scc_id += 1

                page_history.append(current_page)

                avalible_links = unvisited_links[current_page]
                while len(avalible_links) > 0:
                    next_page = avalible_links[-1]
                    if page_id[next_page] == 0:
                        # Recursively execute on next_page
                        stack.append(-current_page)
                        stack.append(next_page)
                        recurse = True
                        break

                    if page_id[next_page] > 0:
                        page_cluster_id[current_page] = min(page_cluster_id[current_page], page_id[next_page])

                    del avalible_links[-1]

            # Continue executing where we left off
            else:
                current_page = -current_page
                avalible_links = unvisited_links[current_page]
                next_page = avalible_links[-1]

                page_cluster_id[current_page] = min(page_cluster_id[current_page], page_cluster_id[next_page])
                del avalible_links[-1]

                while len(avalible_links) > 0:
                    next_page = avalible_links[-1]
                    if page_id[next_page] == 0:
                        # Recursivly execute on next_page
                        stack.append(-current_page)
                        stack.append(next_page)
                        recurse = True
                        break

                    if page_id[next_page] > 0:
                        page_cluster_id[current_page] = min(page_cluster_id[current_page], page_id[next_page])

                    del avalible_links[-1]

            # This effectively makes it a DFS as any chance you can when you see
            # A new node you explore it
            if recurse:
                continue

            # A Strongly Connected Component Identified
            if page_cluster_id[current_page] == page_id[current_page]:
                prev_page = page_history.pop()
                page_id[prev_page] *= -page_id[current_page]
                scc = [prev_page]
                scc_size = 1

                # Go until you get back to the start page (an SCC is a cycle so this will happen)
                while prev_page != current_page:
                    prev_page = page_history.pop()
                    page_id[prev_page] *= -page_id[current_page]
                    scc.append(prev_page)
                    scc_size += 1

                # Condense SCC into a single "page" with union of all links
                scc_links = set()
                for page in scc:
                    scc_links.update(links[page])

                # Remove links to pages within the SCC
                scc_links.difference_update(scc)

                # The max visitable from this SCC is
                # Larger than the scc size because some link might take you out of it
                max_visitable_from_this_scc = scc_size + max([0] + [max_visitable_from_page[page] for page in scc_links])

                # Assign the max_visitable value to all pages in the SCC
                for page in scc:
                    max_visitable_from_page[page] = max_visitable_from_this_scc

    return max(max_visitable_from_page)

test_cases = [
    [4, 4, 4, [1,2,3,4], [4,1,2,1]],
    [4, 5, 6, [3,5,3,1,3,2], [2,1,2,4,5,4]],
    [5, 10, 9, [3,2,5,9,10,3,3,9,4], [9,5,7,8,6,4,5,3,9]]
]
for expected, N, M, A, B in test_cases:
    actual = getMaxVisitableWebpages(N, M, A, B)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: N: {N}, M: {M}, A: {A}, B: {B}")

print("Ran all tests")
