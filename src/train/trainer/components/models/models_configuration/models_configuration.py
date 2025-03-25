class ModelsConfiguration():
    def __init__(self) -> None:
        self.parameters = {
            'XGBClassifier': {
                'n_estimators': [100],
                'max_depth': [6],
                'learning_rate': [0.1]
            },
            'RandomForestClassifier': {
                'n_estimators': [100],
                'max_depth': [None, 10]
            },
            'LGBMClassifier': {
                'n_estimators': [100],
                'max_depth': [10],
                'learning_rate': [0.1]
            }
        }

    def get_parameters(self, model_name):
        return self.parameters.get(model_name, {})
