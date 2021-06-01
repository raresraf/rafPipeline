import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from rComplexity.features.feature_transformation import extract_features, LOG_POLYNOMIAL_FEATURE_TYPE, \
    FRACTIONAL_POWER_FEATURE_TYPE, POLYNOMIAL_FEATURE_TYPE, POWER_FEATURE_TYPE, FACTORIAL_FEATURE_TYPE, \
    LOGLOG_POLYNOMIAL_FEATURE_TYPE

CONFIGS = [
    (LOGLOG_POLYNOMIAL_FEATURE_TYPE, 0),
    (LOGLOG_POLYNOMIAL_FEATURE_TYPE, 1),
    (LOGLOG_POLYNOMIAL_FEATURE_TYPE, 2),
    (LOGLOG_POLYNOMIAL_FEATURE_TYPE, 3),
    (LOG_POLYNOMIAL_FEATURE_TYPE, 0),
    (LOG_POLYNOMIAL_FEATURE_TYPE, 1),
    (LOG_POLYNOMIAL_FEATURE_TYPE, 2),
    (LOG_POLYNOMIAL_FEATURE_TYPE, 3),
    (LOG_POLYNOMIAL_FEATURE_TYPE, 4),
    (LOG_POLYNOMIAL_FEATURE_TYPE, 5),
    (LOG_POLYNOMIAL_FEATURE_TYPE, 6),
    (LOG_POLYNOMIAL_FEATURE_TYPE, 7),
    (LOG_POLYNOMIAL_FEATURE_TYPE, 8),
    (LOG_POLYNOMIAL_FEATURE_TYPE, 9),
    (LOG_POLYNOMIAL_FEATURE_TYPE, 10),
    (FRACTIONAL_POWER_FEATURE_TYPE, 0.1),
    (FRACTIONAL_POWER_FEATURE_TYPE, 0.2),
    (FRACTIONAL_POWER_FEATURE_TYPE, 0.3),
    (FRACTIONAL_POWER_FEATURE_TYPE, 0.4),
    (FRACTIONAL_POWER_FEATURE_TYPE, 0.5),
    (FRACTIONAL_POWER_FEATURE_TYPE, 0.6),
    (FRACTIONAL_POWER_FEATURE_TYPE, 0.7),
    (FRACTIONAL_POWER_FEATURE_TYPE, 0.8),
    (FRACTIONAL_POWER_FEATURE_TYPE, 0.9),
    (POLYNOMIAL_FEATURE_TYPE, 1),
    (POLYNOMIAL_FEATURE_TYPE, 1.3),
    (POLYNOMIAL_FEATURE_TYPE, 1.5),
    (POLYNOMIAL_FEATURE_TYPE, 1.7),
    (POLYNOMIAL_FEATURE_TYPE, 2),
    (POLYNOMIAL_FEATURE_TYPE, 2.5),
    (POLYNOMIAL_FEATURE_TYPE, 2.7),
    (POLYNOMIAL_FEATURE_TYPE, 3),
    (POLYNOMIAL_FEATURE_TYPE, 3.5),
    (POLYNOMIAL_FEATURE_TYPE, 4),
    (POLYNOMIAL_FEATURE_TYPE, 4.5),
    (POLYNOMIAL_FEATURE_TYPE, 5),
    (POLYNOMIAL_FEATURE_TYPE, 5.5),
    (POLYNOMIAL_FEATURE_TYPE, 6),
    (POLYNOMIAL_FEATURE_TYPE, 7),
    (POLYNOMIAL_FEATURE_TYPE, 8),
    (POLYNOMIAL_FEATURE_TYPE, 9),
    (POLYNOMIAL_FEATURE_TYPE, 10),
    (POWER_FEATURE_TYPE, 1.5),
    (POWER_FEATURE_TYPE, 2),
    (POWER_FEATURE_TYPE, 2.5),
    (POWER_FEATURE_TYPE, 3),
    (POWER_FEATURE_TYPE, 3.5),
    (POWER_FEATURE_TYPE, 4),
    (POWER_FEATURE_TYPE, 5),
    (FACTORIAL_FEATURE_TYPE, 1),
]


def get_best_feature(X, y):
    np.seterr(all='raise')
    best_rmse = np.inf
    best_config = None
    best_coef = None
    for config in CONFIGS:
        feature_type = config[0]
        feature_val = config[1]
        try:
            Xc = extract_features(X, feature_type, feature_val)

            regression_model = LinearRegression(fit_intercept=False)
            regression_model.fit(Xc, y)

            y_predicted = regression_model.predict(Xc)
            rmse = mean_squared_error(y, y_predicted)
            if rmse < best_rmse:
                best_rmse = rmse
                best_config = config
                best_coef = regression_model.coef_
        except Exception:
            continue

    return best_config, best_coef
