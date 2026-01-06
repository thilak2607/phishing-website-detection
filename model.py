import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

print("START")

data = pd.read_csv("phishing.csv")

X = []
y = []

for i in range(len(data)):
    url = data["url"][i]
    label = data["label"][i]
    X.append([len(url)])
    y.append(label)

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("MODEL SAVED")
