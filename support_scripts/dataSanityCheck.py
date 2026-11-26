import os
from collections import defaultdict, Counter

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

client = MongoClient(os.environ["MONGO_READWRITE_URI"])
db = client["api"]

SEARCH_COLLECTIONS = ["searchEvaluation"]          # add "simulatedSearchEvaluation" to check it too
COMPARISON_COLLECTIONS = ["comparisonEvaluation"]  # add "simulatedComparisonEvaluation" to check it too
CRITERIA = ["fluency", "groundness", "faithfulness"]
VALID_GRADES = {0, 1, 2, 3, 4}
MAX_SHOW = 20


def report(title, items):
    print(f"\n[{'OK' if not items else 'PROBLEM'}] {title}: {len(items)}")
    for item in items[:MAX_SHOW]:
        print(f"    {item}")
    if len(items) > MAX_SHOW:
        print(f"    ... and {len(items) - MAX_SHOW} more")


def check_search(name):
    print(f"\n==================== {name} ====================")
    coll = db[name]

    missing_fields = []
    no_id = []
    dup_in_list = []
    both_lists = []
    doc_count = Counter()
    labels = defaultdict(lambda: defaultdict(set))   # (query, apiId) -> label -> {components}
    components_per_query = defaultdict(set)
    all_components = set()
    n_docs = 0

    for doc in coll.find({}):
        n_docs += 1
        query = doc.get("query")
        component = doc.get("component")
        _id = doc.get("_id")

        for field in ("query", "component", "accepted", "rejected"):
            if field not in doc:
                missing_fields.append(f"{_id}: missing '{field}' ({query!r} / {component})")

        if query is None or component is None:
            continue

        doc_count[(query, component)] += 1
        components_per_query[query].add(component)
        all_components.add(component)

        ids = {}
        for label, field in ((1, "accepted"), (0, "rejected")):
            seen = set()
            for api in doc.get(field) or []:
                api_id = api.get("id") if isinstance(api, dict) else None
                if api_id is None:
                    no_id.append(f"{query!r} / {component} / {field}: {api}")
                    continue
                if api_id in seen:
                    dup_in_list.append(f"{query!r} / {component} / {field}: {api_id}")
                seen.add(api_id)
                ids.setdefault(api_id, set()).add(label)
                labels[(query, api_id)][label].add(component)

        for api_id, ls in ids.items():
            if len(ls) > 1:
                both_lists.append(f"{query!r} / {component}: {api_id}")

    print(f"Documents: {n_docs}, queries: {len(components_per_query)}, systems: {len(all_components)}")

    report("Documents with missing fields", missing_fields)

    report(
        "Duplicate (query, component) documents",
        [f"{q!r} / {c}: {n} documents" for (q, c), n in doc_count.items() if n > 1],
    )

    report("API in both accepted and rejected (same document)", both_lists)
    report("API listed twice in the same list", dup_in_list)
    report("API entries without id", no_id)

    inconsistent = []
    for (query, api_id), by_label in sorted(labels.items(), key=lambda x: str(x[0])):
        if len(by_label) > 1:
            acc = sorted(by_label.get(1, []))
            rej = sorted(by_label.get(0, []))
            inconsistent.append(
                f"{query!r} / {api_id}: accepted in {len(acc)}, rejected in {rej}"
            )
    report("Inconsistent labels for the same (query, API) across systems", inconsistent)

    report(
        "Queries missing some systems",
        [
            f"{q!r}: missing {sorted(all_components - comps)}"
            for q, comps in sorted(components_per_query.items(), key=lambda x: str(x[0]))
            if comps != all_components
        ],
    )

    system_counts = Counter(c for comps in components_per_query.values() for c in comps)
    report(
        "Systems not present for every query",
        [
            f"{c}: {n}/{len(components_per_query)} queries"
            for c, n in sorted(system_counts.items())
            if n != len(components_per_query)
        ],
    )


def check_comparison(name):
    print(f"\n==================== {name} ====================")
    coll = db[name]

    doc_count = Counter()
    bad_grades = []
    missing = []
    n_docs = 0

    for doc in coll.find({}):
        n_docs += 1
        query, model = doc.get("query"), doc.get("model")
        doc_count[(query, model)] += 1
        grades = doc.get("grades") or {}

        for criterion in CRITERIA:
            g = grades.get(criterion)
            if g is None:
                missing.append(f"{query!r} / {model}: no '{criterion}'")
            elif g not in VALID_GRADES:
                bad_grades.append(f"{query!r} / {model}: {criterion}={g!r}")

    print(f"Documents: {n_docs}")
    report(
        "Duplicate (query, model) documents",
        [f"{q!r} / {m}: {n} documents" for (q, m), n in doc_count.items() if n > 1],
    )
    report("Missing grades", missing)
    report("Grades outside 0–4", bad_grades)


for name in SEARCH_COLLECTIONS:
    check_search(name)

for name in COMPARISON_COLLECTIONS:
    check_comparison(name)