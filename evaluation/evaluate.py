import spacy
import pandas as pd
from sklearn.metrics import f1_score

nlp = spacy.load("trained_model/model-best")

df = pd.read_csv("data/products.csv")

correct = 0
total = 0

y_true = []
y_pred = []

ATTRIBUTE_MAP = {
    "category": "CATEGORY",
    "fabric": "FABRIC",
    "neckline": "NECKLINE",
    "sleeve": "SLEEVE",
    "length": "LENGTH",
    "silhouette": "SILHOUETTE",
    "embellishment": "EMBELLISHMENT",
    "color": "COLOR"
}

for _, row in df.iterrows():

    doc = nlp(row["description"])

    predicted = {}

    for ent in doc.ents:
        predicted[ent.label_] = ent.text.lower()

    for col, label in ATTRIBUTE_MAP.items():

        actual = str(row[col]).lower()

        pred = predicted.get(label, "")

        y_true.append(actual)
        y_pred.append(pred)

        if actual == pred:
            correct += 1

        total += 1

accuracy = correct / total

print("=" * 50)
print("Evaluation")
print("=" * 50)
print("Attribute Accuracy :", round(accuracy, 4))

try:
    print("Overall F1 Score :", round(f1_score(y_true, y_pred, average="weighted"), 4))
except:
    print("Overall F1 Score : Unable to calculate")