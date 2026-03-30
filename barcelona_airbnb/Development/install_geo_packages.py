import subprocess
import sys

# Install geospatial packages to a user-writable target directory
packages = ["geopandas", "folium"]

for pkg in packages:
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", pkg, "--target", "/tmp/geo_packages", "--quiet"],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print(f"✅ {pkg} installed successfully")
    else:
        print(f"❌ {pkg} install failed:\n{result.stderr}")

# Add the install target to the path so imports work
import os
geo_path = "/tmp/geo_packages"
if geo_path not in sys.path:
    sys.path.insert(0, geo_path)

# Verify imports work
import geopandas as gpd
import folium

print(f"\n✅ geopandas version: {gpd.__version__}")
print(f"✅ folium version: {folium.__version__}")
print("\nGeo packages are ready for downstream use.")
