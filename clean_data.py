import pandas as pd

# Load the data
df = pd.read_csv("car_prices.csv")

# Print original columns to verify
print("🧾 Original columns:", df.columns.tolist())

# Clean column names: remove spaces, lowercase, replace spaces with underscores
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
print("✅ Cleaned columns:", df.columns.tolist())

# Convert 'saledate' to datetime with timezone handling
df['saledate'] = pd.to_datetime(df['saledate'], errors='coerce', utc=True)

# Check the result
print(df.head())
# Specify the exact format for the 'saledate' column
df['saledate'] = pd.to_datetime(df['saledate'], format='%Y-%m-%d %H:%M:%S%z', errors='coerce', utc=True)
print(df['saledate'].head())

df.to_csv("cleaned_data.csv", index=False)  # Save the cleaned data
