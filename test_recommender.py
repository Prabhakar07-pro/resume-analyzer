from recommendation.recommender import recommend_roles

skills = [
    "css",
    "html",
    "javascript",
    "python",
    "sql",
    "django",
    "git",
    "github",
    "numpy",
    "pandas",
    "machine learning",
    "data science"
]

results = recommend_roles(skills)

print("\nRecommended Roles:\n")
for r in results:
    print(f"{r['role']} → {r['score']*100:.0f}% match")
