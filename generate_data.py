import pandas as pd

#Create table of products to later convert to dataframe and export to csv
product_data = {
    "id": [1, 2, 3, 4, 5, 6, 7],
    "name": ["Phone", "Lamp", "Desk", "T-Shirt", "Monitor", "Basket", "Candle"],
    "price": [1000, 100, 225, 35, 180, 20, 5],
    "quantity": [12, 15, 4, 72, 14, 51, 621],
    "category": ["Electronics", "Home", "Home", "Clothing", "Electronics", "Home", "Home"]
}

df = pd.DataFrame(product_data)

#Export to csv file in data folder
df.to_csv("data/generated_products.csv", index=False)