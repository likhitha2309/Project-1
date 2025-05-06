import pandas as pd
dataset= pd.read_csv('walmart.csv')

print(dataset.describe)

print("Dataset Loaded")

columns = ["Weekly_Sales","Holiday_Flag","Temperature","Fuel_Price","CPI","Unemployment"]

for column in columns:
    print(f"Mean: {dataset[column].mean()}")
    print(f"Median: {dataset[column].median()}")
    print(f"Mode: {dataset[column].mode()}")
