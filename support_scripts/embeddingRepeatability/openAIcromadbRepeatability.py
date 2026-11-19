from collections import defaultdict
import json
import chromadb
import numpy as np

chroma_client = chromadb.PersistentClient(path="../../dataRAG/chroma")

def evaluate_embeddings(file_path, collection):
    groups = defaultdict(list)

    chroma_collection = chroma_client.get_collection(name=collection)

    with open(file_path, encoding="utf-8") as file:
        for line in file:
            if line.strip():
                record = json.loads(line)
                groups[record["query_id"]].append(record)

        exact_match_queries = 0
        exact_match_queries_unordered = 0
        total_queries = len(groups)

        for query_id, records in groups.items():
            results = [
                chroma_collection.query(query_embeddings=[record['embedding']], n_results=5)['ids'][0]
                for record in records
            ]

            if results and all(result == results[0] for result in results[1:]):
                exact_match_queries += 1

            if results and all(set(result) == set(results[0]) for result in results[1:]):
                exact_match_queries_unordered += 1

        non_exact_match_queries = total_queries - exact_match_queries
        non_exact_match_queries_unordered = total_queries - exact_match_queries_unordered

        print(f"\nCollection: {collection}")
        print(f"Total queries: {total_queries}")
        print(f"Queries with identical top-5 results: {exact_match_queries}")
        print(f"Queries with non-identical top-5 results: {non_exact_match_queries}")
        print(f"Queries with identical unordered top-5 results: {exact_match_queries_unordered}")
        print(f"Queries with non-identical unordered top-5 results: {non_exact_match_queries_unordered}")

        if total_queries:
            print(
                f"Retrieval consistency: "
                f"{100 * exact_match_queries / total_queries:.2f}%"
            )
            print(
                f"Retrieval unordered consistency: "
                f"{100 * exact_match_queries_unordered / total_queries:.2f}%"
            )

evaluate_embeddings("embedding_OpenAI_determinism.jsonl", "gptAPI")
evaluate_embeddings("embedding_OpenAI_determinism.jsonl", "gptAPImeta")
evaluate_embeddings("embedding_OpenAI_determinism.jsonl", "gptAPIdescriptive")
