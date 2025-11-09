import google.generativeai as genai
from statistics import mean

class LLMClient:
    def __init__(self, api_key: str):

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def summarize(self, products, avg_price, best, diff):

        text = "\n".join([
            f"{p.source}: {p.price} грн ({'в наявності' if p.stock else 'немає'})"
            for p in products
        ])

        prompt = (
            f"Проаналізуй ціни на товар за різними магазинами.\n"
            f"Дані:\n{text}\n\n"
            f"Середня ціна: {avg_price} грн\n"
            f"Найвигідніша пропозиція: {best.source} ({best.price} грн)\n"
            f"Різниця між найдешевшим і найдорожчим варіантом: {diff} грн\n\n"
            f"Зроби короткий висновок українською: оцінка ринку, вигідність покупки, рекомендація де краще купити."
        )

        response = self.model.generate_content(prompt)

        return response.text.strip()