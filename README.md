# 📈 Data-Driven Stock Analysis

## Project Overview

The **Data-Driven Stock Analysis** project focuses on organizing, cleaning, analyzing, and visualizing historical stock market data.

The project uses Python and Pandas for data processing and analysis, SQL for structured data storage, Power BI for business intelligence visualization, and Streamlit for building an interactive web application.

The objective is to identify stock market trends, compare stock performance, analyze volatility, calculate cumulative returns, study sector-wise performance, identify monthly gainers and losers, and analyze correlations between stocks.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Organize raw stock market data into a structured format
- Clean and preprocess stock data
- Analyze yearly stock performance
- Identify top-performing and worst-performing stocks
- Calculate market-level statistics
- Measure stock volatility
- Calculate cumulative returns
- Analyze sector-wise performance
- Identify monthly top gainers and losers
- Analyze correlations between different stocks
- Store processed data using SQL
- Build an interactive Power BI dashboard
- Develop an interactive Streamlit web application

---

## 🛠️ Technologies Used

### Programming
- Python

### Data Analysis
- Pandas
- NumPy

### Data Visualization
- Plotly
- Matplotlib
- Power BI

### Database
- SQL

### Web Application
- Streamlit

### Development Tools
- Jupyter Notebook
- VS Code / Python Environment
- Git
- GitHub

---

## 📂 Project Workflow

The overall project workflow is:

```text
Raw Stock Data
      ↓
Data Organization
      ↓
Data Cleaning
      ↓
50 Individual Stock CSV Files
      ↓
Combined Stock Dataset
      ↓
Exploratory Data Analysis
      ↓
Stock Performance Analysis
      ↓
SQL Database
      ↓
Power BI Dashboard
      ↓
Streamlit Web Application
```

---

## 🧹 Data Cleaning

The raw stock market data was cleaned and transformed using Python and Pandas.

The major preprocessing steps included:

- Converting date columns into datetime format
- Removing duplicate records
- Checking missing values
- Sorting records chronologically
- Standardizing the structure of stock files
- Combining individual stock datasets for market-level analysis

The cleaned dataset contains important fields such as:

- Ticker
- Date
- Open
- High
- Low
- Close
- Volume
- Month

---

# 📊 Stock Market Analysis

## 1. Top 10 Performing Stocks

Yearly returns were calculated for every stock.

The stocks were ranked based on their yearly return to identify the **Top 10 Performing Stocks**.

Yearly Return:

```text
(Final Closing Price - Initial Closing Price)
------------------------------------------------
              Initial Closing Price
```

---

## 2. Bottom 10 Performing Stocks

Stocks were sorted in ascending order based on yearly return to identify the **Bottom 10 Performing Stocks**.

These represent the stocks with the lowest performance during the analysis period.

---

## 3. Market Summary

The market overview contains the following important KPIs:

- Total number of stocks
- Number of green stocks
- Number of red stocks
- Average closing price
- Average trading volume

A **Green Stock** represents a stock with a positive return during the analysis period.

A **Red Stock** represents a stock with a negative return during the analysis period.

---

## 4. Volatility Analysis

Volatility measures how much a stock's returns fluctuate over time.

Daily returns were first calculated using percentage change in closing prices.

```text
Daily Return =
(Current Close - Previous Close) / Previous Close
```

Volatility was calculated using the standard deviation of daily returns.

Higher volatility indicates larger fluctuations in stock returns.

The project identifies the **Top 10 Highly Volatile Stocks**.

---

## 5. Cumulative Return Analysis

Cumulative return represents the compounded performance of a stock over the complete analysis period.

It was calculated using daily returns.

```text
Cumulative Return =
(1 + Daily Return).cumprod() - 1
```

This analysis helps understand how an investment would have performed over time.

---

## 6. Sector-wise Performance

Stocks were grouped based on their respective sectors.

The average yearly return for each sector was calculated to compare performance across industries.

This analysis helps identify stronger and weaker performing sectors.

---

## 7. Stock Correlation Analysis

A correlation matrix was created using closing prices of different stocks.

Correlation values range from:

```text
-1 to +1
```

- **+1** → Strong positive relationship
- **0** → Little or no linear relationship
- **-1** → Strong negative relationship

The results are displayed using a **Correlation Heatmap**.

---

## 8. Monthly Top 5 Gainers and Losers

Monthly returns were calculated using the first and last closing prices of every stock for each month.

For every month, the project identifies:

- Top 5 Gainers
- Top 5 Losers

This provides a month-by-month view of stock market performance.

---

# 📊 Power BI Dashboard

A Power BI dashboard was developed to provide an interactive visual representation of the stock market analysis.

The Power BI report contains two main pages.

## Page 1 — Market Overview

The Market Overview dashboard contains:

- Total Stocks
- Green Stocks
- Red Stocks
- Average Price
- Average Volume
- Top 10 Performing Stocks
- Bottom 10 Performing Stocks
- Sector-wise Performance
- Top 10 Volatile Stocks

## Page 2 — Detailed Analysis

The Detailed Analysis dashboard contains:

- Ticker selection
- Stock Price Trend
- Cumulative Return Trend
- Monthly Top 5 Gainers
- Monthly Top 5 Losers
- Month filters
- Stock Correlation Heatmap

Power BI screenshots are also included inside the Streamlit application to demonstrate the completed BI dashboard.

---

# 🌐 Streamlit Application

An interactive Streamlit application was developed to allow users to explore the stock market analysis through a web interface.

The application contains the following pages:

### 📊 Market Overview

Displays:

- Market KPIs
- Top 10 stocks
- Bottom 10 stocks
- Volatility analysis
- Sector-wise performance

### 📈 Stock Analysis

Users can select an individual ticker and dynamically view:

- First closing price
- Latest closing price
- Yearly return
- Volatility
- Closing price trend
- Cumulative return trend
- Dynamic stock insights

### 📅 Monthly Analysis

Users can select a month and view:

- Top 5 monthly gainers
- Top 5 monthly losers
- Monthly return charts
- Monthly performance tables

### 🔥 Correlation Analysis

Displays an interactive stock correlation heatmap.

### 📊 Power BI Dashboard

Displays the completed Power BI dashboard pages inside the Streamlit application.

### 📘 About

Provides explanations of important financial concepts including:

- Yearly Return
- Daily Return
- Volatility
- Cumulative Return
- Correlation
- Green and Red Stocks

---

# 🗄️ SQL Database

The cleaned and processed stock market data is stored in a SQL database.

SQL is used to provide structured storage and querying of the processed stock information.

The database component enables stock data to be retrieved and analyzed using SQL queries.

---

# 📁 Project Structure

```text
project_2_DD/
│
├── app.py
│
├── README.md
├── requirements.txt
│
├── images/
│   ├── powerbi_page1.png
│   └── powerbi_page2.png
│
├── powerbi_data/
│   ├── stock_market_data.csv
│   ├── stock_summary.csv
│   ├── cumulative_returns.csv
│   ├── monthly_top_5_gainers.csv
│   ├── monthly_top_5_loosers.csv
│   └── correlation_long.csv
│
├── cleaned_stock_csv/
│
├── stock_csv/
│
├── Power BI Dashboard/
│
└── Python Analysis Files/
```

> The exact project structure may vary depending on the local development environment.

---

# 🚀 How to Run the Streamlit Application

## 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

## 2. Navigate to the Project Directory

```bash
cd project_2_DD
```

## 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

## 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in the browser.

---

# 📦 Requirements

The major Python packages used in the project include:

```text
streamlit
pandas
numpy
plotly
matplotlib
```

Additional database packages can be included depending on the SQL database configuration.

---

# 📈 Key Insights

The project provides insights into:

- Overall stock market performance
- Best and worst-performing stocks
- Positive and negative performing stocks
- Highly volatile stocks
- Long-term cumulative stock performance
- Performance differences between sectors
- Monthly market leaders and laggards
- Relationships between stock price movements

---

# 💡 Business Use Cases

This analysis can help:

- Investors compare historical stock performance
- Analysts identify market trends
- Users identify high-volatility stocks
- Investors compare sector performance
- Analysts understand relationships between stocks
- Users monitor monthly gainers and losers
- Support data-driven investment research

> This project is intended for educational and analytical purposes and should not be considered financial advice.

---

# 🔮 Future Improvements

Possible future improvements include:

- Real-time stock market API integration
- Automated data updates
- Technical indicators
- Moving averages
- Portfolio analysis
- Risk-return analysis
- Machine learning-based forecasting
- Cloud-hosted SQL database
- Enhanced Power BI integration

---

# 👨‍💻 Author

**Janardhanan**

Data Science / AI & Machine Learning

---

## ⭐ Conclusion

This project demonstrates an end-to-end data analytics workflow using **Python, Pandas, SQL, Power BI, Plotly, and Streamlit**.

It transforms raw stock market data into structured information and presents the results through interactive dashboards, enabling users to explore stock performance, volatility, cumulative returns, sector trends, monthly performance, and correlations.