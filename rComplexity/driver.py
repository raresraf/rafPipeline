import sys

import numpy as np

from rComplexity.features.get_best_feature import get_best_feature

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python3 driver.py <path_to_metrics> ")
        sys.exit(-1)

    path = sys.argv[1]

    X = np.array([1,2,3,4])
    y = np.array([0,1.2,4.3,9.6])

    r = get_best_feature(X, y)
    print(r)
