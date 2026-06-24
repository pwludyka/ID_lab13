import base64
import io

import matplotlib.pyplot as plt
from fastmcp import FastMCP

mcp = FastMCP("Visualization")


@mcp.tool(description="Create a line plot and return it as a base64 encoded image.")
def line_plot(
        data: list[list[float]],
        title: str = "",
        x_label: str = "",
        y_label: str = "",
        legend: bool = False,
) -> str:
    plt.figure()

    for i, series in enumerate(data):
        plt.plot(series, label=f"Series {i + 1}")

    if title:
        plt.title(title)

    if x_label:
        plt.xlabel(x_label)
    
    if y_label:
        plt.ylabel(y_label)

    if legend:
        plt.legend()

    buffer = io.BytesIO()
    plt.savefig(buffer, format="jpg")
    buffer.seek(0)

    return base64.b64encode(buffer.read()).decode()


if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=8003)
