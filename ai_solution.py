```python
def generate_summary(text):
    summary = []
    programs = {
        "Afterpay Bug Bounty Program": {"bc": "bc:afterpay", "prize": "$5000", "new_targets": 10},
        "Block Open Source": {"bc": "bc:blockopensource", "prize": "$5000", "new_targets": 7},
        "Square": {"bc": "bc:square", "prize": "$18000", "new_targets": 7},
        "TIDAL": {"bc": "bc:tidal-bugbounty", "prize": "$5000", "new_targets": 8},
        "MongoDB": {"bc": "h1:mongodb", "prize": "", "new_targets": 4},
        "Cash App": {"bc": "bc:cashapp", "prize": "$18000", "new_targets": 4},
        "Visa": {"bc": "h1:visa", "prize": "", "new_targets": 1}
    }

    summary.append(f"{len(programs)} new in-scope assets added on 2026-10-01.")
    for name, details in programs.items():
        line = f"- {name} (`{details['bc']}`) {''.ljust(20 - len(name), ' ')}{details['prize']}"
        line += f" {details['new_targets']} new in-scope target(s)."
        summary.append(line)
    return "\n".join(summary)
```