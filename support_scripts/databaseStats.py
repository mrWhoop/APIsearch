from pymongo import MongoClient
import os
from dotenv import load_dotenv
import pandas as pd
import re



load_dotenv()

client = MongoClient(os.environ['MONGO_READWRITE_URI'])
db = client["api"]
collection = db["apis"]

documents = list(collection.find({}, {"_id": 0}))
df = pd.DataFrame(documents)

# --------------------------------------------------
# 1. Dataset size and category distribution
# --------------------------------------------------

categoryCounts = df["category"].value_counts()

print("=== DATASET COMPOSITION ===")
print(f"Total APIs: {len(df)}")
print(f"Number of categories: {df['category'].nunique()}")
print(f"Mean APIs per category: {categoryCounts.mean():.2f}")
print(f"Median APIs per category: {categoryCounts.median():.2f}")
print(f"Minimum APIs per category: {categoryCounts.min()}")
print(f"Maximum APIs per category: {categoryCounts.max()}")
print(f"Standard deviation: {categoryCounts.std():.2f}")
print(f"Coefficient of variation: {categoryCounts.std() / categoryCounts.mean():.3f}")

print("\nAPIs per category:")
print(categoryCounts.sort_values(ascending=False))


# --------------------------------------------------
# 2. Description characteristics
# --------------------------------------------------

def wordCount(value):
    if not isinstance(value, str):
        return 0
    return len(re.findall(r"\b\w+\b", value))

df["descriptionWords"] = df["description"].apply(wordCount)

descriptionStats = df["descriptionWords"].describe(
    percentiles=[0.25, 0.5, 0.75]
)

print("\n=== DESCRIPTION CHARACTERISTICS ===")
print(descriptionStats)

print(f"Missing descriptions: {df['description'].isna().sum()}")
print(f"Empty descriptions: {(df['descriptionWords'] == 0).sum()}")


# --------------------------------------------------
# 3. Keyword characteristics
# --------------------------------------------------

def keywordCount(value):
    if isinstance(value, list):
        return len(value)
    if isinstance(value, str):
        return len([x for x in value.split(",") if x.strip()])
    return 0

df["keywordCount"] = df["api_keywords"].apply(keywordCount)

print("\n=== KEYWORD CHARACTERISTICS ===")
print(df["keywordCount"].describe())

print(f"APIs without keywords: {(df['keywordCount'] == 0).sum()}")


# --------------------------------------------------
# 4. Categorical attributes
# --------------------------------------------------

categoricalFields = [
    "https",
    "authentication",
    "cors",
    "type"
]

print("\n=== CATEGORICAL ATTRIBUTES ===")

for field in categoricalFields:
    print(f"\n{field.upper()}")

    counts = df[field].fillna("Missing").value_counts()

    percentages = (
        df[field].fillna("Missing")
        .value_counts(normalize=True) * 100
    )

    result = pd.DataFrame({
        "Count": counts,
        "Percentage": percentages.round(2)
    })

    print(result)


# --------------------------------------------------
# 5. Numerical attributes
# --------------------------------------------------

numericalFields = [
    "popularity",
    "reliability",
    "latency",
    "price"
]

print("\n=== NUMERICAL ATTRIBUTES ===")

for field in numericalFields:
    if field not in df.columns:
        continue

    values = pd.to_numeric(df[field], errors="coerce").dropna()

    if len(values) == 0:
        continue

    print(f"\n{field.upper()}")
    print(values.describe(
        percentiles=[0.25, 0.5, 0.75]
    ))
