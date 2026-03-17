import pandas as pd   
df = pd.DataFrame({
 "Student":["A","B","C","D"],
 "Math":[70,45,90,60],
 "Science":[75,40,85,55]
})
# Create Average column using apply (row-wise)
df["Average"] = df.apply(lambda x: (x["Math"] + x["Science"]) / 2, axis=1)
# Function to assign Grade
def grade(avg):
    if avg >= 80:
        return "Distinction"
    elif avg >= 60:
        return "First"
    else:
        return "Second"
# Create Grade column
df["Grade"] = df["Average"].apply(grade)
print(df)