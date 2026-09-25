import streamlit as st
import pandas as pd
import plotly.express as px
from analytics.sales_analysis import analyze_sales
from ai.insights import generate_insights

st.set_page_config(page_title="BizInsight AI", page_icon="📊", layout="wide")

st.title("📊 BizInsight AI")
st.caption("Business Sales & Decision Analytics Platform")

st.sidebar.header("Data Source")
uploaded = st.sidebar.file_uploader("Upload sales CSV", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
else:
    df = pd.read_csv("data/sample_sales.csv")
    st.sidebar.info("Using sample business data.")

required = {"date", "product", "sales", "cost"}
missing = required - set(df.columns.str.lower())
df.columns = [c.lower().strip() for c in df.columns]

if missing:
    st.error(f"Missing required columns: {', '.join(sorted(missing))}")
    st.stop()

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["sales"] = pd.to_numeric(df["sales"], errors="coerce").fillna(0)
df["cost"] = pd.to_numeric(df["cost"], errors="coerce").fillna(0)
df["profit"] = df["sales"] - df["cost"]
df = df.dropna(subset=["date"])

metrics = analyze_sales(df)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Sales", f"Rs. {metrics['total_sales']:,.0f}")
c2.metric("Total Cost", f"Rs. {metrics['total_cost']:,.0f}")
c3.metric("Profit", f"Rs. {metrics['profit']:,.0f}")
c4.metric("Profit Margin", f"{metrics['margin']:.1f}%")

st.divider()

left, right = st.columns(2)
with left:
    product_sales = df.groupby("product", as_index=False)["sales"].sum().sort_values("sales", ascending=False)
    fig = px.bar(product_sales, x="product", y="sales", title="Sales by Product")
    st.plotly_chart(fig, use_container_width=True)

with right:
    daily = df.groupby("date", as_index=False)["sales"].sum()
    fig = px.line(daily, x="date", y="sales", markers=True, title="Sales Trend")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("🤖 AI Business Insights")
question = st.text_input(
    "Ask about the business",
    placeholder="Example: Which product is performing best?"
)
if question:
    st.write(generate_insights(df, question))
else:
    st.info(generate_insights(df, "Give me a short business performance summary."))

st.subheader("📋 Sales Data")
st.dataframe(df, use_container_width=True)

st.download_button(
    "Download analyzed CSV",
    df.to_csv(index=False).encode("utf-8"),
    "analyzed_sales.csv",
    "text/csv"
)
