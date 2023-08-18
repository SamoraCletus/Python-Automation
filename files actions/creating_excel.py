import pandas as pd

df = pd.read_excel("supermarket_sales.xlsx")

df = df[["Gender", "Product line", "Total"]]

pivot_table = df.pivot_table(
    index="Gender", columns="Product line", values="Total", aggfunc="sum")

pivot_table.to_excel('pivot_table.xlsx', 'Report', startrow=4)
