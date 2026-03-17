import pandas as pd
df = pd.DataFrame({
 "Marks":["50","60","Absent","70","Absent"]
})
# Replace "Absent" with 0
df["Marks"] = df["Marks"].replace("Absent", 0)
# Convert to integer
df["Marks"] = df["Marks"].astype(int)
# Mean marks
print("Mean Marks:", df["Marks"].mean())
# Number of students scoring above 50
print("Students scoring above 50:", (df["Marks"] > 50).sum())