                # Avisos python
import warnings

             # Manipulação de dados
import numpy as np
import pandas as pd
import math

            # Visualização de dados
import shap
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

              # Modelos utilizados
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, ExtraTreesClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

         # Preprocessamento dos dados
from sklearn.preprocessing import StandardScaler, MinMaxScaler    
from sklearn.model_selection import train_test_split, RandomizedSearchCV

            # Seleção de features
from sklearn.feature_selection import RFECV, RFE
from sklearn.pipeline import Pipeline

            #Tratamento de outliers
from sklearn.impute import KNNImputer

            # Avaliação de modelo
from sklearn.metrics import classification_report, confusion_matrix, roc_curve
from sklearn import metrics