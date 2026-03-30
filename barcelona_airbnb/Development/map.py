
# CHOROPLETH MAP 
# Interactive folium map

import sys
import subprocess

# Install geospatial packages inline for this block's execution context
_geo_pkg_path = "/tmp/geo_packages"
_pkgs_needed = ["geopandas", "folium"]

for _p in _pkgs_needed:
    subprocess.run(
        [sys.executable, "-m", "pip", "install", _p,
         "--target", _geo_pkg_path, "--quiet", "--exists-action", "i"],
        capture_output=True
    )

if _geo_pkg_path not in sys.path:
    sys.path.insert(0, _geo_pkg_path)

import pandas as pd
import numpy as np
import geopandas as gpd
import folium

print(f"✅ geopandas {gpd.__version__} | folium {folium.__version__}")

# Merge HPI scores into geodataframe
# Find the right column name to join on
geo_col = [c for c in geo.columns if "neighbourhood" in c.lower() and "group" not in c.lower()][0]
print(f"\nJoining geojson on column: '{geo_col}'")

geo_merged = geo.merge(nbh_reliable, left_on=geo_col, right_on="neighbourhood", how="left")

print(f"Matched neighbourhoods: {geo_merged['hpi'].notna().sum()} / {len(geo_merged)}")

# Check for unmatched neighborhoods
unmatched = geo_merged[geo_merged["hpi"].isna()][geo_col].tolist()
if unmatched:
    print(f"Unmatched (no listing data): {unmatched}")

# Build folium map centered on Barcelona
m = folium.Map(
    location=[41.3851, 2.1734],
    zoom_start=13,
    tiles="CartoDB positron"
)

# Choropleth layer
folium.Choropleth(
    geo_data=geo_merged.__geo_interface__,
    data=nbh_reliable,
    columns=["neighbourhood", "hpi"],
    key_on=f"feature.properties.{geo_col}",
    fill_color="RdYlGn_r",
    fill_opacity=0.75,
    line_opacity=0.3,
    line_color="white",
    legend_name="Housing Pressure Index (0–100)",
    nan_fill_color="#cccccc",
    highlight=True,
).add_to(m)

# Tooltip — click any neighbourhood to see its stats
folium.GeoJson(
    geo_merged.__geo_interface__,
    style_function=lambda f: {
        "fillOpacity": 0,
        "weight": 0,
    },
    tooltip=folium.GeoJsonTooltip(
        fields=[geo_col, "hpi", "total_listings",
                "pct_entire_home", "pct_high_confidence"],
        aliases=["Neighbourhood", "HPI Score", "Total Listings",
                 "% Entire Home", "% High Confidence Commercial"],
        localize=True,
        sticky=True,
        labels=True,
        style="""
            background-color: white;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-family: sans-serif;
            font-size: 12px;
            padding: 8px;
        """
    )
).add_to(m)

m.save("barcelona_hpi_map.html")
print("\n✓ Map saved as barcelona_hpi_map.html")
print(f"✓ Map covers {geo_merged['hpi'].notna().sum()} neighbourhoods with HPI data")
