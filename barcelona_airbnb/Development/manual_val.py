#SPOT-CHECK — MANUAL VALIDATION 

check_cols = {
    "name": "Listing Name",
    "calculated_host_listings_count": "# Host Listings",
    "availability_365": "Avail/yr",
    "room_type": "Room Type",
    "minimum_nights": "Min Nights",
    "reviews_per_month": "Rev/mo",
    "price_clean": "Price €",
    "neighbourhood_cleansed": "Neighbourhood",
    "commercialization_score": "Score",
}

# Dynamically get actual cluster names from the data to avoid hardcoding errors
manual_val_clusters = sorted(df["operator_type"].unique())

for cluster in manual_val_clusters:
    cluster_df = df[df["operator_type"] == cluster]
    n = min(10, len(cluster_df))
    sample = (
        cluster_df
        .sample(n, random_state=1)
        .rename(columns=check_cols)
        [list(check_cols.values())]
        .reset_index(drop=True)
    )
    # Truncate long listing names
    sample["Listing Name"] = sample["Listing Name"].str[:40]
    
    print(f"\n{'='*40}")
    print(f"  {cluster.upper().replace('_',' ')}  (n={len(cluster_df):,})")
    print(f"{'='*40}")
    print(sample.to_string(index=True))
