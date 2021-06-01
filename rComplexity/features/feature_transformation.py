import numpy as np

"""All possible feature modification types"""
LOGLOG_POLYNOMIAL_FEATURE_TYPE = "LOGLOG_POLYNOMIAL"
LOG_POLYNOMIAL_FEATURE_TYPE = "LOG_POLYNOMIAL"
FRACTIONAL_POWER_FEATURE_TYPE = "FRACTIONAL_POWER"
POLYNOMIAL_FEATURE_TYPE = "POLYNOMIAL"
POWER_FEATURE_TYPE = "POWER"
FACTORIAL_FEATURE_TYPE = "FACTORIAL"


def extract_features(X=None,
                     feature_type=POLYNOMIAL_FEATURE_TYPE,
                     feature_val=1.0):
    if X is None:
        return None
    if feature_type == LOGLOG_POLYNOMIAL_FEATURE_TYPE:
        return extract_loglog_polynomial_features(X, feature_val)
    if feature_type == LOG_POLYNOMIAL_FEATURE_TYPE:
        return extract_log_polynomial_features(X, feature_val)
    if feature_type == FRACTIONAL_POWER_FEATURE_TYPE:
        return extract_power_features(X, feature_val)
    if feature_type == POLYNOMIAL_FEATURE_TYPE:
        return extract_polynomial_features(X, feature_val)
    if feature_type == POWER_FEATURE_TYPE:
        return extract_power_features(X, feature_val)
    if feature_type == FACTORIAL_FEATURE_TYPE:
        return extract_factorial_features(X, feature_val)


def extract_loglog_polynomial_features(X, M):
    M = int(M)
    phi = np.ones((X.size, 2))
    for i in range(X.size):
        phi[i][0] = 1
        phi[i][1] = np.log2(np.log2(X[i])) * np.power(X[i], M)
    return phi


def extract_log_polynomial_features(X, M):
    M = int(M)
    phi = np.ones((X.size, 2))
    for i in range(X.size):
        phi[i][0] = 1
        phi[i][1] = np.log2(X[i]) * np.power(X[i], M)
    return phi


def extract_polynomial_features(X, M):
    M = int(M)
    phi = np.ones((X.size, 2))
    for i in range(X.size):
        phi[i][0] = 1
        phi[i][1] = np.power(X[i], M)
    return phi


def extract_power_features(X, M):
    phi = np.ones((X.size, 2))
    for i in range(X.size):
        phi[i][0] = 1
        phi[i][1] = np.power(M, X[i])
    return phi


def extract_factorial_features(X, _M):
    phi = np.ones((X.size, 2))
    for i in range(X.size):
        phi[i][0] = 1
        if X[i] < 100:
            phi[i][1] = np.math.factorial(X[i])
        else:
            phi[i][1] = np.inf
    return phi
