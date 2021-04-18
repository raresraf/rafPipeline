import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from rComplexity.features.feature_transformation import extract_features, LOG2_POLYNOMIAL_FEATURE_TYPE, \
    POLYNOMIAL_FEATURE_TYPE, POWER_FEATURE_TYPE

CONFIGS = [
    (POLYNOMIAL_FEATURE_TYPE, 1),
    (POLYNOMIAL_FEATURE_TYPE, 2),
    (POLYNOMIAL_FEATURE_TYPE, 3),
    (POLYNOMIAL_FEATURE_TYPE, 4),
    (POLYNOMIAL_FEATURE_TYPE, 5),
    (POLYNOMIAL_FEATURE_TYPE, 6),
    (POLYNOMIAL_FEATURE_TYPE, 7),
    (POLYNOMIAL_FEATURE_TYPE, 8),
    (POLYNOMIAL_FEATURE_TYPE, 9),
    (POLYNOMIAL_FEATURE_TYPE, 10),
    (LOG2_POLYNOMIAL_FEATURE_TYPE, 1),
    (LOG2_POLYNOMIAL_FEATURE_TYPE, 2),
    (LOG2_POLYNOMIAL_FEATURE_TYPE, 3),
    (LOG2_POLYNOMIAL_FEATURE_TYPE, 4),
    (LOG2_POLYNOMIAL_FEATURE_TYPE, 5),
    (POWER_FEATURE_TYPE, 1),
    (POWER_FEATURE_TYPE, 2),
    (POWER_FEATURE_TYPE, 3),
    (POWER_FEATURE_TYPE, 4),
    (POWER_FEATURE_TYPE, 5),
]
def get_best_feature(X, y):
    best_rmse = np.inf
    best_config = None
    best_coef = None
    for config in CONFIGS:
        feature_type = config[0]
        feature_val = config[1]

        Xc = extract_features(X, feature_type, feature_val)

        regression_model = LinearRegression(fit_intercept=False)
        regression_model.fit(Xc, y)

        y_predicted = regression_model.predict(Xc)
        rmse = mean_squared_error(y, y_predicted)
        if rmse < best_rmse:
            best_rmse = rmse
            best_config = config
            best_coef = regression_model.coef_
    return best_config, best_coef