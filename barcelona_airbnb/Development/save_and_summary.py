# SAVE OUTPUT 
 
output_cols = [
    "id", "host_id", "neighbourhood_cleansed", "room_type",
    "latitude", "longitude", "price_clean",
    "calculated_host_listings_count", "availability_365",
    "reviews_per_month", "minimum_nights",
    "commercialization_score", "operator_type",
    "high_confidence_commercial", "signals_fired"   
]
 
df[output_cols].to_csv("listings_scored.csv", index=False)
print("\n✓ Saved listings_scored.csv")
 
# SUMMARY 
print("\n" + "="*55)
print("SUMMARY")
print("="*55)
casual = df[df["operator_type"] == "casual"]
medrom = df[df["operator_type"] == "medium_term_room_rental"]
medhom = df[df["operator_type"] == "medium_term_home_rental"]
comm = df[df["operator_type"] == "commercial"]
print(f"Casual hosts:        {len(casual):,} ({len(casual)/len(df)*100:.1f}%)")
print(f"Medium-term home rental:  {len(medhom):,} ({len(medhom)/len(df)*100:.1f}%)")
print(f"Medium-term room rental:      {len(medrom):,} ({len(medrom)/len(df)*100:.1f}%)")
print(f"Commercial operators: {len(comm):,} ({len(comm)/len(df)*100:.1f}%)")
print(f"\nMean score — casual:           {casual['commercialization_score'].mean():.1f}")
print(f"Mean score — medium-term home rental:{medhom['commercialization_score'].mean():.1f}")
print(f"Mean score — medium-term room rental:    {medrom['commercialization_score'].mean():.1f}")
print(f"Mean score — commercial:        {comm['commercialization_score'].mean():.1f}")
print("="*55)