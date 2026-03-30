#  HIGH CONFIDENCE FLAGS 
# A listing is "high confidence commercial" when at least 2 of 3
# key signals are above 0.5 (scaled). Gives a cleaner subset
# for Phase 3 without discarding the full scored dataset.
signal_cols = [
    "feat_host_scale",
    "feat_availability",
    "feat_short_min_nights",
    "feat_entire_home",
    "feat_regulatory_arbitrage"
]

# Count how many signals are above 0.5 per listing
# (use the scaled features we already computed)
df["signals_fired"] = (features_df[signal_cols] > 0.5).sum(axis=1)

# High confidence = 3 or more signals
df["high_confidence_commercial"] = (df["signals_fired"] >= 3).astype(int)

# How many listings meet the bar?
hcc = df[df["high_confidence_commercial"] == 1]
print(f"High confidence commercial listings: {len(hcc):,} ({len(hcc)/len(df)*100:.1f}%)")

# How does it break down by cluster?
print("\nHigh confidence % by operator type:")
print(
    df.groupby("operator_type")["high_confidence_commercial"]
    .mean()
    .mul(100)
    .round(1)
    .astype(str) + "%"
)

# Sanity check — what does a high confidence listing look like?
print("\nSample high confidence commercial listings:")
sample_hcc = (
    hcc.sample(5, random_state=42)
    .rename(columns=check_cols)
    [list(check_cols.values()) + ["signals_fired"]]
    .reset_index(drop=True)
)
sample_hcc["Listing Name"] = sample_hcc["Listing Name"].str[:40]
print(sample_hcc.to_string())

# FIX: 'medium_term_operator' was a stale label — the cluster was renamed
# to 'medium_term_home_rental' and 'medium_term_room_rental'. Combine both.
med_term = df[df["operator_type"].isin(["medium_term_home_rental", "medium_term_room_rental"])]
pct_31_32 = (med_term["minimum_nights"].isin([31, 32])).mean() * 100
print(f"\n% of medium-term listings with 31 or 32 day minimum: {pct_31_32:.1f}%")
print(f"Total medium-term listings: {len(med_term):,}")
