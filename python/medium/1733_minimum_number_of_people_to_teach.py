from typing import List


class Solution:
    # Go over all friendships that can't talk to each other
    # Keep track of friend indexes who have a broken friendship
    # Go over all n languages and count min num of people who need to learn it
    # Time O(N + FL) as we go through friendships once and languages list once as well
    # Space O(N) as in theory we could store and array of size N
    def minimumTeachings(
        self,
        n: int,
        languages: List[List[int]],
        friendships: List[List[int]]
    ) -> int:
        # Keeps track of people who are in a broken friendship
        broken_friendships_folks = set()

        # Go over all friendships
        for friend1, friend2 in friendships:
            # Quick optimization, if they are both already in a broken friendship
            # Skip doing this computation as we don't care if they can't talk to each other
            if friend1 in broken_friendships_folks and friend2 in broken_friendships_folks:
                continue

            can_communicate = False
            # Add all the languages friend1 speaks to a set
            friend1_langs = set()
            for lang in languages[friend1-1]:
                friend1_langs.add(lang)

            # See if friend2 can communicate
            for lang in languages[friend2-1]:
                if lang in friend1_langs:
                    can_communicate = True
                    break

            # They can't talk, so add indexes to broken friendships
            if not can_communicate:
                broken_friendships_folks.add(friend1)
                broken_friendships_folks.add(friend2)

        # Optimization edge cases
        if len(broken_friendships_folks) == 0:
            return 0
        elif len(broken_friendships_folks) == 2:
            return 1

        # Now go over all languages and see how many of the folks know it
        # Return min of however many people don't
        answer = len(broken_friendships_folks)
        for lang in range(n+1):
            count_need_to_learn = 0
            for person in broken_friendships_folks:
                if lang not in languages[person-1]:
                    count_need_to_learn += 1
            
            # See if we have a new best answer
            answer = min(answer, count_need_to_learn)
        
        return answer

test_cases = [
    [1, 2, [[1],[2],[1,2]], [[1,2],[1,3],[2,3]]],
    [1, 5, [[1],[5],[1,5],[5]], [[1,2],[1,3],[1,4],[2,3]]],
    [2, 3, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]]]
]
solution = Solution()
for expected, n, languages, friendships in test_cases:
    actual = solution.minimumTeachings(n, languages, friendships)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, languages: {languages}, friendships: {friendships}")

print("Ran all tests")