from typing import List


class Solution:
    # Trie plus Floyd Warshall plus DP
    # Crazy hard problem. Read through editorial then chatted with AI to understand
    # n is source length, m is length of original array, L is average str length
    # Time O(n^2 + m^3 + mL)
    # Space O(n + m^2 + mL)
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        INF = 10**18
        INF_INT = 10**9

        n = len(source)
        m = len(original)

        # Initialize trie structure: child[node][char] = next_node
        child = [[-1] * 26]
        # tid[node] = transformation id (for words ending at this node)
        tid = [-1]

        # Create a new trie node
        def new_node() -> int:
            child.append([-1] * 26)
            tid.append(-1)
            return len(child) - 1

        idx = -1

        # Add word to the trie and return its transformation id
        def add(word: str) -> int:
            nonlocal idx
            node = 0

            # Traverse/build trie for each character in word
            for ch in word:
                c = ord(ch) - 97
                nxt = child[node][c]

                # Create new node if path doesn't exist
                if nxt == -1:
                    nxt = new_node()
                    child[node][c] = nxt

                node = nxt

            # Assign unique id to this word if not already assigned
            if tid[node] == -1:
                idx += 1
                tid[node] = idx

            return tid[node]

        # Build trie and create edges for transformation graph
        edges = []
        for i in range(m):
            x = add(original[i])
            y = add(changed[i])
            edges.append((x, y, cost[i]))

        # P = total number of unique words in trie
        P = idx + 1
        # If there are no unique words in the trie either no cost or impossible
        if P == 0:
            return 0 if source == target else -1

        # Floyd-Warshall: compute shortest path between all pairs of words
        dist = [[INF_INT] * P for _ in range(P)]
        for i in range(P):
            dist[i][i] = 0
        for x, y, w in edges:
            if w < dist[x][y]:
                dist[x][y] = w

        # Apply Floyd-Warshall algorithm
        for k in range(P):
            dk = dist[k]
            for i in range(P):
                di = dist[i]
                dik = di[k]
                if dik == INF_INT:
                    continue
                base = dik
                for j in range(P):
                    nd = base + dk[j]
                    if nd < di[j]:
                        di[j] = nd

        # DP[i] = min cost to convert source[0:i] to target[0:i]
        dp = [INF] * (n + 1)
        dp[0] = 0

        s_arr = [ord(c) - 97 for c in source]
        t_arr = [ord(c) - 97 for c in target]

        # Build DP by trying all possible substring conversions
        # Start at position j, and compute dp for all possible changes to get to end
        # Going over all possible length substrings starting there
        for j in range(n):
            if dp[j] >= INF:
                continue

            base = dp[j]

            # If characters match, no conversion needed
            if source[j] == target[j] and base < dp[j + 1]:
                dp[j + 1] = base

            # Try all substrings starting at position j
            u = 0  # Trie node for source substring
            v = 0  # Trie node for target substring
            for i in range(j, n):
                # Navigate both tries character by character
                u = child[u][s_arr[i]]
                v = child[v][t_arr[i]]
                
                # If either substring doesn't exist in trie, stop exploring
                # And go to next starting point j
                if u == -1 or v == -1:
                    break
                
                # Get transformation IDs for current substrings (or -1 if not a complete word)
                uid = tid[u]
                vid = tid[v]
                
                # Only proceed if both substrings are complete words in our transformation set
                if uid != -1 and vid != -1:
                    # Look up shortest transformation cost from source word to target word
                    w = dist[uid][vid]
                    
                    # If a valid transformation path exists
                    if w != INF_INT:
                        ni = i + 1  # Next position in source/target strings
                        cand = base + w  # Candidate cost: previous cost + transformation cost
                        
                        # Update DP if this path is cheaper than previously found
                        if cand < dp[ni]:
                            dp[ni] = cand

        ans = dp[n]
        return -1 if ans >= INF else ans

test_cases = [
    [28, "abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]],
    [9, "abcdefgh", "acdeeghh", ["bcd","fgh","thh"], ["cde","thh","ghh"], [1,3,5]],
    [-1, "abcdefgh", "addddddd", ["bcd","defgh"], ["ddd","ddddd"], [100,1578]],
    [-1, "ab", "cd", ["a","bb"], ["b","cd"], [1,2]]
]
solution = Solution()
for expected, source, target, original, changed, cost in test_cases:
    actual = solution.minimumCost(source, target, original, changed, cost)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: source: {source}, target: {target}, original: {original}")
        print(f"\tINPUTS: changed: {changed}, cost: {cost}")

print("Ran all tests")
