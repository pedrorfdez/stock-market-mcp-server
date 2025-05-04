import httpx
from typing import Any
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()

# Constants
ALPHAVANTAGE_API_BASE = "https://www.alphavantage.co/query?datatype=json&function="
USER_AGENT = "stock-market-app/1.0"
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

async def make_alphavantage_request(url: str, function: str, symbol: str) -> dict[str, Any] | None:
    """Make a request to the Alpha Vantage API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url+function+"&symbol="+symbol+"&apikey="+ALPHAVANTAGE_API_KEY, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

async def get_stock_price(symbol: str) -> dict[str, Any]:
    """Get the current price of a stock."""
    data = await make_alphavantage_request(ALPHAVANTAGE_API_BASE, "GLOBAL_QUOTE", symbol)
    return data

if __name__ == "__main__":
    price = asyncio.run(get_stock_price("AAPL"))
    print(f"AAPL stock price: ${price}")