import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("🌦 Weather Forecast Dashboard")

# Load data
df = pd.read_csv(r"C:\Users\user19\Downloads\weather_forecast_data.csv")

# Show raw data
if st.checkbox("Show raw data"):
    st.write(df)

# Convert Date column if it exists
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# ====== Graph 1: Temperature Over Time ======
if 'Date' in df.columns and 'Temperature' in df.columns:
    st.subheader("📈 Temperature Over Time")
    fig_temp = px.line(df, x='Date', y='Temperature', title="Daily Temperature", markers=True)
    st.plotly_chart(fig_temp)

# ====== Graph 2: Rainfall Over Time ======
if 'Date' in df.columns and 'Rainfall' in df.columns:
    st.subheader("🌧 Rainfall Over Time")
    fig_rain = px.bar(df, x='Date', y='Rainfall', title="Daily Rainfall", color='Rainfall')
    st.plotly_chart(fig_rain)

# ====== Graph 3: Temperature vs Humidity ======
if 'Temperature' in df.columns and 'Humidity' in df.columns:
    st.subheader("💧 Temperature vs Humidity")
    fig_scatter = px.scatter(df, x='Temperature', y='Humidity', title="Temperature vs Humidity", size='Humidity', color='Temperature')
    st.plotly_chart(fig_scatter)

# ====== Graph 4: Average Temperature by Location ======
if 'Location' in df.columns and 'Temperature' in df.columns:
    st.subheader("📍 Average Temperature by Location")
    avg_temp = df.groupby('Location')['Temperature'].mean().reset_index()
    fig_bar = px.bar(avg_temp, x='Location', y='Temperature', title="Average Temperature by Location", color='Temperature')
    st.plotly_chart(fig_bar)
