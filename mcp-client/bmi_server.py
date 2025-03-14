from mcp.server.fastmcp import FastMCP

mcp = FastMCP("BMI Calculator")


@mcp.tool()
async def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI given weight in kg and height in meters"""
    return weight_kg / (height_m ** 2)

if __name__ == "__main__":
    mcp.run(transport="stdio")