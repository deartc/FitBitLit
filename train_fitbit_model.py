"""Train and evaluate a Fitbit calorie prediction model."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

REQUIRED_COLUMNS = {
    "Duration",
    "Date",
    "Pulse",
    "Steps",
    "Calories",
    "Exerciser",
}


def load_data(csv_path: Path, additional_paths: list[Path] | None = None) -> pd.DataFrame:
    """Load the CSV and add date-derived features used by the model."""
    paths = [csv_path, *(additional_paths or [])]
    data = pd.concat((pd.read_csv(path) for path in paths), ignore_index=True)
    missing_columns = REQUIRED_COLUMNS.difference(data.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Missing required columns: {missing}")

    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data["DayOfWeek"] = data["Date"].dt.dayofweek
    data["DayOfYear"] = data["Date"].dt.dayofyear
    data = data.dropna(subset=["Calories"]).copy()
    if data.empty:
        raise ValueError("No rows with a known Calories target remain after cleaning.")
    return data


def build_pipeline() -> Pipeline:
    numeric_features = ["Duration", "Pulse", "Steps", "DayOfWeek", "DayOfYear"]
    categorical_features = ["Exerciser"]

    preprocess = ColumnTransformer(
        transformers=[
            (
                "numeric",
                Pipeline([("imputer", SimpleImputer(strategy="median"))]),
                numeric_features,
            ),
            (
                "categorical",
                Pipeline(
                    [
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("onehot", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                categorical_features,
            ),
        ]
    )

    return Pipeline(
        [
            ("preprocess", preprocess),
            (
                "model",
                RandomForestRegressor(
                    n_estimators=300,
                    random_state=42,
                    min_samples_leaf=2,
                    n_jobs=-1,
                ),
            ),
        ]
    )


def train_model(
    csv_path: Path,
    output_dir: Path,
    additional_paths: list[Path] | None = None,
) -> dict[str, float | int]:
    paths = [csv_path, *(additional_paths or [])]
    raw_data = pd.concat((pd.read_csv(path) for path in paths), ignore_index=True)
    data = load_data(csv_path, additional_paths)
    features = ["Duration", "Pulse", "Steps", "DayOfWeek", "DayOfYear", "Exerciser"]
    X = data[features]
    y = data["Calories"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_test)

    metrics: dict[str, float | int] = {
        "rows_loaded": int(len(raw_data)),
        "rows_dropped_missing_calories": int(raw_data["Calories"].isna().sum()),
        "rows_with_known_calories": int(len(data)),
        "rows_used_for_training": int(len(X_train)),
        "rows_used_for_testing": int(len(X_test)),
        "mean_absolute_error": float(mean_absolute_error(y_test, predictions)),
        "root_mean_squared_error": float(mean_squared_error(y_test, predictions) ** 0.5),
        "r2_score": float(r2_score(y_test, predictions)),
    }

    output_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, output_dir / "fitbit_calorie_model.joblib")
    (output_dir / "training_metrics.json").write_text(
        json.dumps(metrics, indent=2) + "\n", encoding="utf-8"
    )

    predictions_frame = X_test.copy()
    predictions_frame["ActualCalories"] = y_test
    predictions_frame["PredictedCalories"] = predictions
    predictions_frame.to_csv(output_dir / "fitbit_predictions.csv", index=False)
    return metrics


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=Path("increaseddata.csv"))
    parser.add_argument("--additional-data", type=Path, action="append", default=[])
    parser.add_argument("--output-dir", type=Path, default=Path("model_output"))
    args = parser.parse_args()

    metrics = train_model(args.data, args.output_dir, args.additional_data)
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
