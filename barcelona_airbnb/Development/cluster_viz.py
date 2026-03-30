# CLUSTER PROFILE 
# What does each cluster actually look like?
 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 

print(df.groupby("operator_type")[["calculated_host_listings_count", 
                                    "minimum_nights",
                                    "availability_365"]].mean().round(1).to_string())
print(df.groupby("operator_type")["room_type"].value_counts(normalize=True).mul(100).round(1).to_string())

profile_cols = feature_cols + ["commercialization_score", "price_clean"]
profile = df.groupby("operator_type")[profile_cols].mean().round(2)
print("\nCluster profiles (mean values):")
print(profile.T)
 
fig, ax = plt.subplots(figsize=(10, 5))

# Use scaled feature means per cluster for the heatmap
features_df["operator_type"] = df["operator_type"].values

heatmap_data = features_df.groupby("operator_type")[feature_cols].mean()
heatmap_data.columns = [
    "Host Scale", "Availability",
    "Short Min Nights", "Entire Home", "Regular Arbitrage"
]

sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=".2f",
    cmap="RdYlGn_r",      # red = more commercial, green = less
    linewidths=0.5,
    linecolor="white",
    ax=ax,
    vmin=0, vmax=1
)

ax.set_title("Feature Profiles by Operator Type\n(0 = least commercial, 1 = most)",
             fontweight="bold", pad=15)
ax.set_xlabel("")
ax.set_ylabel("")
plt.xticks(rotation=30, ha="right")
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig("cluster_heatmap.png", dpi=150)
plt.show()