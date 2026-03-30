# CORRELATION ANALYSIS 
# Which individual metrics drive HPI the most?
# Useful for writeup and shows analytical depth.

import matplotlib.pyplot as plt

print("\nCorrelation with HPI:")
corr = nbh_reliable[hpi_features + ["hpi"]].corr()["hpi"].drop("hpi").sort_values(ascending=False)
print(corr.round(3))
 
fig, ax = plt.subplots(figsize=(7, 4))
colors = ["#e63946" if v > 0 else "#457b9d" for v in corr.values]
corr.plot(kind="barh", ax=ax, color=colors)
ax.set_title("Feature Correlation with Housing Pressure Index", fontweight="bold")
ax.set_xlabel("Pearson correlation coefficient")
ax.axvline(0, color="black", linewidth=0.8)
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("hpi_correlations.png", dpi=150)
plt.show()
 
 