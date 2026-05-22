from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/top-products")
def get_top_products():
    df = pd.read_csv("output/top5_highprice.csv")
    return df.to_dict(orient="records")