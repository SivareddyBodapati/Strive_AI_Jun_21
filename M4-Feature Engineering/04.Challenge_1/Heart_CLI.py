import Heart_challenge as HC
import pandas as pd
# Accuracy = HC.results_ord['Accuracy'].iloc[0]

age = int(input('How old are you? (integer) \n'))
gender = int(input('Please input 0 if male and 1 if female \n'))
cp = int(input('What is the Chest Pain type \n Please input the CP \n enter integer between 0-1000 \n '))
trtbps = int(input('What is the resting blood pressure (in mm Hg) \n Please input the trtbps \n enter integer between 0-1000 \n '))
chol = int(input('Please input the chol \n enter integer between 0-1000 \n'))
fbs= int(input('if > 120mg/dl \n input 1 else 0 \n '))
restecg = int(input('What are the resting electrocardiographic results? \n Please input as follow : \n 0: normal \n 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) \n 2: showing probable or definite left ventricular hypertrophy by Estes criteria \n'))
thalachh = int(input('What is the  maximum heart rate achieved  \n Please input the thalach \n enter integer between 0-1000 \n'))
exng= int(input('Did the patient had exercise induced angina \n Please input 1 for Yes and 0 for No \n'))
oldpeak = int(input('Please inpu the value of the old peak \n enter integer between 0-1000 \n'))
slp =int(input('Please input the value of SLP \n enter integer between 0-1000 \n'))
caa = int(input('What is the number of major vessels ? \n Please input the CA number between 0-3 \n'))
thall = int(input('Please input the value of the thall  \n enter integer between 0-1000 \n'))
answers =  [age,gender,cp, trtbps,chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]

data = pd.DataFrame(data = answers).T

data.columns = ['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh','exng', 'oldpeak', 'slp', 'caa', 'thall']

prediction = HC.predictions(data)

if prediction == 0:
        print("You are healthy up to date ")
else:
        print("You are suggested to use Hippocratia drug as you have a high risk of heart attack")