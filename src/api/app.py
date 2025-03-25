from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split, GridSearchCV


features_df_base = pd.read_csv("../../data/processed/features.csv")
features_df_base = features_df_base.drop(columns=["Unnamed: 0"])
plataform_df_base = pd.read_csv("../../data/processed/plataform_data.csv")


if '' in features_df_base.columns:
    features_df_base = features_df_base.drop(columns=[''])

features_df_base.columns = [
    col.strip().replace(" ", "_").replace("&", "and").replace("-", "_") 
    for col in features_df_base.columns
]

app = FastAPI()

class FavoriteRequest(BaseModel):
    favorite_ids: List[str]

@app.post("/recommend")
def recommend_movies(data: FavoriteRequest):
    favorite_ids = data.favorite_ids

    if not favorite_ids:
        raise HTTPException(status_code=400, detail="Lista de IDs favorita está vazia.")

    features_df = features_df_base.copy()
    plataform_df = plataform_df_base.copy()


    plataform_df["label"] = plataform_df["imdbId"].apply(lambda x: 1 if x in favorite_ids else 0)
    X = features_df
    y = plataform_df["label"]

    # Treino/validação
    model = LGBMClassifier(
    class_weight='balanced',
    random_state=42,
    learning_rate=0.05,
    max_depth=5,
    min_child_samples=10,
    num_leaves=20
    )

    model.fit(X, y)


    y_proba = model.predict_proba(X)[:, 1]
    plataform_df["prob_like"] = y_proba

    recommendations = plataform_df[~plataform_df["imdbId"].isin(favorite_ids)].copy()
    recommendations = recommendations.sort_values(by="prob_like", ascending=False).head(10)
    
    recommended_ids = recommendations["imdbId"].tolist()
    return {"recommended_ids": recommended_ids}
