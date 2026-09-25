# 📊 BizInsight AI

**BizInsight AI** is a business sales and decision analytics dashboard built with Python, Pandas and Streamlit.

It combines **Business + Information Technology + Data Analytics** concepts in one portfolio project.

## Features

- Upload sales data using CSV
- Calculate total sales
- Calculate total cost
- Calculate estimated profit
- Calculate profit margin
- Identify top-selling and low-performing products
- Visualize product sales
- Visualize sales trends
- Generate basic business insights
- Download analyzed data

## Tech Stack

- Python
- Pandas
- Plotly
- Streamlit
- CSV
- SQL schema included for future database integration

## CSV Format

Your CSV should contain:

```text
date,product,sales,cost
2026-09-01,Shirt,15000,9000
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/BizInsight-AI.git
cd BizInsight-AI
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The dashboard will open in your browser.

## Project Structure

```text
BizInsight-AI/
├── app.py
├── analytics/
│   └── sales_analysis.py
├── ai/
│   └── insights.py
├── database/
│   └── schema.sql
├── data/
│   └── sample_sales.csv
├── .env.example
├── requirements.txt
└── README.md
```

## Future Improvements

- MySQL integration
- Real LLM API integration
- Customer segmentation
- Inventory forecasting
- Sales prediction
- Authentication and role-based access
- PDF business reports
- Automated email reports

## Disclaimer

This project is for educational and portfolio purposes. Business calculations depend on the quality and completeness of the uploaded data.
