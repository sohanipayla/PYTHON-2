import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "notebook"
df = pd.DataFrame({
"Department":["IT","HR","Finance","Marketing"],
"Budget":[50000,30000,40000,20000]
})
max_index = df["Budget"].idxmax()
pull = [0.1 if i == max_index else 0 for i in range(len(df))]
fig = px.pie(df,
names="Department",
values="Budget",
title="Department Budget Allocation",
color_discrete_sequence=["#636EFA","#EF553B","#00CC96","#AB63FA"])
fig.update_traces(pull=pull,
textinfo="label+percent",
textposition="inside")
fig.show()