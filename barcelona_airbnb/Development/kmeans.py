# KMEANS CLUSTERING 
# Group listings into 4 clusters: casual / informal room rental/ small operator / commercial
# We use the scaled features (not the score) for clustering,
# so the model sees all dimensions, not just our weighted summary.
 
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# First: check if k=4 is actually the right number (elbow + silhouette)
inertias = []
silhouettes = []
k_range = range(2, 8)
 
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(features_df)
    inertias.append(km.inertia_)
    silhouettes.append(silhouette_score(features_df, labels))
 
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(k_range, inertias, "o-", color="#e63946")
axes[0].set_title("Elbow Method — Inertia by k")
axes[0].set_xlabel("Number of clusters (k)")
axes[0].set_ylabel("Inertia")
 
axes[1].plot(k_range, silhouettes, "o-", color="#2a9d8f")
axes[1].set_title("Silhouette Score by k")
axes[1].set_xlabel("Number of clusters (k)")
axes[1].set_ylabel("Silhouette Score (higher = better)")
 
plt.tight_layout()
plt.savefig("kmeans_evaluation.png", dpi=150)
plt.show()
 
print("\nSilhouette scores by k:")
for k, s in zip(k_range, silhouettes):
    print(f"  k={k}: {s:.4f}")
 
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df["cluster_raw"] = kmeans.fit_predict(features_df)

# Re-label clusters by mean commercialization score so they're interpretable
cluster_mean_scores = df.groupby("cluster_raw")["commercialization_score"].mean()
score_rank = cluster_mean_scores.rank().astype(int)
label_map = {
    score_rank[score_rank == 1].index[0]: "casual",
    score_rank[score_rank == 2].index[0]: "medium_term_room_rental",
    score_rank[score_rank == 3].index[0]: "commercial",
    score_rank[score_rank == 4].index[0]: "medium_term_home_rental"}
df["operator_type"] = df["cluster_raw"].map(label_map)

print("\nCluster sizes:")
print(df["operator_type"].value_counts())
print(df["operator_type"].value_counts(normalize=True).mul(100).round(1).astype(str) + "%")
 
print("\nMean commercialization score by cluster:")
print(df.groupby("operator_type")["commercialization_score"].mean().round(1))


 