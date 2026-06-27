import pandas as pd
import numpy as np
from datetime import timedelta, date

#Set random seed so that the data looks consistent
np.random.seed(42)

#1.Generate random dates across 2025 (Prior Year) and 2026 (Current Year)
start_date = date(2025, 1, 1)
end_date = date(2026, 12, 31)
days_between = (end_date - start_date).days
dates = [start_date + timedelta(days=np.random.randint(0, days_between)) for _ in range(3000)]

#2 Assign Sales Channels (Matching your inspiration image)
channels=np.random.choice(['Online','Retail'],size=3000,p=[0.6,0.4])

#3 Assign Products and Financials
categories=np.random.choice(['Footwear','Apperal','Accessories'],size=3000)
sales=np.round(np.random.uniform(25,600,size=3000),2)
#Profit is calculated as a realistic 10% to 45 % margin on sales
profit=np.round(sales*np.random.uniform(0.10,0.45,size=3000),2)

# 4. Build the DataFrame
df = pd.DataFrame({
    'Order_ID': ['ORD-' + str(i).zfill(4) for i in range(1, 3001)],
    'Order_Date': dates,
    'Sales_Channel': channels,
    'Product_Category': categories,
    'Sales': sales,
    'Profit': profit
})

# Sort by date and save
df.sort_values('Order_Date', inplace=True)
df.to_csv('stride_athletics_sales.csv', index=False)

print("Success! stride_athletics_sales.csv has been generated with 3,000 records.")