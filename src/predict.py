import spacy

# Load trained model
nlp = spacy.load("trained_model/model-best")

text = input("Enter Product Description:\n")

doc = nlp(text)

result = {}

for ent in doc.ents:
    result[ent.label_] = ent.text

print("\nExtracted Attributes:")
print(result)