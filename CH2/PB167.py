import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "notebook"
df = pd.DataFrame({
"Sales":[100,120,150,180,200,220,250,270,300,320,
110,130,160,190,210,230,260,280,310,330,
105,125,155,185,205,225,255,275,305,325],
"Region":["North"]*15 + ["South"]*15
})
fig = px.histogram(df,x="Sales",color="Region",pattern_shape="Region",nbins=6,color_discrete_sequence=["#1f77b4", "#ff7f0e"],title="Monthly Sales Distribution by Region")
fig.show()