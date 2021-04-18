import numpy as np

"""All possible feature modification types"""
POLYNOMIAL_FEATURE_TYPE = "POLYNOMIAL"
LOG2_POLYNOMIAL_FEATURE_TYPE = "LOG2_POLYNOMIAL"
POWER_FEATURE_TYPE = "POWER"
NO_FEATURE_TYPE = "NO_TYPE"


def extract_features(X=None,
                     feature_type=POLYNOMIAL_FEATURE_TYPE,
                     feature_val=1.0):
    if X is None:
        return None
    if feature_type == POLYNOMIAL_FEATURE_TYPE:
        return extract_polynomial_features(X, feature_val)
    if feature_type == LOG2_POLYNOMIAL_FEATURE_TYPE:
        return extract_log2_polynomial_features(X, feature_val)
    if feature_type == POWER_FEATURE_TYPE:
        return extract_power_features(X, feature_val)
    if feature_type == NO_FEATURE_TYPE:
        return same_features(X, feature_val)


def extract_polynomial_features(X, M):
    M = int(M)
    phi = np.ones((X.size, 2))
    for i in range(X.size):
        phi[i][0] = 1
        phi[i][1] = np.power(X[i], M)
    return phi

def extract_log2_polynomial_features(X, M):
    M = int(M)
    phi = np.ones((X.size, 2))
    for i in range(X.size):
        phi[i][0] = 1
        phi[i][1] = np.log2(X[i]) * np.power(X[i], M)
    return phi


def extract_power_features(X, M):
    phi = np.ones((X.size, 1))
    for i in range(X.size):
        phi[i][0] = np.power(X[i], M)
    return phi


def same_features(X, _M):
    M = 1
    phi = np.ones((X.size, 1))
    for i in range(X.size):
        phi[i][0] = X[i]
    return phi
