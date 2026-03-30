# BUILD COMMERCIALIZATION SCORE
# Weighted average of all features → single score 0–100.
#
# Weights reflect relative importance to commercial detection:
# - Host scale and entire home are the strongest signals
# - Availability matters a lot too
# - review freq, min nights are supporting signals
 
weights = {
    "feat_host_scale":        0.30,  # strongest signal — multi-property = commercial
    "feat_entire_home":       0.30,  # whole apt off housing market
    "feat_availability":      0.20,  # always available = not your home
    "feat_short_min_nights":  0.10, # tourist-optimized
    "feat_regulatory_arbitrage": 0.10  # regulatory risk increases commercial likelihood

}
 
# Verify weights sum to 1
assert abs(sum(weights.values()) - 1.0) < 1e-9, "Weights must sum to 1"
 
score = sum(features_df[col] * w for col, w in weights.items()) * 100
df["commercialization_score"] = score.round(1)
 
print("\nCommercialization Score — summary stats:")
print(df["commercialization_score"].describe().round(2))