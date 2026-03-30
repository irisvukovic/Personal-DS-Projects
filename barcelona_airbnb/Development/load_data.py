import sys
import subprocess
import os

# Ensure geo packages are available in this block's environment
_geo_path = "/tmp/geo_packages"
os.makedirs(_geo_path, exist_ok=True)

# Install packages to the target directory (fast if already cached)
subprocess.run(
    [sys.executable, "-m", "pip", "install", "geopandas", "folium", "--target", _geo_path, "--quiet"],
    check=True
)

# Add to sys.path before importing
if _geo_path not in sys.path:
    sys.path.insert(0, _geo_path)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import geopandas as gpd
import folium
from sklearn.preprocessing import MinMaxScaler

# LOAD DATA
df = pd.read_csv("listings_scored.csv")
geo = gpd.read_file("neighbourhoods.geojson")

print(f"Listings loaded: {len(df):,}")
print(f"Neighbourhoods in geojson: {len(geo)}")
print(f"\nGeoJSON columns: {geo.columns.tolist()}")

# Check the neighborhood column name in geojson
print("\nSample neighbourhood names from geojson:")
print(geo.iloc[:, 0:3].head(10))

print("\nSample neighbourhood names from listings:")
print(df["neighbourhood_cleansed"].value_counts().head(10))
 