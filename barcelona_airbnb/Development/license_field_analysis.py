import pandas as pd

# LICENSE FIELD 
# This will be messy. 
 
print("\nLicense field — null rate:")
print(f"  Missing: {df['license'].isnull().mean()*100:.1f}%")
 
print("\nSample of non-null license values:")
print(df["license"].dropna().value_counts().head(20))
 
# Flag: does it look like a real HUT license?
# Barcelona HUT licenses follow pattern: HUTB-XXXXXX-XX
def looks_like_hutb(val):
    if pd.isnull(val):
        return "missing"
    val = str(val).strip().upper()
    if val.startswith("HUTB"):
        return "has_hutb"
    if val in ["", "N/A", "NA", "NONE", "NO REQUERIDO", "EXEMPT"]:
        return "blank_or_exempt"
    return "other_value"
 
df["license_status"] = df["license"].apply(looks_like_hutb)
print("\nLicense status breakdown:")
print(df["license_status"].value_counts())
print(df["license_status"].value_counts(normalize=True).mul(100).round(1).astype(str) + "%")