from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class FoodRatings:
    # Map of food to rating
    food_ratings: defaultdict
    # Map of food to cuisine
    food_to_cuisine: defaultdict
    # Map of cuisine to priority queue of (score, food)
    cuisines_best: defaultdict

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]) -> None:
        self.food_ratings = defaultdict(int)
        self.food_to_cuisine = defaultdict(str)
        self.cuisines_best = defaultdict(list)

        for i in range(len(foods)):
            food = foods[i]
            rating = ratings[i]
            cuisine = cuisines[i]

            # Put the food in the food rating
            self.food_ratings[food] = rating

            # Map the food to the cuisine
            self.food_to_cuisine[food] = cuisine

            # Put rating in the cuisine map
            heappush(self.cuisines_best[cuisine], (-rating, food))

    # Change the rating in the food map
    # Put new value in cuisine priority queue
    # Time O(1)
    def changeRating(self, food: str, newRating: int) -> None:
        self.food_ratings[food] = newRating
        heappush(self.cuisines_best[self.food_to_cuisine[food]], (-newRating, food))

    # Go through cuisine priority queue
    # If highest rated doesn't match current rating pop it and keep searching
    # Time O(n) as worst case we pop through whole queue
    def highestRated(self, cuisine: str) -> str:
        # Keep popping items until we have a max
        while True:
            # Get the highest rated item in the queue
            rating, food = self.cuisines_best[cuisine][0]

            # Make sure it's still the rating and hasn't changed
            if self.food_ratings[food] == -rating:
                return food
            
            # If rating has changed then pop the queue entry and try next one
            heappop(self.cuisines_best[cuisine])


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
