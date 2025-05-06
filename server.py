from fastmcp import FastMCP
from dotenv import load_dotenv
import yfinance as yf

load_dotenv()

# Initialize FastMCP server
mcp = FastMCP(
    name="StockMarketServer",
    instructions="You are a Stock Market Specialist that can answer questions about the stock market.",
    )

@mcp.tool()
async def get_stock_info(symbol: str) -> float:
    """Get information from a stock. It may have a delay of up to 15 minutes."""
    return yf.Ticker(symbol).info

@mcp.tool()
async def get_current_stock_price(symbol: str) -> float:
    """Get the current price of a stock. It may have a delay of up to 15 minutes."""
    return yf.Ticker(symbol).info["regularMarketPrice"],yf.Ticker(symbol).info['financialCurrency']

if __name__ == "__main__":
    mcp.run(transport="stdio")