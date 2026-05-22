import pandas as pd

df = pd.read_csv("data/generated_products.csv") #create dataframe by reading csv with pandas
df = df.dropna() #remove any empty values

#get total value of each product in system and assign it to a variable
product_values_df = df["total_product_value"] = df["price"] * df["quantity"]
print(product_values_df.head(10))

#calculate the total value of all products in system
total_inv_value = df["total_product_value"].sum()
print("Total inventory value:", total_inv_value)

highest_price_df = df.sort_values("price", ascending=False) #sort by highest prices
#create clean csv of 5 highest priced products
highest_price_df.head(5).to_csv("output/top5_highprice.csv", index=False)
print(highest_price_df.head(5)) #print the 5 highest priced products

#get average product price
average_price_df = df["price"].mean()
print(round(average_price_df, 2))