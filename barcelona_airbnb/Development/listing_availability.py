import matplotlib.pyplot as plt

# AVAILABILITY 
# High availability_365 = listing is always open i.e. not someone's actual home
 
print("\navailability_365 — summary stats:")
print(df["availability_365"].describe())
 
fig, ax = plt.subplots(figsize=(8, 4))
df["availability_365"].plot(kind="hist", bins=50, ax=ax, color="#2a9d8f")
ax.set_title("availability_365 Distribution")
ax.set_xlabel("Days available per year")
ax.set_ylabel("Count")
# Notable thresholds
ax.axvline(90, color="red", linestyle="--", alpha=0.7, label="90 days")
ax.axvline(180, color="orange", linestyle="--", alpha=0.7, label="180 days")
ax.legend()
plt.tight_layout()
plt.savefig("availability_distribution.png", dpi=150)
plt.show()
 
# What % are available more than 180 days/year?
high_avail = (df["availability_365"] > 180).mean() * 100
print(f"\nListings available >180 days/year: {high_avail:.1f}%")
 
 