import pandas as pd
import numpy as np
from pathlib import Path

# Create weekly dates for three years (2022-2024)
dates = pd.date_range(start='2022-01-01', end='2024-12-31', freq='W')

# Seed for reproducibility
np.random.seed(42)

# Simulate seasonal sales pattern (kg/week) with some randomness
seasonal_pattern = np.sin(np.linspace(0, 6 * np.pi, len(dates)))  # 3 cycles (annual seasonality)
sales_quantity = (seasonal_pattern * 50 + 200) + np.random.normal(0, 10, len(dates))

# Create DataFrame with sales quantity rounded and cast as integer
data = pd.DataFrame({
    'date': dates,
    'product': 'Salmon Fillet',
    'sales_quantity': np.round(sales_quantity).astype(int)
})

print("✅ Generating synthetic sales data.")

# Define and create output directory
output_dir = Path.cwd() / 'data'
output_dir.mkdir(parents=True, exist_ok=True)

# Save CSV file
output_path = output_dir / 'kalamesta_sales.csv'
data.to_csv(output_path, index=False)

# Confirm CSV creation
if output_path.exists():
    print(f"✅ CSV successfully saved at: {output_path.resolve()}")
else:
    print(f"❌ CSV file not found at: {output_path.resolve()}")
