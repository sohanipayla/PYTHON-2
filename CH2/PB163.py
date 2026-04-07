import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "notebook"
df = pd.DataFrame({
"Month":["Jan","Feb","Mar","Jan","Feb","Mar"],
"Sales":[50,60,70,40,55,65],
"Product":["A","A","A","B","B","B"]
})
fig = px.line(df, x="Month", y="Sales",color="Product",markers=True,title="Product-wise Sales Trend")
fig.show()