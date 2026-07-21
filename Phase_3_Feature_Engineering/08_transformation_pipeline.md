# 3.8 — Transformation Pipeline (Train/Serve Parity)

> Reference: Slide 3.8 of `phase3_feature_engineering.html`

## The Golden Rule

```
Whatever you .fit() on training, you must .transform()
with the SAME fitted object at serving time.
NEVER .fit() in production.
```

## House Prices: sklearn Pipeline

```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression

# Preprocessing
preprocessor = ColumnTransformer([
    ('num', Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ]), numerical_cols),
    ('cat', Pipeline([
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ]), categorical_cols)
])

# Full pipeline = preprocess + model (ONE object)
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
])

# Train — everything is .fit() together
pipeline.fit(X_train, y_train)

# Serve — .predict() uses fitted transforms, no .fit()
prediction = pipeline.predict(X_new)
```

## Save the ENTIRE pipeline with MLflow

```python
mlflow.sklearn.log_model(pipeline, "model")
# Saves: scaler stats + encoder mappings + imputer values + model weights
# ALL in one artifact. No mismatch possible.
```
