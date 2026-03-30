import matplotlib.pyplot as plt
# ROOM TYPE BREAKDOWN 
# How much of the market is entire homes vs shared?
 
print("\nRoom type distribution:")
print(df["room_type"].value_counts())
print(df["room_type"].value_counts(normalize=True).mul(100).round(1).astype(str) + "%")
 
fig, ax = plt.subplots(figsize=(7, 4))
df["room_type"].value_counts().plot(kind="bar", ax=ax, color=["#e63946","#457b9d","#a8dadc","#1d3557"])
ax.set_title("Listings by Room Type", fontweight="bold")
ax.set_xlabel("")
ax.set_ylabel("Count")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("room_type_distribution.png", dpi=150)
plt.show()
 
 