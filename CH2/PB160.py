import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "notebook"
df = pd.DataFrame({
"Sales":[100,200,300,400],
"Profit":[20,50,70,90],
"Quantity":[10,30,50,80]
})
fig = px.scatter(df, x="Sales", y="Profit",
size="Quantity",
title="Sales vs Profit (Bubble Size = Quantity)")
fig.show()