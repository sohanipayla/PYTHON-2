import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "notebook"
df = pd.DataFrame({
"Department": ["IT","HR","Finance","Marketing"],
"Profit_Loss": [50000,-20000,70000,-15000]
})
fig = px.bar(df, x="Department", y="Profit_Loss",
color="Profit_Loss",
color_continuous_scale=["red","green"],
title="Profit and Loss by Department")
fig.show()