import matplotlib.pyplot as plt

# HOST LISTINGS COUNT (the key commercialization signal)
# Most "sharing economy" hosts have 1 listing.
# Multi-listing hosts are likely commercial operators.
 
col = "calculated_host_listings_count"  # use this over host_listings_count (more reliable)
 
print(f"\n{col} — summary stats:")
print(df[col].describe())
 
# How many hosts have more than 1, 5, 10 listings?
for threshold in [1, 2, 5, 10, 20]:
    pct = (df[col] > threshold).mean() * 100
    print(f"  Listings where host has >{threshold} listings: {pct:.1f}%")

 
# Left: full distribution (will be very skewed)
df[col].clip(upper=50).plot(kind="hist", bins=50, color="#e63946")
plt.title("Host Listings Count (clipped at 50)")
plt.xlabel("Number of listings by this host")
 
plt.tight_layout()
plt.savefig("host_listings_distribution.png", dpi=150)
plt.show()
 
 