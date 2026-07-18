import random
import pandas as pd
from pathlib import Path

CATEGORIES = [
    "Wedding Dress",
    "Bridesmaid Dress",
    "Prom Gown",
    "Cocktail Dress",
    "Evening Gown",
    "Formal Dress"
]

FABRICS = [
    "Chiffon",
    "Satin",
    "Lace",
    "Velvet",
    "Jersey",
    "Tulle",
    "Organza",
    "Silk",
    "Crepe",
    "Sequin"
]

NECKLINES = [
    "V Neck",
    "Sweetheart",
    "Square",
    "Halter",
    "Off Shoulder",
    "One Shoulder",
    "Illusion",
    "Boat Neck",
    "Scoop Neck"
]

SLEEVES = [
    "Sleeveless",
    "Cap Sleeve",
    "Long Sleeve",
    "Short Sleeve",
    "Puff Sleeve",
    "Strapless"
]

LENGTHS = [
    "Mini",
    "Knee Length",
    "Tea Length",
    "Midi",
    "Floor Length"
]

SILHOUETTES = [
    "A-Line",
    "Mermaid",
    "Ball Gown",
    "Sheath",
    "Empire",
    "Fit and Flare"
]

EMBELLISHMENTS = [
    "Pleated",
    "Embroidery",
    "Beaded",
    "Sequins",
    "Ruched",
    "Feather Trim",
    "Ruffles",
    "Lace Applique"
]

COLORS = [
    "Black",
    "White",
    "Red",
    "Pink",
    "Emerald",
    "Royal Blue",
    "Dusty Blue",
    "Sage",
    "Champagne",
    "Navy"
]

# print("Attributes Loaded Successfully")



def generate_product():
    category = random.choice(CATEGORIES)
    fabric = random.choice(FABRICS)
    neckline = random.choice(NECKLINES)
    sleeve = random.choice(SLEEVES)
    length = random.choice(LENGTHS)
    silhouette = random.choice(SILHOUETTES)
    embellishment = random.choice(EMBELLISHMENTS)

    color = random.choice(COLORS)

    templates = [
        f"{length} {fabric.lower()} {category.lower()} with {embellishment.lower()} bodice and {neckline.lower()} available in {color.lower()}.",

        f"Elegant {fabric.lower()} {category.lower()} featuring {neckline.lower()}, {sleeve.lower()} and {embellishment.lower()} details in {color.lower()}.",

        f"Beautiful {silhouette.lower()} {category.lower()} made from {fabric.lower()} with {neckline.lower()} and {sleeve.lower()} in {color.lower()}.",

        f"Designer {fabric.lower()} {category.lower()} featuring {embellishment.lower()} work, {neckline.lower()} and {sleeve.lower()} available in {color.lower()}.",

        f"Premium {length.lower()} {fabric.lower()} {category.lower()} with {silhouette.lower()} silhouette, {neckline.lower()} and {color.lower()} color."
    ]

    description = random.choice(templates)

    return {
        "description": description,
        "category": category,
        "fabric": fabric,
        "neckline": neckline,
        "sleeve": sleeve,
        "length": length,
        "silhouette": silhouette,
        "embellishment": embellishment,
        "color": color
    }