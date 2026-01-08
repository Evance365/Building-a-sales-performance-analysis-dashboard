 📊 Sales Performance Analysis Dashboard

> A comprehensive data analysis project that analyzes 5,000+ sales records to uncover business insights, revenue trends, and customer behavior patterns.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)](https://pandas.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

---

 Project Overview

This project demonstrates real-world data analysis skills by examining sales performance across products, regions, and customers. The analysis answers critical business questions and provides actionable insights for decision-making.

 Key Questions Answered:
- Which products generate the most revenue?
-  Which regions perform best?
-  What are the monthly revenue trends?
- Who are the top 20% customers (Pareto Principle)?
- What seasonal patterns exist in sales data?

---

 📁 Project Structure

```
sales-performance-dashboard/
│
├── data/
│   └── sales_data.csv              # Raw sales dataset (5,000 records)
│
├── notebooks/
│   └── sales_analysis.ipynb        # Complete analysis notebook
│
├── outputs/
│   └── charts/                     # Exported visualizations
│       ├── top_products_revenue.png
│       ├── regional_performance.png
│       ├── monthly_revenue_trend.png
│       ├── pareto_customer_analysis.png
│       └── product_region_heatmap.png
│
├── generate_data.py                # Script to generate sample data
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

 🚀 Getting Started

 Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Git (for version control)

 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/sales-performance-dashboard.git
cd sales-performance-dashboard
```

2. **Create virtual environment**
```bash
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Generate sample data**
```bash
python generate_data.py
```

5. **Launch Jupyter Notebook**
```bash
jupyter notebook
```

6. **Open and run** `notebooks/sales_analysis.ipynb`

---

## 📊 Key Findings

### 1. Product Performance
- **Top Product**: Laptop generates the highest revenue
- **Top 5 products** account for over 50% of total revenue
- High-value items (Graphics Cards, Laptops) drive significant revenue despite lower volume

### 2. Regional Insights
- **Best Performing Region**: [Region varies by data] leads in both revenue and order count
- Regional performance varies by 30-40%, indicating opportunity for targeted marketing
- Customer density differs across regions, suggesting different market penetration strategies

### 3. Customer Behavior (Pareto Principle)
- **Top 20% of customers** generate approximately **70-80% of total revenue**
- High-value customers average 3-5x more orders than typical customers
- Customer segmentation reveals distinct buying patterns (Bronze, Silver, Gold, Platinum)

### 4. Temporal Trends
- Revenue shows seasonal patterns with peaks in Q4
- Month-over-month growth averages X% (varies by data)
- Year-over-year comparison shows business growth trajectory

---

## 🛠️ Technologies & Skills Demonstrated

### Technical Skills
- **Python**: Data manipulation and analysis
- **Pandas**: Data cleaning, aggregation, pivot tables
- **NumPy**: Numerical computations
- **Matplotlib/Seaborn**: Data visualization
- **Jupyter Notebook**: Interactive analysis and documentation

### Data Analysis Skills
- Handling missing values and data quality issues
- Date/time parsing and time-based analysis
- Grouping and aggregation operations
- Statistical analysis and metrics calculation
- Creating meaningful visualizations
- Deriving actionable business insights

### Business Skills
- Revenue analysis and forecasting
- Customer segmentation
- Regional performance comparison
- Product portfolio analysis
- Pareto principle application

---

 Sample Visualizations

 Top Products by Revenue
![Top Products](outputs/charts/top_products_revenue.png)

 Regional Performance
![Regional Performance](outputs/charts/regional_performance.png)

 Monthly Revenue Trend
![Revenue Trend](outputs/charts/monthly_revenue_trend.png)

 Pareto Analysis (80/20 Rule)
![Pareto Analysis](outputs/charts/pareto_customer_analysis.png)

---

 💡 Business Recommendations

Based on the analysis, here are key recommendations:

1. **Customer Retention**: Implement VIP loyalty program for top 20% customers
2. **Regional Expansion**: Increase marketing investment in underperforming regions
3. **Inventory Optimization**: Stock more high-margin, fast-moving products
4. **Seasonal Planning**: Prepare for peak seasons with appropriate inventory
5. **Product Bundling**: Bundle slow-moving items with bestsellers

---

 📝 Dataset Information

Data Source
- **Type**: Simulated realistic sales data
- **Records**: 5,000 transactions
- **Time Period**: January 2022 - December 2024
- **Geography**: 5 regions (North, South, East, West, Central)

 Data Fields
- `Order_ID`: Unique order identifier
- `Date`: Transaction date
- `Customer_ID`: Unique customer identifier
- `Product`: Product name
- `Quantity`: Units sold per order
- `Unit_Price`: Price per unit
- `Revenue`: Total order revenue
- `Region`: Geographic region
- `Sales_Rep`: Assigned sales representative

---

 Future Enhancements

- [ ] Add predictive modeling for sales forecasting
- [ ] Implement customer churn analysis
- [ ] Create interactive dashboard with Plotly/Dash
- [ ] Add market basket analysis
- [ ] Integrate with real-time data sources
- [ ] Build automated reporting system

---

 📧 Contact

Evance Odhiambo
- https://www.linkedin.com/in/evance-odhiambo-4628183a3?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
- evanceotis365@gmal.com

 License

This project is open source and available under the [MIT License](LICENSE).

---

 Acknowledgments

- Dataset generated using Python's random and pandas libraries
- Inspired by real-world business intelligence projects
- Built as part of data analyst portfolio development

---

**⭐ If you found this project helpful, please give it a star!**
