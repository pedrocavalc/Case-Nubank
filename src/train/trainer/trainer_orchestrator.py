from trainer.components.dataloader.dataloader import DataLoader
from trainer.components.models.models_manager.models_manager import ModelsManager
from trainer.components.models.pipeline.custom_pipeline import CustomPipeline
from trainer.components.models.models_configuration.models_configuration import ModelsConfiguration
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

import warnings
warnings.filterwarnings("ignore")

import mlflow
mlflow.set_tracking_uri("http://localhost:5000")

class TrainerOrchestrator():
    def __init__(self, data_path, target, columns, ids):
        self.data_path = data_path
        self.target = target
        self.columns= columns
        self.ids = ids
        
    def run(self):
        data_loader = self.get_data_loader()
        models_to_train = self.get_models()
        self.train(data_loader,models_to_train)

    
    def get_data_loader(self):
        data_loader = DataLoader(self.data_path, self.target)
        data_loader.run(favorite_ids=self.ids)
        return data_loader
    
    def get_models(self):
        models_to_train = ModelsManager().get_models_dict()
        return models_to_train

    def train(self, data_loader,models_to_train):
        mlflow.start_run()
        mlflow.sklearn.autolog()
        for model_name, model in models_to_train.items():
            grid_search = GridSearchCV(model, ModelsConfiguration().get_parameters(model_name), cv=5, n_jobs=-1, verbose=2,refit=True)
            model = CustomPipeline().build_model(grid_search)
            model.fit(data_loader.get_train_data()[0], data_loader.get_train_data()[1])
            self.get_metrics(model, data_loader)

    def get_metrics(self, model, data_loader):
        y_hat = model.predict(data_loader.get_test_data()[0])
        y_true = data_loader.get_test_data()[1]
        
        accuracy = accuracy_score(y_true, y_hat)
        precision = precision_score(y_true, y_hat, average='weighted', zero_division=0)
        recall = recall_score(y_true, y_hat, average='weighted', zero_division=0)
        f1 = f1_score(y_true, y_hat, average='weighted', zero_division=0)

        mlflow.log_metric('accuracy', accuracy)
        mlflow.log_metric('precision', precision)
        mlflow.log_metric('recall', recall)
        mlflow.log_metric('f1_score', f1)