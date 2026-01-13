import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Project1(Sales Performance Analysis)/sales_visual.csv")
print(df)
print("Dataset Preview:")
print(df.head())

print("Dataset Info:")
print(df.info())

print(df["Sales"].describe())

print("Month with highest Sales:")
print(df.loc[df["Sales"].idxmax()])

print("Month with lowest Sales:")
print(df.loc[df["Sales"].idxmin()])

df.to_csv("Cleaned_sales_data.csv",index=False)