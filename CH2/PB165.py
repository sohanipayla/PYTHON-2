import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "notebook"
df = pd.DataFrame({
"Student": [f"S{i}" for i in range(1, 21)],
"Marks": [45, 50, 55, 60, 65, 70, 75, 80, 85, 90,
48, 52, 58, 62, 68, 72, 78, 82, 88, 92],
"Grade": ["C","C","C","B","B","B","A","A","A","A",
"C","C","C","B","B","B","A","A","A","A"]
})
fig = px.histogram(df,x="Marks",color="Grade",nbins=5,text_auto=True,title="Student Marks Distribution by Grade")
fig.show()