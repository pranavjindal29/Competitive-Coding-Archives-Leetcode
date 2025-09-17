import heapq

class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_foods = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r
            if c not in self.cuisine_foods:
                self.cuisine_foods[c] = []
            heapq.heappush(self.cuisine_foods[c], (-r, f))

    def changeRating(self, food, newRating):
        cuisine = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        heapq.heappush(self.cuisine_foods[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        heap = self.cuisine_foods[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)