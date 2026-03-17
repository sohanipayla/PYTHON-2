import pandas as pd
df = pd.DataFrame({
 "Product":["P1","P2","P3","P4","P5"],
 "Price":[100,200,150,300,250],
 "Quantity":[5,2,4,1,3]
})
# Create TotalAmount using apply (row-wise)
df["TotalAmount"] = df.apply(lambda x: x["Price"] * x["Quantity"], axis=1)
# Sort by TotalAmount in descending order
df = df.sort_values(by="TotalAmount", ascending=False)
print(df)