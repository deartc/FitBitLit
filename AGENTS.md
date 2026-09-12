# AGENTS.md

This repository is a small Python data-science project for training a Fitbit calorie prediction model from exercise data.

## Project purpose

- Train and evaluate a regression model that predicts `Calories` from exercise features such as `Duration`, `Pulse`, `Steps`, and the exerciser identity.
- Keep the dataset and model pipeline reproducible from the repository root.
- Use the notebooks for exploration, but treat the Python training script as the canonical implementation for model training and validation.

## Key files

- [README.md](README.md): project overview, dataset notes, and usage instructions.
- [train_fitbit_model.py](train_fitbit_model.py): model training pipeline and CLI entry point.
- [requirements.txt](requirements.txt): Python dependencies.
- [increaseddata.csv](increaseddata.csv): primary dataset.
- [supplemental_fitbit_data.csv](supplemental_fitbit_data.csv): optional synthetic training data.
- [model_output/](model_output/): generated artifacts, including the trained model and metrics.

## How to run the project

From the repository root:

```bash
python -m pip install -r requirements.txt
python train_fitbit_model.py
```

Optional additional training set:

```bash
python train_fitbit_model.py --additional-data supplemental_fitbit_data.csv
```

## Code conventions

- Prefer editing [train_fitbit_model.py](train_fitbit_model.py) when changing training logic, feature engineering, or evaluation behavior.
- Keep generated model files in [model_output/](model_output/) and do not treat those as source code.
- Preserve the pipeline structure: load data, clean missing `Calories`, engineer date features, split into train/test, train a scikit-learn model, and write metrics/output CSVs.
- Use pandas and scikit-learn idioms already present in the project instead of introducing unrelated frameworks.
- When changing data assumptions, update the README and any user-facing instructions that describe the project workflow.

## Validation

After making changes to the training script or dependencies, validate with:

```bash
python train_fitbit_model.py
```

This command should complete successfully and write the expected artifacts into [model_output/](model_output/).

## Notes for AI agents

- The notebooks are exploratory and may contain project-specific instructions for data cleaning or analysis.
- The model training pipeline is the reliable source of truth for dataset validation and metrics.
- Avoid broad refactors that change the training contract unless the README and scripts are updated together.
