from fastapi import FastAPI
from scraper import PriceScraper
from llm_client import LLMClient
from db import SessionLocal, ProductDB
from statistics import mean
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

llm = LLMClient(api_key=api_key)

app = FastAPI(title="Оглядач цін – Price Observer")
scraper = PriceScraper()

@app.get("/products/{name}")
def compare_prices(name: str):
    session = SessionLocal()
    products = scraper.scrape(name)

    for p in products:
        session.add(ProductDB(name=p.name, price=p.price, source=p.source))
    session.commit()


    prices = [p.price for p in products]
    avg_price = round(mean(prices), 2)
    best = min(products, key=lambda x: x.price)
    worst = max(products, key=lambda x: x.price)
    diff = round(worst.price - best.price, 2)

    summary = llm.summarize(products, avg_price, best, diff)

    return {
        "product": name,
        "avg_price": avg_price,
        "price_diff": diff,
        "best_offer": best.source,
        "prices": [p.__dict__ for p in products],
        "summary": summary
    }