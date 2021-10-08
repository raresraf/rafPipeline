import json
from collections import OrderedDict

labels = OrderedDict()

for a in range(1, 2000):
    for b in ['A','B','C','D','E','F']:
        labels[f"{a}{b}"] = []

with open('../../../dataset.json', 'r') as f:
    dataset = json.load(f)

for x in dataset:
    if x.get("source", None) != "codeforces":
        continue
    if not x.get("tags", None) or not x.get("index", None):
        continue
    labels[x["index"]]= x["tags"]

with open('labels.json', 'w') as f:
    json.dump(labels, f, sort_keys=False)
