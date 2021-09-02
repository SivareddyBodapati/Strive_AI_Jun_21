import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn import pipeline      # Pipeline
from sklearn import preprocessing # OrdinalEncoder, LabelEncoder
from sklearn import impute
from sklearn import compose
from sklearn import model_selection # train_test_split
from sklearn import metrics         # accuracy_score, balanced_accuracy_score, plot_confusion_matrix
from sklearn import set_config

set_config(display='diagram') # Useful for display the pipeline
DATA_PATH = "C:/Users/User/Documents/Strive_AI_Jun_21/M4-Feature Engineering/04.Challenge_1/"
df =pd.read_csv(DATA_PATH+"heart.csv")
print(df.head())
print(df.info())

# also can be done in the pipeline
# from sklearn.preprocessing import StandardScaler
# SS = StandardScaler()
# columns_toscale =['age','trtbps','thalachh','oldpeak','chol']
# df[columns_toscale]=SS.fit_transform(df[columns_toscale])
# df.head()

X,y = df.drop(['output'],axis=1),df.output

cat_vars=X.select_dtypes(include=[object]).columns.values.tolist()
num_vars =X.select_dtypes(exclude=[object]).columns.values.tolist()

num_preprocessing =pipeline.Pipeline([("imputer",impute.SimpleImputer(strategy="mean"))]) #,("scaler",preprocessing.StandardScaler())

cat_preporcessing =pipeline.Pipeline([("imputer",impute.SimpleImputer(strategy='constant', fill_value='missing')),
                                      ("ordinal",preprocessing.OrdinalEncoder(handle_unknown="use_encoded_value",unknown_value = -1))])
tree_prepro = compose.ColumnTransformer(transformers=[('num_data',num_preprocessing,num_vars),('cat_data',cat_preporcessing,cat_vars),],remainder='drop')

from sklearn.tree          import DecisionTreeClassifier
from sklearn.ensemble      import RandomForestClassifier
from sklearn.ensemble      import ExtraTreesClassifier
from sklearn.ensemble      import AdaBoostClassifier
from sklearn.ensemble      import GradientBoostingClassifier
from sklearn.experimental  import enable_hist_gradient_boosting # Necesary for HistGradientBoostingClassifier
from sklearn.ensemble      import HistGradientBoostingClassifier
from xgboost               import XGBClassifier
from lightgbm              import LGBMClassifier
from catboost              import CatBoostClassifier
from sklearn.svm           import SVC
from sklearn.linear_model  import LogisticRegression
from sklearn.neighbors     import KNeighborsClassifier

from sklearn.tree          import DecisionTreeRegressor
from sklearn.ensemble      import RandomForestRegressor
from sklearn.ensemble      import ExtraTreesRegressor
from sklearn.ensemble      import AdaBoostRegressor
from sklearn.ensemble      import GradientBoostingRegressor
from xgboost               import XGBRegressor
from lightgbm              import LGBMRegressor
from catboost              import CatBoostRegressor

#checking the classifiers
classifiers = {
  "Decision Tree": DecisionTreeClassifier(),
  "Extra Trees":  ExtraTreesClassifier(),
  "Random Forest": RandomForestClassifier(),
  "AdaBoost":AdaBoostClassifier(),
  "Skl GBM":GradientBoostingClassifier(),
  "Skl HistGBM":HistGradientBoostingClassifier(),
  "XGBoost": XGBClassifier(),
  "LightGBM":LGBMClassifier(),
  "CatBoost":CatBoostClassifier(),
  "SVM": SVC(),
  "lr":LogisticRegression(),
  "KNN":KNeighborsClassifier(n_neighbors=3)
}


for tree, method in classifiers.items():
    classifiers[tree]=pipeline.Pipeline([("preprocessing", tree_prepro),(tree,method)])

print(classifiers['SVM'])

# checking the regressors
Regressors = {
  "Decision Tree": DecisionTreeRegressor(),
  "Extra Trees":   ExtraTreesRegressor(n_estimators=100),
  "Random Forest": RandomForestRegressor(n_estimators=100),
  "AdaBoost":      AdaBoostRegressor(n_estimators=100),
  "Skl GBM":       GradientBoostingRegressor(n_estimators=100),
  "XGBoost":       XGBRegressor(n_estimators=100),
  "LightGBM":      LGBMRegressor(n_estimators=100),
  "CatBoost":      CatBoostRegressor(n_estimators=100),
}

from sklearn import set_config
set_config(display='diagram')

for tree, method in Regressors.items():
    Regressors[tree]=pipeline.Pipeline([("preprocessing", tree_prepro),(tree,method)])

import time
X_train,X_test,y_train,y_test =model_selection.train_test_split(X,y,test_size=0.2,stratify = y,random_state=0)

results = pd.DataFrame({'Model': [], 'Accuracy': [], 'Bal Acc.': [], 'Time': []})


for model_name, model in classifiers.items():
    start_time = time.time()
    
    # FOR EVERY PIPELINE (PREPRO + MODEL) -> TRAIN WITH TRAIN DATA (x_train)
    model.fit(X_train,y_train)
    # GET PREDICTIONS USING x_val
    pred = model.predict(X_test)

    total_time = time.time() - start_time
    
    results = results.append({"Model":    model_name,
                              "Accuracy": metrics.accuracy_score(y_test, pred)*100,
                              "Bal Acc.": metrics.balanced_accuracy_score(y_test, pred)*100,
                              "Time":     total_time},
                              ignore_index=True)

results_ord = results.sort_values(by=['Accuracy'], ascending=False, ignore_index=True)
results_ord.index += 1 
results_ord.style.bar(subset=['Accuracy', 'Bal Acc.'], vmin=0, vmax=100, color='#5fba7d')
print(results_ord)

#univariate selection # selecting the best features
#feature engineering

#apply selectKBest.class to extact top five best features
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
best_ft = SelectKBest(score_func = chi2, k=8)
model =best_ft.fit(X,y)
df_scores=pd.DataFrame(model.scores_)
df_columns =pd.DataFrame(X.columns)
feature_scores = pd.concat([df_columns,df_scores],axis=1)
feature_scores.columns=['features','scores']
print(feature_scores) #highest the score 

best_features = feature_scores.nlargest(4,'scores')['features'].tolist()
print('the Best features for this data:',best_features )

# Data enhancement based on gender with best features
def enhancement(data):
    gen_data =data
    for sex in data['sex'].unique():
        gender_data = gen_data[gen_data['sex']==sex]
        
        thalachh_std = gender_data['thalachh'].std()/10
        oldpeak_std = gender_data['oldpeak'].std()/10
        caa_std = gender_data['caa'].std()/10
        cp_std =gender_data['cp'].std()/10
        
        for i in gen_data[gen_data['sex']==sex].index:
            if np.random.randint(2) == 1:
                gen_data['thalachh'].values[i] += thalachh_std
            else:
                gen_data['thalachh'].values[i] -= thalachh_std
            
            if np.random.randint(2) == 1:
                gen_data['oldpeak'].values[i] += oldpeak_std
            else:
                gen_data['oldpeak'].values[i] -= oldpeak_std
            
            if np.random.randint(2) == 1:
                gen_data['caa'].values[i] += caa_std
            else:
                gen_data['caa'].values[i] -= caa_std
            
            if np.random.randint(2) == 1:
                gen_data['cp'].values[i] += cp_std
            else:
                gen_data['cp'].values[i] -= cp_std
                
    return gen_data
gen = enhancement(df)
#random subset of the sample 
gen =gen.sample(gen.shape[0]//4)
gen = pd.concat((df,gen),axis=0)
X,y = gen.drop(['output'],axis=1),gen.output

import time
X_train,X_test,y_train,y_test =model_selection.train_test_split(X,y,test_size=0.2,stratify = y,random_state=0)

results = pd.DataFrame({'Model': [], 'Accuracy': [], 'Bal Acc.': [], 'Time': []})


for model_name, model in classifiers.items():
    start_time = time.time()
    
    # FOR EVERY PIPELINE (PREPRO + MODEL) -> TRAIN WITH TRAIN DATA (x_train)
    model.fit(X_train,y_train)
    # GET PREDICTIONS USING x_val
    pred = model.predict(X_test)# CODE HERE

    total_time = time.time() - start_time
    
    results = results.append({"Model":    model_name,
                              "Accuracy": metrics.accuracy_score(y_test, pred)*100,
                              "Bal Acc.": metrics.balanced_accuracy_score(y_test, pred)*100,
                              "Time":     total_time},
                              ignore_index=True)
                              
                              


### BEGIN SOLUTION

results_ord = results.sort_values(by=['Accuracy'], ascending=False, ignore_index=True)
results_ord.index += 1 
results_ord.style.bar(subset=['Accuracy', 'Bal Acc.'], vmin=0, vmax=100, color='#5fba7d')
print(results_ord)

#adding a new column
gen['new_col']=gen[best_features].mean(axis=1)

X,y = gen.drop(['output'],axis=1),gen.output
import time
X_train,X_test,y_train,y_test =model_selection.train_test_split(X,y,test_size=0.2,stratify = y,random_state=0)

results = pd.DataFrame({'Model': [], 'Accuracy': [], 'Bal Acc.': [], 'Time': []})


for model_name, model in classifiers.items():
    start_time = time.time()
    
    # FOR EVERY PIPELINE (PREPRO + MODEL) -> TRAIN WITH TRAIN DATA (x_train)
    model.fit(X_train,y_train)
    # GET PREDICTIONS USING x_val
    pred = model.predict(X_test)# CODE HERE

    total_time = time.time() - start_time
    
    results = results.append({"Model":    model_name,
                              "Accuracy": metrics.accuracy_score(y_test, pred)*100,
                              "Bal Acc.": metrics.balanced_accuracy_score(y_test, pred)*100,
                              "Time":     total_time},
                              ignore_index=True)
                              
                              


### BEGIN SOLUTION

results_ord = results.sort_values(by=['Accuracy'], ascending=False, ignore_index=True)
results_ord.index += 1 
results_ord.style.bar(subset=['Accuracy', 'Bal Acc.'], vmin=0, vmax=100, color='#5fba7d')
print(results_ord)
print('Highest of all accuracy:',results_ord['Accuracy'].iloc[0],',Method is:',results_ord['Model'].iloc[0])
