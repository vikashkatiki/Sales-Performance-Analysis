import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Project1(Sales Performance Analysis)/sales_visual.csv")

print(df.isnull().sum())
print(df.duplicated().sum())

print(df["Sales"].describe())

plt.figure(figsize=(8,5))
plt.plot(df["Month"],df["Sales"],marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.show()

plt.figure(figsize=(8,5))
plt.bar(df["Month"],df["Sales"],alpha=0.2)
plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
