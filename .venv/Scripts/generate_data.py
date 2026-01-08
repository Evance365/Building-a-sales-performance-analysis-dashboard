import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Configuration
NUM_RECORDS = 5000
START_DATE = datetime(2022, 1, 1)
END_DATE = datetime(2024, 12, 31)

# Define business data
PRODUCTS = [
    'Laptop', 'Desktop', 'Monitor', 'Keyboard', 'Mouse', 
    'Headphones', 'Webcam', 'USB Cable', 'Hard Drive', 'SSD',
    'RAM', 'Graphics Card', 'Motherboard', 'Power Supply', 'Case'
]

REGIONS = ['North', 'South', 'East', 'West', 'Central']

CUSTOMERS = [f'CUST{str(i).zfill(4)}' for i in range(1, 301)]  # 300 customers

# Price ranges for products (min, max)
PRODUCT_PRICES = {
    'Laptop': (500, 2000),
    'Desktop': (600, 1800),
    'Monitor': (150, 800),
    'Keyboard': (20, 200),
    'Mouse': (10, 150),
    'Headphones': (30, 400),
    'Webcam': (40, 250),
    'USB Cable': (5, 30),
    'Hard Drive': (50, 300),
    'SSD': (60, 500),
    'RAM': (40, 300),
    'Graphics Card': (200, 1500),
    'Motherboard': (80, 600),
    'Power Supply': (50, 300),
    'Case': (40, 200)
}

def generate_sales_data(n_records):
    """Generate realistic sales data"""
    
    data = []
    
    for _ in range(n_records):
        # Random date
        days_diff = (END_DATE - START_DATE).days
        random_days = random.randint(0, days_diff)
        date = START_DATE + timedelta(days=random_days)
        
        # Random product
        product = random.choice(PRODUCTS)
        
        # Price based on product with some variation
        price_range = PRODUCT_PRICES[product]
        unit_price = round(random.uniform(price_range[0], price_range[1]), 2)
        
        # Quantity (most orders are small, few are large)
        quantity = int(np.random.exponential(2) + 1)
        quantity = min(quantity, 50)  # Cap at 50
        
        # Calculate revenue
        revenue = round(unit_price * quantity, 2)
        
        # Random region
        region = random.choice(REGIONS)
        
        # Random customer (with some customers buying more - Pareto principle)
        if random.random() < 0.2:  # 20% chance to be a top customer
            customer = random.choice(CUSTOMERS[:60])  # Top 60 customers
        else:
            customer = random.choice(CUSTOMERS)
        
        # Random sales rep
        sales_rep = f'REP{random.randint(1, 20):02d}'
        
        # Add some missing values (realistic scenario - 5% missing data)
        if random.random() < 0.05:
            sales_rep = None
        if random.random() < 0.03:
            region = None
        
        # Create record
        record = {
            'Order_ID': f'ORD{len(data)+1:06d}',
            'Date': date.strftime('%Y-%m-%d'),
            'Customer_ID': customer,
            'Product': product,
            'Quantity': quantity,
            'Unit_Price': unit_price,
            'Revenue': revenue,
            'Region': region,
            'Sales_Rep': sales_rep
        }
        
        data.append(record)
    
    return pd.DataFrame(data)

# Generate data
print("Generating sales data...")
df = generate_sales_data(NUM_RECORDS)

# Save to CSV
output_path = 'data/sales_data.csv'
df.to_csv(output_path, index=False)

print(f"\n✓ Generated {len(df)} sales records")
print(f"✓ Saved to: {output_path}")
print(f"\nData Preview:")
print(df.head())
print(f"\nData Info:")
print(df.info())
print(f"\nBasic Statistics:")
print(df.describe())