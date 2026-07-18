import pandas as pd
import spacy
from spacy.tokens import DocBin

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/products.csv")

nlp = spacy.blank("en")
db = DocBin()

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

count = 0

for _, row in df.iterrows():

    text = str(row["description"])

    doc = nlp.make_doc(text)

    ents = []

    for column, label in ATTRIBUTE_MAP.items():

        value = str(row[column])

        start = text.lower().find(value.lower())

        if start == -1:
            continue

        end = start + len(value)

        span = doc.char_span(
            start,
            end,
            label=label,
            alignment_mode="expand"
        )

        if span:
            ents.append(span)

    doc.ents = ents

    db.add(doc)

    count += 1

db.to_disk("data/train.spacy")

print("="*50)
print("Training Data Created")
print("Total Examples :", count)
print("Saved :", "data/train.spacy")
print("="*50)