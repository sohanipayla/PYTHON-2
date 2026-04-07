import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "notebook"
df = pd.DataFrame({
"City":["City A","City B","City C","City D"],
"Population":[400,300,200,100]
})
pull = [0, 0.1, 0, 0]
fig = px.pie(df,
names="City",
values="Population",
title="Population Share by City",
color_discrete_sequence=["#636EFA","#EF553B","#00CC96","#AB63FA"])
fig.update_traces(pull=pull,
textinfo="label+percent")
fig.show()