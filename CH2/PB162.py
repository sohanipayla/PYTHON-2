import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "notebook"
df = pd.DataFrame({
"Year":[2020,2021,2022,2023,2024],
"Revenue":[100,150,200,250,300]
})
fig = px.line(df, x="Year", y="Revenue",title="Yearly Company Growth",markers=True)
fig.show()