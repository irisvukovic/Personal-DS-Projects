# FINAL SUMMARY 
 
high_pressure = nbh_reliable[nbh_reliable["hpi"] >= nbh_reliable["hpi"].quantile(0.75)]
low_pressure  = nbh_reliable[nbh_reliable["hpi"] <= nbh_reliable["hpi"].quantile(0.25)]
 
print("\n" + "="*55)
print("PHASE 3 SUMMARY — HOUSING PRESSURE INDEX")
print("="*55)
print(f"Neighbourhoods analysed:     {len(nbh_reliable)}")
print(f"Mean HPI:                    {nbh_reliable['hpi'].mean():.1f}")
print(f"Highest pressure:            {nbh_reliable.loc[nbh_reliable['hpi'].idxmax(), 'neighbourhood']} ({nbh_reliable['hpi'].max():.1f})")
print(f"Lowest pressure:             {nbh_reliable.loc[nbh_reliable['hpi'].idxmin(), 'neighbourhood']} ({nbh_reliable['hpi'].min():.1f})")
print(f"\nTop quartile (high pressure) neighbourhoods:")
for _, r in high_pressure.nlargest(5, "hpi").iterrows():
    print(f"  {r['neighbourhood']:<40} HPI: {r['hpi']:.1f}")
print(f"\nBottom quartile (low pressure) neighbourhoods:")
for _, r in low_pressure.nsmallest(5, "hpi").iterrows():
    print(f"  {r['neighbourhood']:<40} HPI: {r['hpi']:.1f}")
print("="*55)