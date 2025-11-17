import pandas as pd
import pyarrow.parquet as pq

df = pd.read_csv("./Dataset/ORDERS.csv")
print(df.head())

parqt = df.to_parquet("./Dataset/orders.parquet", engine="pyarrow", index=False)
# dfprq = pd.read_parquet(parqt)
df1 = pd.read_parquet("./Dataset/orders.parquet")
print(df1.head())