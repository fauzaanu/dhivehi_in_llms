import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def generate_graph(ev):
    benchmarks = [model.model_dump() for model in ev.benchmarks]
    # Convert to DataFrame
    df = pd.DataFrame(benchmarks)
    # Drop 'model_name' from metrics and set it as index
    df.set_index("model_name", inplace=True)
    # Compute the average rating for each model
    df["average_score"] = df.mean(axis=1)
    # Sort models by performance
    df_sorted = df.sort_values(by="average_score", ascending=False)
    colors = plt.cm.plasma(np.linspace(0.2, 0.8, len(df_sorted)))
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(df_sorted.index, df_sorted["average_score"], color=colors, edgecolor="white")
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, f"{yval:.1f}", ha="center", fontsize=12,
                fontweight="bold",
                color="white")
    # Customize chart appearance
    ax.set_facecolor("#121212")
    fig.patch.set_facecolor("#121212")
    ax.spines["bottom"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    # Labels and title with modern font styles
    ax.set_xlabel("Model Name", fontsize=14, fontweight="bold", color="white")
    ax.set_ylabel("Average Score (Out of 10)", fontsize=14, fontweight="bold", color="white")
    ax.set_title("Dhivehi Performance compare", fontsize=16, fontweight="bold", color="white")
    # Improve readability of x-axis labels
    plt.xticks(rotation=25, fontsize=12, color="white")
    plt.yticks(fontsize=12, color="white")
    # Grid customization
    ax.grid(axis="y", linestyle="--", alpha=0.5, color="gray")
    # Save the chart
    plt.savefig("model_performance_comparison.png", dpi=300, bbox_inches="tight")
