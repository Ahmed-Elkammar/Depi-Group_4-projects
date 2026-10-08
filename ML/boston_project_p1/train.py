"""Train the Decision Tree exactly as in the solved notebook and save it to model.joblib.

Same steps as the notebook:
  * 80/20 split, random_state=1
  * GridSearchCV over max_depth 1..10, scored with R2, cv = ShuffleSplit(10 splits, 20%, random_state=0)
  * the deployed model is the best estimator fitted on the training split only,
    so the saved test metrics describe exactly the model that is served.
"""
import json
import warnings

import joblib
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, make_scorer, r2_score
from sklearn.model_selection import GridSearchCV, ShuffleSplit, train_test_split
from sklearn.tree import DecisionTreeRegressor

warnings.filterwarnings("ignore")

data = pd.read_csv("housing.csv")
features, prices = data.drop("MEDV", axis=1), data["MEDV"]
X_train, X_test, y_train, y_test = train_test_split(
    features, prices, test_size=0.2, random_state=1
)

cv_sets = ShuffleSplit(n_splits=10, test_size=0.20, random_state=0)
grid = GridSearchCV(
    DecisionTreeRegressor(random_state=0),
    {"max_depth": list(range(1, 11))},
    scoring=make_scorer(r2_score),
    cv=cv_sets,
).fit(X_train, y_train)

model = grid.best_estimator_
pred = model.predict(X_test)
metrics = {
    "model": "Decision Tree (max_depth=%d)" % model.get_params()["max_depth"],
    "best_params": grid.best_params_,
    "cv_r2": round(grid.best_score_, 4),
    "test_r2": round(r2_score(y_test, pred), 4),
    "test_mae": round(mean_absolute_error(y_test, pred), 2),
    "test_rmse": round(mean_squared_error(y_test, pred) ** 0.5, 2),
    "n_train": len(X_train),
    "feature_ranges": {
        c: [float(features[c].min()), float(features[c].max())] for c in features
    },
}
joblib.dump(model, "model.joblib")
json.dump(metrics, open("metrics.json", "w"), indent=2)
print(json.dumps(metrics, indent=2))
