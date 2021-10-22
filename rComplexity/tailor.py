# python3 rComplexity/tailor.py ../TheOutputsCodeforces/processed

import json
import os
import sys

import numpy as np

from rComplexity.features.get_best_feature import get_best_feature

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python3 tailor.py <path_to_metrics_directory> ")
        print("sample usage: python3 rComplexity/tailor.py ../TheOutputsCodeforces/processed/ ")
        sys.exit(-1)

    path = sys.argv[1]

    for root, dirs, files in os.walk(path):
        name = 'AGGREGATED.RAF'
        if name not in files:
            continue
        if os.path.exists(os.path.join(root, 'PROCESSED.RAF')):
            continue

        path = os.path.join(root, name)
        with open(path) as f:
            data = json.load(f)

        processed = {}
        for metric in data["metric"].keys():
            X = []
            y = []
            print(metric)
            for k, v in data["metric"][metric].items():
                X.append(int(k))
                y.append(v)

            processed["path"] = path
            if not processed.get("metrics", None):
                processed["metrics"] = {}

            r, coef = get_best_feature(np.array(X), np.array(y))
            print(r)
            print(coef)
            processed["metrics"][metric] = {
                "FEATURE_TYPE": r[0],
                "FEATURE_CONFIG": r[1],
                "INTERCEPT": coef[0],
                "R-VAL": coef[1],
            }

        outname = 'PROCESSED.RAF'
        outpath = os.path.join(root, outname)
        with open(outpath, 'w', encoding='utf-8') as f:
            json.dump(processed, f, ensure_ascii=False, indent=4, sort_keys=True)
