from fastapi import FastAPI
from pydantic import BaseModel
import spacy

# Load trained model
nlp = spacy.load("trained_model/model-best")

app = FastAPI(
    title="Product Attribute Extraction API",
    version="1.0"
)

class ProductRequest(BaseModel):
    description: str

@app.get("/")
def home():
    return {
        "message": "Product Attribute Extraction API is Running"
    }

@app.post("/extract")
def extract(product: ProductRequest):

    doc = nlp(product.description)

    attributes = {
        "CATEGORY": None,
        "FABRIC": None,
        "NECKLINE": None,
        "SLEEVE": None,
        "LENGTH": None,
        "SILHOUETTE": None,
        "EMBELLISHMENT": None,
        "COLOR": None
    }

    for ent in doc.ents:
        attributes[ent.label_] = ent.text

    return {
        "input": product.description,
        "attributes": attributes
    }