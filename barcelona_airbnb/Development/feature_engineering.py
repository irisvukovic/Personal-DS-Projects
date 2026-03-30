# FEATURE ENGINEERING 
# Each feature captures a different dimension of commercial behavior.
# Higher value = more commercial in every case (important for scoring).
 
# 1a. Host scale — how many listings does this host have?
#     Use calculated_host_listings_count (more reliable than host_listings_count)
df["feat_host_scale"] = df["calculated_host_listings_count"].fillna(1)
 
# 1b. Availability — always-on = not your actual home
#     Clip at 365, fill missing with median

df["feat_availability"] = df["availability_365"].fillna(
    df["availability_365"].median()
)
 
# 1c. Minimum nights — low minimum = optimized for tourists, not longer stays
#     INVERT: low minimum_nights → high commercial score
# 0 = long stay (>30), 0.5 = medium (7-30), 1 = tourist (1-6)
def min_nights_category(n):
    if n <= 6:
        return 1.0    # tourist optimized
    elif n <= 30:
        return 0.5    # medium
    else:
        return 0.0    # long stay / regulatory arbitrage

df["feat_short_min_nights"] = df["minimum_nights"].apply(min_nights_category)

# 1d. Entire home — takes the whole unit off the residential market
df["feat_entire_home"] = (df["room_type"] == "Entire home/apt").astype(int)

# 1e. Feature specifically designed to catch regulatory arbitrage
# Scores highest for listings with minimums just above 30 days
df["feat_regulatory_arbitrage"] = (
    df["minimum_nights"].between(30, 35)
).astype(int)

 
# Collect all feature columns
feature_cols = [
    "feat_host_scale",
    "feat_availability",
    "feat_short_min_nights",
    "feat_entire_home",
    "feat_regulatory_arbitrage"]
 
print("\nFeature summary (raw, before scaling):")
print(df[feature_cols].describe().round(2))
 