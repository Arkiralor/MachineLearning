from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
import joblib

from .data_resolvers import DataResolver

class Model:

    def __init__(self, df=None):
        self.df = df
        self.df['Platform'] = df['Platform'].apply(DataResolver.resolve_platform)
        self.df['Genre'] = df['Genre'].apply(DataResolver.resolve_genre)
        self.df['Publisher'] = df['Publisher'].apply(DataResolver.resolve_publisher)

    def make_sets(self):
        x = self.df.drop(columns=["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales", "Market_Performance"])
        y = self.df["Market_Performance"]
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=0.3)

    def train_model(self):
        self.model = DecisionTreeClassifier()
        self.model.fit(self.x_train, self.y_train)

    def predict(self, x = None):            
        return self.model.predict(x)

    def score(self, x=None, y=None):
        return accuracy_score(self.y_test, self.predict(x))

    def export_model(self, filename):
        joblib.dump(self.model, filename)

    @staticmethod
    def load_model(filename):
        return joblib.load(filename)

