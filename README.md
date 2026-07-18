# Product-Attribute-Extraction
AI/NLP Product Attribute Extraction using spaCy and FastAPI

# Product Attribute Extraction using spaCy & FastAPI

## Overview

This project extracts structured product attributes from unstructured fashion product descriptions using a trained spaCy Named Entity Recognition (NER) model and exposes the functionality through a FastAPI REST API.

## Features

- Extracts product attributes from text
- Trained spaCy NER model
- FastAPI REST API
- Swagger UI for testing
- Evaluation with Accuracy and F1 Score

## Extracted Attributes

- Category
- Fabric
- Neckline
- Sleeve
- Length
- Silhouette
- Embellishment
- Color

## Project Structure

```
Product-Attribute-Extraction/
│
├── api/
├── data/
├── evaluation/
├── src/
├── trained_model/
├── config.cfg
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Training

```bash
python src/train.py

python -m spacy train config.cfg --output trained_model --paths.train data/train.spacy --paths.dev data/train.spacy
```

## Run API

```bash
uvicorn api.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

## Sample Input

```
Floor length chiffon bridesmaid dress with pleated bodice and V neckline available in sage and dusty blue
```

## Sample Output

```json
{
  "CATEGORY": "Bridesmaid Dress",
  "FABRIC": "Chiffon",
  "NECKLINE": "V Neckline",
  "SLEEVE": null,
  "LENGTH": "Floor Length",
  "SILHOUETTE": null,
  "EMBELLISHMENT": "Pleated",
  "COLOR": "Dusty Blue"
}
```

## Evaluation

- Attribute Accuracy
- Overall F1 Score

## Common Failure Cases

- Unseen colors
- New fabrics not present in training data
- Multiple colors in one description
- Ambiguous wording
- Typographical errors

## Tech Stack

- Python
- spaCy
- FastAPI
- Pandas
- scikit-learn
- Pydantic
