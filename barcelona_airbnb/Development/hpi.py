# COMPUTE HOUSING PRESSURE INDEX (HPI) 
# Normalize each metric to 0–1, then compute weighted average.
# Higher score = more pressure on residential housing.
 
from sklearn.preprocessing import MinMaxScaler

hpi_features = [
    "pct_entire_home",
    "pct_high_confidence",
    "mean_comm_score",
    "mean_availability",
    "pct_commercial_type",
]
 
scaler = MinMaxScaler()
nbh_scaled = nbh.copy()
nbh_scaled[hpi_features] = scaler.fit_transform(nbh[hpi_features])
 
# entire home and confirmed commercial operators
# are the strongest signals of housing displacement
hpi_weights = {
    "pct_entire_home":      0.25,
    "pct_high_confidence":  0.25,
    "mean_comm_score":      0.25,
    "pct_commercial_type":  0.20,
    "mean_availability":    0.05,
}
 
assert abs(sum(hpi_weights.values()) - 1.0) < 1e-9
 
nbh["hpi"] = sum(
    nbh_scaled[col] * w for col, w in hpi_weights.items()
) * 100
 
nbh["hpi"] = nbh["hpi"].round(1)

threshold = 10

nbh_reliable = nbh[nbh["total_listings"] >= threshold].copy()

print(f"Neighbourhoods with at least {threshold} listings: {len(nbh_reliable)}")

print("\nTop 10 highest pressure neighbourhoods (thresholded):")
print(
    nbh_reliable.nlargest(10, "hpi")[
        ["neighbourhood", "hpi", "total_listings", "pct_entire_home", "pct_high_confidence"]
    ].to_string(index=False)
)

print("\nBottom 10 lowest pressure neighbourhoods (thresholded):")
print(
    nbh_reliable.nsmallest(10, "hpi")[
        ["neighbourhood", "hpi", "total_listings", "pct_entire_home", "pct_high_confidence"]
    ].to_string(index=False)
)


print("\nHousing Pressure Index — summary:")
print(nbh["hpi"].describe().round(2))
 
print("\nTop 10 highest pressure neighbourhoods:")
print(
    nbh.nlargest(10, "hpi")[["neighbourhood", "hpi", "total_listings",
                               "pct_entire_home", "pct_high_confidence"]]
    .to_string(index=False)
)
 
print("\nBottom 10 lowest pressure neighbourhoods:")
print(
    nbh.nsmallest(10, "hpi")[["neighbourhood", "hpi", "total_listings",
                                "pct_entire_home", "pct_high_confidence"]]
    .to_string(index=False)
)
 