import requests
import json

API_BASE = "https://php.enigmagenomics.com/api/gene.php?search="
genes = ["AAAS", "BRCA1", "TP53", "CFTR", "EGFR"]

results = []

for symbol in genes:
    url = API_BASE + symbol
    print("Fetching:", url)
    resp = requests.get(url, timeout=30)
    if resp.status_code != 200:
        print("Error:", resp.status_code, "for", symbol)
        continue

    data = resp.json()
    gene_name = data.get("name", symbol)

    # Extract conditions
    conditions = []
    for item in data.get("details", {}).get("conditions", []):
        cond_name = item.get("name")
        if cond_name:
            conditions.append(cond_name)

    results.append({
        "gene": gene_name,
        "conditions": conditions
    })

output_file = "api_5_genes.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("✅ Saved to", output_file)
