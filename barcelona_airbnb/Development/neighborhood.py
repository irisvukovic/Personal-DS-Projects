import matplotlib.pyplot as plt
# NEIGHBORHOOD OVERVIEW 
# Which neighborhoods have the most listings?
 
nbh_counts = df["neighbourhood_cleansed"].value_counts()
print(f"\nTotal neighborhoods: {len(nbh_counts)}")
print("\nTop 15 neighborhoods by listing count:")
print(nbh_counts.head(15))
 
fig, ax = plt.subplots(figsize=(10, 5))
nbh_counts.head(15).sort_values().plot(kind="barh", ax=ax, color="#e9c46a")
ax.set_title("Top 15 Neighborhoods by Airbnb Listing Count", fontweight="bold")
ax.set_xlabel("Number of listings")
plt.tight_layout()
plt.savefig("neighborhood_counts.png", dpi=150)
plt.show()
 
# Entire home % by neighborhood (preview of Phase 3)
entire_home_by_nbh = (
    df.groupby("neighbourhood_cleansed")["room_type"]
    .apply(lambda x: (x == "Entire home/apt").mean() * 100)
    .sort_values(ascending=False)
)
print("\nTop 10 neighborhoods by % entire-home listings:")
print(entire_home_by_nbh.head(10).round(1).astype(str) + "%")
