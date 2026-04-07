import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "notebook"
df = pd.DataFrame({
"Height":[150,160,170,180,165],
"Weight":[50,60,70,80,65],
"Gender":["M","F","M","F","M"]
})
fig = px.scatter(df, x="Height", y="Weight",
color="Gender",
title="Height vs Weight by Gender")
fig.show()