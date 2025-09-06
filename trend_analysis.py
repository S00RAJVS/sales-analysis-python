# Import necessary libraries
import pandas as pd              # For handling and analyzing data
import seaborn as sns            # For creating attractive visualizations
import matplotlib.pyplot as plt  # For plotting charts

# Load the time-series sales data from CSV file
# 'parse_dates' ensures the 'Date' column is read as datetime objects
df = pd.read_csv('sales_data.csv', parse_dates=['Date'])

# Set the 'Date' column as the index (important for time-series operations)
df.set_index('Date', inplace=True)

# Resample the data by month ('M') and calculate total sales for each month
monthly_sales = df['Sales'].resample('ME').sum()

# -------------------- PLOT 1 --------------------
plt.figure(figsize=(10, 5))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values)
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")  # Save plot as PNG
plt.show()

# -------------------- PLOT 2 --------------------
monthly_sales.rolling(3).mean().plot(label='3-Month Avg', linewidth=2)
monthly_sales.plot(label='Actual', alpha=0.5)
plt.legend()
plt.title('Sales with Rolling Average')
plt.tight_layout()
plt.savefig("sales_with_rolling_avg.png")  # Save plot as PNG
plt.show()
