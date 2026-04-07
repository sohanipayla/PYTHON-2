import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "notebook"
df = pd.DataFrame({
    "Product": ["A", "B", "C", "D", "E"],
    "Sales": [30, 25, 20, 15, 10]
})
fig = px.pie(
    df,
    names="Product",
    values="Sales",
    title="Product Market Share",
    color_discrete_sequence=["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A"]
)
fig.update_traces(textinfo='percent+label')
fig.show()