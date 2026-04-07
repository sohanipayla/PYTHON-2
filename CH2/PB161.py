import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "notebook"
df = pd.DataFrame({
"X":[1,2,3,4],
"Y":[10,20,30,40],
"Z":[5,15,25,35],
"Category":["A","B","A","B"]
})
fig = px.scatter_3d(df,x="X", y="Y", z="Z",color="Category",title="3D Scatter Plot with Category Grouping")
fig.show()