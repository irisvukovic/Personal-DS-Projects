# BUILD NEIGHBORHOOD-LEVEL METRICS 
# Each metric captures a different dimension of housing pressure.
 
nbh = df.groupby("neighbourhood_cleansed").agg(
    total_listings        = ("id", "count"),
    pct_entire_home       = ("room_type", lambda x: (x == "Entire home/apt").mean() * 100),
    pct_high_confidence   = ("high_confidence_commercial", "mean"),
    mean_comm_score       = ("commercialization_score", "mean"),
    mean_availability     = ("availability_365", "mean"),
    pct_commercial_type   = ("operator_type", lambda x: x.isin(["commercial", "medium_term_room_rental", "medium_term_home_rental"]).mean() * 100),
).reset_index()
 
nbh = nbh.rename(columns={"neighbourhood_cleansed": "neighbourhood"})
 
print(f"\nNeighbourhoods with data: {len(nbh)}")
print("\nTop 10 by total listings:")
print(nbh.nlargest(10, "total_listings")[["neighbourhood", "total_listings"]].to_string())