class MovieRentingSystem:
    
    def __init__(self, n: int, entries: List[List[int]]):
        self.available = {}
        self.movie_shops = {}
        self.rented = set()

        
        for shop, movie, price in entries:
            self.available[(shop, movie)] = price
            if movie not in self.movie_shops:
                self.movie_shops[movie] = []
            self.movie_shops[movie].append((price, shop))

        for movie in self.movie_shops:
            self.movie_shops[movie].sort()

    def search(self, movie: int) -> List[int]:
        res = []
        for price, shop in self.movie_shops.get(movie, []):
            if (shop, movie) not in self.rented:
                res.append(shop)
            if len(res) == 5:
                break
        return res

    def rent(self, shop: int, movie: int) -> None:
        self.rented.add((shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.rented.discard((shop, movie))
    
    def report(self) -> List[List[int]]:
        rented_list = []
        for shop, movie in self.rented:
            price = self.available[(shop, movie)]
            rented_list.append((price, shop, movie))    
        rented_list.sort()
        return [[shop, movie] for price, shop, movie in rented_list[:5]]  

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()