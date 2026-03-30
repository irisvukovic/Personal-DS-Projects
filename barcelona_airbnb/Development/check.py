# BASIC CHECK
# What's missing? What can we actually use?
 
null_rates = (df.isnull().sum() / len(df) * 100).sort_values(ascending=False)
print("\nNull rates (%):")
print(null_rates[null_rates > 0])
 
# Key columns we need for our project
key_cols = [
    "id", "host_id", "host_listings_count", "host_total_listings_count",
    "neighbourhood_cleansed", "room_type", "price",
    "minimum_nights", "maximum_nights",
    "availability_365", "availability_90", "availability_30",
    "number_of_reviews", "reviews_per_month",
    "calculated_host_listings_count",
    "license"
]
 
print("\nNull rates for KEY columns only:")
print(null_rates[null_rates.index.isin(key_cols)])