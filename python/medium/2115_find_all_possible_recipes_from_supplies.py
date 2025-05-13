from collections import defaultdict, deque
from typing import List


class Solution:
    # Time O(R + I + S)
    # Space O(R + I + S)
    def findAllRecipes(
        self,
        recipes: list[str],
        ingredients: list[list[str]],
        supplies: list[str],
    ) -> list[str]:
        # Store available supplies
        available_supplies = set(supplies)
        # Map recipe to its index
        recipe_to_index = {recipe: idx for idx, recipe in enumerate(recipes)}
        # Map ingredient to recipes that need it
        dependency_graph = defaultdict(list)
        # Count of non-supply ingredients needed for each recipe
        in_degree = [0] * len(recipes)

        # Build dependency graph
        for recipe_idx, ingredient_list in enumerate(ingredients):
            for ingredient in ingredient_list:
                # Only care about ingredients we can create later (recipes basically)
                if ingredient not in available_supplies:
                    dependency_graph[ingredient].append(recipes[recipe_idx])
                    # Notate that this recipe needs something that needs to be made (or we don't have)
                    in_degree[recipe_idx] += 1

        # Start with recipes that only need supplies
        queue = deque(idx for idx, count in enumerate(in_degree) if count == 0)
        created_recipes = []

        # Process recipes in topological order
        while queue:
            recipe_idx = queue.popleft()
            recipe = recipes[recipe_idx]
            created_recipes.append(recipe)

            # Skip if no recipes depend on this one
            for dependent_recipe in dependency_graph[recipe]:
                in_degree[recipe_to_index[dependent_recipe]] -= 1
                # If we now have all we need for this recipe add it to the queue
                if in_degree[recipe_to_index[dependent_recipe]] == 0:
                    queue.append(recipe_to_index[dependent_recipe])

        return created_recipes

    # Time O(S + R*R*I) as we could need to loop through full recipes list r times if one is added per time
    # Space O(S + R)
    def findAllRecipes_bfs(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Create supply set
        supply_set = set()
        for supply in supplies:
            supply_set.add(supply)

        answer_set = set()

        # Iterate over all recipes until no new ones are added, then we know we've gotten all we can
        added_supply = True
        while added_supply:
            added_supply = False
            for i in range(len(recipes)):
                recipe = recipes[i]
                # Already added
                if recipe in supply_set:
                    continue

                # See if we can create recipe with supplies we have
                have_all_ingredients = True
                for ingredient in ingredients[i]:
                    if ingredient not in supply_set:
                        have_all_ingredients = False
                        break

                # Was able to make the recipe so add it to new supplies and let loop know we added something new
                if have_all_ingredients:
                    answer_set.add(recipe)
                    supply_set.add(recipe)
                    added_supply = True

        return list(answer_set)
    
test_cases = [
    [["bread"], ["bread"], [["yeast","flour"]], ["yeast","flour","corn"]],
    [["bread","sandwich"], ["bread","sandwich"], [["yeast","flour"],["bread","meat"]], ["yeast","flour","meat"]],
    [["bread","sandwich","burger"], ["bread","sandwich","burger"], [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], ["yeast","flour","meat"]]
]
solution = Solution()
for expected, recipes, ingredients, supplies in test_cases:
    actual = solution.findAllRecipes(recipes, ingredients, supplies)
    actual.sort()
    expected.sort()
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: recipes: {recipes}, ingredients: {ingredients}, supplies: {supplies}")

print("Ran all tests")