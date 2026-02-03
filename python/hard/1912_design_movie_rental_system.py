from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class MovieRentingSystem:
    _rented: set
    _rented_prices: List
    _cheapest_movie_locs: defaultdict
    _movie_prices: dict


    # Time O(nlogn + n) for creating cheapest movie locations and populating prices
    def __init__(self, n: int, entries: List[List[int]]):
        # Initially empty as nothing is rented
        self._rented = set()
        self._rented_prices = []

        # Create list per movie of cheapest locations and populate price info
        self._cheapest_movie_locs = defaultdict(list)
        self._movie_prices = defaultdict(int)
        for shop, movie, price in entries:
            self._cheapest_movie_locs[movie].append((price, shop, movie))

            # Also populate price info while doing this
            self._movie_prices[(shop, movie)] = price

        # Make sure cheapest movie locs are all sorted
        for movie in self._cheapest_movie_locs:
            self._cheapest_movie_locs[movie].sort()


    # Go over cheapest locations, make sure they are unrented
    # Time O(n) as worst case all are same movie and all rented
    # In practice likely mostly O(1)
    def search(self, movie: int) -> List[int]:
        locations = []
    
        for _, location, _ in self._cheapest_movie_locs[movie]:
            # If the movie is currently rented then don't add it
            if (location, movie) in self._rented:
                continue

            locations.append(location)

            if len(locations) == 5:
                break

        return locations


    # Time O(logn) as we add to rented prices
    def rent(self, shop: int, movie: int) -> None:
        self._rented.add((shop, movie))
        heappush(self._rented_prices, (self._movie_prices[(shop, movie)], shop, movie))


    # Time O(1)
    def drop(self, shop: int, movie: int) -> None:
        self._rented.remove((shop, movie))


    # Go over rented prices and make sure are still rented
    # Time O(n) as worst case all unrented now
    def report(self) -> List[List[int]]:
        cheapest_rented = []
        # In case a movie is in the rented prices array already
        already_added = set()

        # Pop all movies from queue until we have 5 that are rented
        while self._rented_prices and len(cheapest_rented) < 5:
            _, shop, movie = heappop(self._rented_prices)

            # Movie was returned
            if (shop, movie) not in self._rented:
                continue

            # Movie is still rented but make sure not already added to array
            if (shop, movie) in already_added:
                continue

            cheapest_rented.append([shop, movie])
            already_added.add((shop, movie))

        # Re-add rented movies to queue
        for shop, movie in cheapest_rented:
            heappush(self._rented_prices, (self._movie_prices[(shop, movie)], shop, movie))

        return cheapest_rented



# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
