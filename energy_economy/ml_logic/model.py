import pandas as pd
import numpy as np
from colorama import Fore, Style

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline

import warnings
warnings.filterwarnings("ignore")


def initialize_model():
    """
    Initialize the Ridge model
    """
    poly_model = PolynomialFeatures(degree=3)
    ridge_reg = Ridge(alpha=0.1)

    # Create a pipeline to combine the polynomial features and the Ridge model
    pipeline = make_pipeline(poly_model, ridge_reg)

    print("✅ Model initialized")

    return pipeline


def train_model(model,
                X: np.ndarray,
                y: np.ndarray):
    """
    Fit the model and return the fitted_model
    """

    print(Fore.BLUE + "\nTraining model..." + Style.RESET_ALL)
    # Fit the pipeline to the training data
    model.fit(X, y)

    print(f"✅ Model trained on {len(X)} rows")

    return model

def evaluate_model(model,
                   X: np.ndarray,
                   y: np.ndarray):
    """
    Evaluate trained model performance on the dataset
    """

    print(Fore.BLUE + f"\nEvaluating model on {len(X)} rows..." + Style.RESET_ALL)

    if model is None:
        print(f"\n❌ No model to evaluate")
        return None

    score = model.score(x=X, y=y)

    return score
