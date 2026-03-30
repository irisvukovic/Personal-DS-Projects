import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
 
#LOAD & CLEAN 
 
df = pd.read_csv("listings.csv.gz", low_memory=False)
 
# Clean price
df["price_clean"] = (
    df["price"].astype(str)
    .str.replace("[$,]", "", regex=True)
    .pipe(pd.to_numeric, errors="coerce")
)
 
# License flag (from EDA)
def looks_like_hutb(val):
    if pd.isnull(val):
        return 0
    val = str(val).strip().upper()
    return 1 if val.startswith("HUTB") else 0
 
df["has_valid_license"] = df["license"].apply(looks_like_hutb)
 
print(f"Loaded {len(df):,} listings")
print(f"Columns available: {df.shape[1]}")

before = len(df)

df = df[df["room_type"] != "Hotel room"]
df = df[~df["name"].str.contains("hostel|Hostel|HOSTEL", na=False)]

after = len(df)
print(f"Removed {before - after} hotel/hostel listings ({before} → {after})")

df = df[df["availability_365"] > 0]
after2 = len(df)
print(f"Removed {after - after2} inactive listings ({after} → {after2})")
