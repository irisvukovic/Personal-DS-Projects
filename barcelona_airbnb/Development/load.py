import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
# LOAD DATA
df = pd.read_csv("listings.csv.gz", low_memory=False)
 
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
 