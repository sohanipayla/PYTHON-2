import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "notebook"
df = pd.DataFrame({
"Region": ["North","North","South","South"],
"Year": ["2023","2024","2023","2024"],
"Sales": [200,250,180,220]
})
fig = px.bar(df, x="Region", y="Sales",
color="Year", barmode="group",
title="Yearly Sales Comparison Across Regions")
fig.show()