import pandas as pd


dataset = pd.read_csv('Walmart.csv')

print(dataset.describe)

columns = ["Weekly_Sales","Holiday_Flag","Temperature","Fuel_Price","CPI","Unemployment"]

for column in columns:
    print(f"Mean: {dataset[column].mean()}")
    print(f"Mdian: {dataset[column].median()}")
    print(f"Mode: {dataset[column].mode()}")