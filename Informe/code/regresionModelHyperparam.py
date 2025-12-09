# Definimos los modelos y sus grids
models = {
    "Lasso": {
        "estimator": Lasso(max_iter=10000, random_state=42),
        "param_grid": {"model__alpha": [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]}
    },
    "Ridge": {
        "estimator": Ridge(max_iter=10000, random_state=42),
        "param_grid": {"model__alpha": [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]}
    },
    "DecisionTree": {
        "estimator": DecisionTreeRegressor(random_state=42),
        "param_grid": {
            "model__max_depth": [1, 2, 3, 5, 10, 20, None],
            "model__min_samples_split": [2, 5, 10],
            "model__min_samples_leaf": [1, 2, 4]
        }
    },
    "RandomForest": {
        "estimator": RandomForestRegressor(random_state=42),
        "param_grid": {
            "model__n_estimators": [1, 50, 100, 200],
            "model__max_depth": [1, 3, 5, 10, 20, None],
            "model__min_samples_split": [2, 5],
            "model__min_samples_leaf": [1, 2]
        }
    },
    "GradientBoosting": {
        "estimator": GradientBoostingRegressor(random_state=42),
        "param_grid": {
            "model__n_estimators": [50, 100, 200],
            "model__learning_rate": [0.05, 0.1, 0.2],
            "model__max_depth": [1, 2, 3, 5, 7],
            "model__min_samples_split": [2, 5]
        }
    }
}
