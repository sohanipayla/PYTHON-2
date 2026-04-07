import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "notebook"
df = pd.DataFrame({
"Age":[22,25,28,30,35,40,45,50,29,33,
26,31,38,42,48],
"Department":["IT","IT","HR","HR","Finance","Finance",
"IT","HR","Finance","IT",
"HR","Finance","IT","HR","Finance"]
})
fig = px.histogram(df,x="Age",color="Department",histfunc="count",nbins=5,title="Employee Age Distribution by Department",width=700,height=400)
fig.show()