#  E-Commerce Customer Behavior & Basket Analysis (EDA)

 **End-to-End Data Analysis Project**
 From Raw Data → Insights → Business Decisions

---

##  Project Overview

This project explores real-world e-commerce transactions to understand **customer behavior**, **sales dynamics**, and **product relationships**. The analysis transforms raw data into actionable insights using data cleaning, feature engineering, and visualization.

---

##  Objectives

* Identify **top-selling products**
* Detect **VIP customers** (high revenue contributors)
* Analyze **hourly sales patterns**
* Explore **country-wise revenue distribution**
* Perform **basket analysis** (product relationships)
* Evaluate **basket value distribution**

---

##  Tech Stack

* Python
* Pandas / NumPy
* Matplotlib / Seaborn

---

##  Data Cleaning

* Removed missing values
* Filtered negative quantities (returns)
* Removed zero-priced transactions

---

##  Feature Engineering

* Created: **TotalPrice = Quantity × UnitPrice**
* Extracted: **Hour from InvoiceDate**

---

#  VISUAL ANALYSIS REPORT

---

##  Top Selling Products

![Top Products](images/top_products.png)

**Insight:**

* A small number of products dominate total sales
* Strong indication of **Pareto distribution (80/20 rule)**

---

##  VIP Customers (Revenue Leaders)

![Top Customers](images/top_customers.png)

**Insight:**

* A few customers generate a large portion of total revenue
* Opportunity for **loyalty programs & retention strategies**

---

##  Hourly Sales Trend

![Hourly Sales](images/hourly_sales.png)

**Insight:**

* Peak sales occur around **midday (12:00–14:00)**
* Low activity during early hours

  **Action:** Schedule campaigns during peak hours

---

##  Revenue by Country

![Country Sales](images/country_sales.png)

**Insight:**

* Revenue is heavily concentrated in a few countries
* Market dependency risk exists

---

##  Basket Analysis (Product Relationships)

![Correlation](images/correlation.png)

**Insight:**

* Certain products are frequently purchased together
* Strong candidates for **bundle strategies**

---

##  Basket Value Distribution

![Basket Value](images/basket_value.png)

**Insight:**

* Most purchases fall into a mid-range spending level
* High-value baskets are less frequent but impactful

---

#  DATA TABLE SNAPSHOT

## Top Countries by Revenue

| Country        | Revenue Rank |
| -------------- | ------------ |
| United Kingdom | 1            |
| Germany        | 2            |
| France         | 3            |
| EIRE           | 4            |
| Spain          | 5            |

---

#  KEY INSIGHTS

>  A small subset of products and customers drives the majority of revenue.

>  Sales behavior is time-dependent and predictable.

>  Product relationships open opportunities for cross-selling.

---

# 📈 BUSINESS IMPACT

This analysis enables:

*  **Inventory Optimization** → Stock high-demand items
*  **Customer Targeting** → Focus on VIP customers
*  **Campaign Timing** → Maximize conversions
*  **Product Bundling** → Increase average basket size

---

#  PROJECT STRUCTURE

```
project/
│
├── data/
├── images/
├── src/
├── README.md
└── requirements.txt
```

---

#  FUTURE WORK

* Customer segmentation (RFM)
* Recommendation system (Apriori / ML)
* Sales forecasting (Time Series)

---



---

⭐ If you found this project useful, consider starring the repo!
