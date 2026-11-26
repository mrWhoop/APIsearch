from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.environ['MONGO_READWRITE_URI'])
db = client["api"]
collection = db["apis"]

fields = ['name', 'description', 'category', 'api_keywords', 'authentication', 'https', 'cors', 'type']

total = 0
trimmed = 0
sizes = []

for doc in collection.find():
    template_parts = []

    for field in fields:
        value = doc.get(field)

        if value is not None:
            template_parts.append(f"{field}: {value}\n")

    template = "".join(template_parts)
    size_bytes = len(template.encode("utf-8"))

    sizes.append(size_bytes)

    if size_bytes > 400:
        trimmed += 1

print(f"Število dokumentov: {len(sizes)}")
print(f"Dokumenti nad omejitvijo: {trimmed}")
print(f"Delež: {trimmed / len(sizes) * 100:.2f}%")
print(f"Povprečna velikost: {sum(sizes) / len(sizes):.2f} B")
print(f"Največja velikost: {max(sizes)} B")