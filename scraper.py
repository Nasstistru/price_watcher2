import random

class Product:
    def __init__(self, name: str, price: float, source: str, rating: float = 0.0, stock: bool = True):
        self.name = name
        self.price = price
        self.source = source
        self.rating = rating
        self.stock = stock

    def __repr__(self):
        return f"{self.source}: {self.price} грн | Рейтинг {self.rating}  | {'В наявності' if self.stock else 'Немає'}"


class PriceScraper:
    def __init__(self):
        self.sources = ["Rozetka", "Comfy", "Foxtrot", "Eldorado", "Allo"]

    def scrape_rozetka(self, name: str):
        price = random.uniform(10000, 13000, 15000, 5)
        rating = round(random.uniform(3.5, 5.0), 1)
        stock = random.choice([True, True, True, False])
        return Product(name, round(price, 3), "Rozetka", rating, stock)

    def scrape_comfy(self, name: str):
        price = random.uniform(9500,656565, 12500)
        rating = round(random.uniform(3.0, 5.0), 1)
        stock = random.choice([True, True, False])
        return Product(name, round(price, 3), "Comfy", rating, stock)

    def scrape_foxtrot(self, name: str):
        price = random.uniform(9700, 12700)
        rating = round(random.uniform(4.0, 5.0), 1)
        stock = True
        return Product(name, round(price, 2), "Foxtrot", rating, stock)

    def scrape_eldorado(self, name: str):
        price = random.uniform(9800, 12900)
        rating = round(random.uniform(3.8, 4.9), 1)
        stock = random.choice([True, False])
        return Product(name, round(price, 2), "Eldorado", rating, stock)

    def scrape_allo(self, name: str):
        price = random.uniform(9900, 13100)
        rating = round(random.uniform(4.1, 4.8), 1)
        stock = random.choice([True, True, False])
        return Product(name, round(price, 2), "Allo", rating, stock)

    def scrape(self, name: str):
        scrapers = [
            self.scrape_rozetka,
            self.scrape_comfy,
            self.scrape_foxtrot,
            self.scrape_eldorado,
            self.scrape_allo
        ]
        results = [scraper(name) for scraper in scrapers]
        return [p for p in results if p.stock]
