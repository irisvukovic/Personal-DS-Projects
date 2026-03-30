from sklearn.preprocessing import MinMaxScaler
import pandas as pd
# NORMALIZE FEATURES TO 0–1
# MinMaxScaler so no single feature dominates due to scale.
# host_scale can be 1-50+, availability is 0-365, etc.
 
scaler = MinMaxScaler()
features_scaled = scaler.fit_transform(df[feature_cols])
features_df = pd.DataFrame(features_scaled, columns=feature_cols, index=df.index)
 
print("\nFeatures after scaling (should all be 0–1):")
print(features_df.describe().round(2))
 