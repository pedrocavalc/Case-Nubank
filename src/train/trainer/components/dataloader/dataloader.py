import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer, StandardScaler

class DataLoader:
    def __init__(self, path, target) -> None:
        self.path = path
        self.target = target

    def run(self, favorite_ids: list):
        try:
            data = self.load_data()
            data = self.clean_data(data)
            data = self.create_labels(data, favorite_ids)
            features = self.transform_features(data)

            self.split_data(features, data[self.target])
            print(f"The data has been loaded: {features.shape}")
        except Exception as e:
            print(f"Error while loading data: {e}")

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.path)

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df["genres"] = df["genres"].fillna("").apply(lambda x: x.split(", "))
        df["platform"] = df["platform"].fillna("None")
        return df

    def create_labels(self, df: pd.DataFrame, favorite_ids: list) -> pd.DataFrame:
        df["label"] = df["imdbId"].apply(lambda x: 1 if x in favorite_ids else 0)
        return df

    def transform_features(self, df: pd.DataFrame) -> pd.DataFrame:
        mlb = MultiLabelBinarizer()
        genres_encoded = mlb.fit_transform(df["genres"])
        genres_df = pd.DataFrame(genres_encoded, columns=mlb.classes_)

        scaler = StandardScaler()
        numerical_data = df[["releaseYear", "imdbAverageRating", "imdbNumVotes"]].fillna(0)
        numerical_scaled = scaler.fit_transform(numerical_data)
        numerical_df = pd.DataFrame(numerical_scaled, columns=["year_scaled", "rating_scaled", "votes_scaled"])

        features_df = pd.concat([genres_df, numerical_df], axis=1)

        if '' in features_df.columns:
            features_df = features_df.drop(columns=[''])

        features_df.columns = [
            col.strip().replace(" ", "_").replace("&", "and").replace("-", "_") for col in features_df.columns
        ]

        return features_df

    def split_data(self, X: pd.DataFrame, y: pd.Series) -> None:
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

    def get_train_data(self):
        return self.X_train, self.y_train

    def get_test_data(self):
        return self.X_test, self.y_test
