
import json
import numpy as np
from collections import defaultdict
from itertools import combinations


def evaluate_embeddings(file_path, model_name):
    groups = defaultdict(list)

    with open(file_path, encoding="utf-8") as file:
        for line in file:
            if line.strip():
                record = json.loads(line)
                groups[record["query_id"]].append(record)

    queries_non_exact_match = 0
    total_exact_matches = 0
    total_comparisons = 0
    total_close_matches = 0
    all_cosine_similarities = []

    for query_id, records in groups.items():
        embeddings = [
            np.asarray(record["embedding"], dtype=np.float64)
            for record in records
        ]

        if any(
                not np.array_equal(emb1, emb2)
                for emb1, emb2 in combinations(embeddings, 2)
        ):
            queries_non_exact_match += 1

        for emb1, emb2 in combinations(embeddings, 2):
            total_comparisons += 1

            # Exact equality
            if np.array_equal(emb1, emb2):
                total_exact_matches += 1

            # Tolerate slight difference
            if np.allclose(emb1, emb2, rtol=1e-5, atol=1e-8):
                total_close_matches += 1

            # Cosine similarity
            norm1 = np.linalg.norm(emb1)
            norm2 = np.linalg.norm(emb2)

            if norm1 == 0 or norm2 == 0:
                continue

            cosine = np.dot(emb1, emb2) / (norm1 * norm2)
            all_cosine_similarities.append(cosine)

    print(f"\n=== Overall results {model_name} ===")
    print(f"Queries: {len(groups)}")
    print(f"Total comparisons: {total_comparisons}")
    print(
        f"Total exact matches: "
        f"{total_exact_matches}/{total_comparisons}"
    )

    if total_comparisons:
        print(
            f"Exact match percentage: "
            f"{100 * total_exact_matches / total_comparisons:.2f}%"
        )

    print(
        f"Total close matches: "
        f"{total_close_matches}/{total_comparisons}"
    )

    if total_comparisons:
        print(
            f"Exact match percentage: "
            f"{100 * total_close_matches / total_comparisons:.2f}%"
        )

    if all_cosine_similarities:
        cosines = np.asarray(all_cosine_similarities)

        print(f"Valid cosine comparisons: {len(cosines)}")
        print(f"Average cosine similarity: {np.mean(cosines):.12f}")
        print(f"Minimum cosine similarity: {np.min(cosines):.12f}")
        print(f"Maximum cosine similarity: {np.max(cosines):.12f}")
        print(f"P05 cosine similarity: {np.percentile(cosines, 5):.12f}")
        print(f"P95 cosine similarity: {np.percentile(cosines, 95):.12f}")
        print(
            f"Queries with non-exact matches: "
            f"{queries_non_exact_match}/{len(groups)}"
        )


evaluate_embeddings("embedding_OpenAI_determinism.jsonl", "OpenAI")
evaluate_embeddings("embedding_Gemini_determinism.jsonl", "Gemini")
