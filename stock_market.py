from typing import Any
import httpx
from fastmcp import FastMCP
from helpers import get_stock_price
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize FastMCP server
mcp = FastMCP(
    name="StockMarketServer",
    instructions="You are a stock market server that can answer questions about the stock market.",
    )

# Constants
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
ALPHAVANTAGE_API_BASE = "https://www.alphavantage.co/query"
USER_AGENT = "stock-market-app/1.0"

@mcp.tool()
async def get_stock_price(symbol: str) -> float:
    """Get the current price of a stock."""
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": ALPHAVANTAGE_API_KEY,
    }
    response = httpx.get(ALPHAVANTAGE_API_BASE, params=params)
    return response.json()["Global Quote"]["05. price"]

if __name__ == "__main__":
    mcp.run()