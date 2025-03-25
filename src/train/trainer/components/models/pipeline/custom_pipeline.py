from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

class CustomPipeline:
    def __init__(self) -> None:
        pass

    def build_model(self, model):
        pipeline = Pipeline(steps=[
            ('model', model)
        ])
        return pipeline