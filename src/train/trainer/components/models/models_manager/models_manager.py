from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

class ModelsManager():
    def __init__(self) -> None:
        self.model_dict = {
            "RandomForestClassifier": RandomForestClassifier(),
            "XGBClassifier": XGBClassifier(verbosity=0, use_label_encoder=False),
            "LGBMClassifier": LGBMClassifier()
        }

    def get_models_dict(self):
        return self.model_dict