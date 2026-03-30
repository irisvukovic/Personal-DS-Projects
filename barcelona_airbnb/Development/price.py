import matplotlib.pyplot as plt
import pandas as pd
# PRICE 
# Clean price column (it's stored as "$1,234.00" string)
 
df["price_clean"] = (
    df["price"]
    .astype(str)
    .str.replace("[$,]", "", regex=True)
    .pipe(pd.to_numeric, errors="coerce")
)
 
print("\nPrice (cleaned) — summary stats:")
print(df["price_clean"].describe())
 
# Remove extreme outliers for visualization
price_filtered = df["price_clean"][(df["price_clean"] > 0) & (df["price_clean"] < 600)]
fig, ax = plt.subplots(figsize=(8, 4))
price_filtered.plot(kind="hist", bins=60, ax=ax, color="#f4a261")
ax.set_title("Nightly Price Distribution (€0–600)")
ax.set_xlabel("Price (€)")
plt.tight_layout()
plt.savefig("price_distribution.png", dpi=150)
plt.show()
 