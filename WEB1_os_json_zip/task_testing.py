import json
import sys

with open('scoring.json', 'r', encoding='utf=8') as f:
    data = json.load(f)

total_result = 0

for i, verdict in enumerate(sys.stdin.readlines()):
    for el in data["scoring"]:
        if i + 1 in el['required_tests']:
            if verdict.strip() == 'ok':
                total_result += el['points']
            break

print(total_result)
