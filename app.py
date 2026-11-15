import pandas as pd
import streamlit as st

st.set_page_config(page_title="Qahwa Corner Sales", page_icon="☕", layout="wide")
st.title("☕ Qahwa Corner – Sales Dashboard (Jan–Jun 2026)")


@st.cache_data
def load_data():
    return pd.read_csv("cafe_sales.csv", parse_dates=["date"])


df = load_data()

# 1) Branch selector
branch = st.selectbox("Select a branch", ["All branches"] + sorted(df["branch"].unique()))
data = df if branch == "All branches" else df[df["branch"] == branch]

# 2) Total-revenue metric
col1, col2 = st.columns(2)
col1.metric("Total revenue (SAR)", f"{data['total_sar'].sum():,.0f}")
col2.metric("Number of orders", f"{len(data):,}")

# 3) Bar chart of revenue by product
st.subheader(f"Revenue by product – {branch}")
rev_by_product = data.groupby("product")["total_sar"].sum().sort_values(ascending=False)
st.bar_chart(rev_by_product, x_label="Product", y_label="Revenue (SAR)")
