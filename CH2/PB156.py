import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "notebook"
df = pd.DataFrame({
"Department": ["IT", "HR", "Finance", "Marketing"],
"Revenue": [120000, 80000, 150000, 95000]
})
fig = px.bar(df, x="Department", y="Revenue",
title="Department-wise Revenue",
color="Department")
fig.show()