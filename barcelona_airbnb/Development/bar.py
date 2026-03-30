#STATIC VISUALIZATION — BAR CHART 
# Ranked bar chart of all neighborhoods by HPI.
# Good for portfolio README / presentations.
import matplotlib.pyplot as plt
import numpy as np

nbh_sorted = nbh_reliable.sort_values("hpi", ascending=True)
 
fig, ax = plt.subplots(figsize=(10, 14))
colors = plt.cm.RdYlGn_r(np.linspace(0.1, 0.9, len(nbh_sorted)))
 
bars = ax.barh(nbh_sorted["neighbourhood"], nbh_sorted["hpi"],
               color=colors, edgecolor="none", height=0.7)
 
ax.set_xlabel("Housing Pressure Index (0 = low, 100 = high)", fontsize=11)
ax.set_title("Barcelona Airbnb Housing Pressure by Neighbourhood",
             fontweight="bold", fontsize=13, pad=15)
ax.axvline(nbh["hpi"].mean(), color="#333", linestyle="--",
           alpha=0.6, linewidth=1.2, label=f"Mean: {nbh['hpi'].mean():.1f}")
ax.legend(fontsize=9)
ax.spines[["top", "right", "left"]].set_visible(False)
ax.tick_params(axis="y", labelsize=7)
 
plt.tight_layout()
plt.savefig("hpi_barchart.png", dpi=150, bbox_inches="tight")
plt.show()
 