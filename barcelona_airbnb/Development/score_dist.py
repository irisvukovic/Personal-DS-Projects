# VISUALIZE THE SCORE DISTRIBUTION 
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(13, 4))
 
# Histogram
df["commercialization_score"].plot(
    kind="hist", bins=50, ax=axes[0], color="#e63946", edgecolor="white"
)
axes[0].set_title("Commercialization Score Distribution", fontweight="bold")
axes[0].set_xlabel("Score (0 = casual host, 100 = full commercial operator)")
axes[0].set_ylabel("Number of listings")
 
# Cumulative distribution — what % of listings exceed a given score?
sorted_scores = df["commercialization_score"].sort_values()
axes[1].plot(sorted_scores.values, np.linspace(0, 100, len(sorted_scores)),
             color="#457b9d", linewidth=2)
axes[1].set_title("Cumulative Distribution of Scores", fontweight="bold")
axes[1].set_xlabel("Commercialization Score")
axes[1].set_ylabel("% of listings below this score")
axes[1].axhline(50, color="gray", linestyle="--", alpha=0.5, label="50th percentile")
axes[1].axhline(75, color="orange", linestyle="--", alpha=0.5, label="75th percentile")
axes[1].legend()
 
plt.tight_layout()
plt.savefig("score_distribution.png", dpi=150)
plt.show()