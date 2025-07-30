import streamlit as st
import pandas as pd
import altair as alt
from aviationstack_api import get_flights_data
from utils import process_flight_data

st.set_page_config(page_title="Airline Market Demand Dashboard", layout="wide")

st.title("✈️ Real-Time Airline Booking Demand Insights")
st.markdown("Showing live airline market trends using Aviationstack API")

with st.spinner("Fetching live airline data..."):
    flights = get_flights_data()  
    df = process_flight_data(flights)

if df.empty:
    st.error("No flight data available.")
else:
    st.success(f"Fetched {len(df)} real-time flights")

    st.subheader("🔍 Flight Status Distribution")
    status_chart = alt.Chart(df).mark_bar().encode(
        x='status',
        y='count()',
        color='status'
    ).properties(height=300)
    st.altair_chart(status_chart, use_container_width=True)

    st.subheader("🧭 Popular Routes")
    route_df = df.groupby(['dep_airport', 'arr_airport']).size().reset_index(name='count')
    top_routes = route_df.sort_values('count', ascending=False).head(10)

    route_chart = alt.Chart(top_routes).mark_bar().encode(
        x='count',
        y=alt.Y('dep_airport:N', sort='-x'),
        color='arr_airport:N',
        tooltip=['dep_airport', 'arr_airport', 'count']
    ).properties(height=400)
    st.altair_chart(route_chart, use_container_width=True)

    st.subheader("🛫 Top Airlines by Flights")
    airline_df = df['airline_name'].value_counts().reset_index()
    airline_df.columns = ['airline', 'count']

    airline_chart = alt.Chart(airline_df.head(10)).mark_bar().encode(
        x='count',
        y=alt.Y('airline:N', sort='-x'),
        color='airline:N'
    ).properties(height=400)
    st.altair_chart(airline_chart, use_container_width=True)

    st.dataframe(df.head(50), use_container_width=True)

st.header("📊 Real-Time Market Demand Summary")

airline_summary = df['airline_name'].value_counts().head(3)
top_airlines = ", ".join(airline_summary.index.tolist())

top_departures = df['dep_airport'].value_counts().head(3)
top_dep_airports = ", ".join(top_departures.index.tolist())

route_df = df.groupby(['dep_airport', 'arr_airport']).size().reset_index(name='count')
top_route = route_df.sort_values('count', ascending=False).head(1)
top_route_str = f"{top_route.iloc[0]['dep_airport']} → {top_route.iloc[0]['arr_airport']}"

status_counts = df['status'].value_counts()
status_info = ", ".join([f"{k}: {v}" for k, v in status_counts.items()])

st.markdown(f"""
### 📝 Summary Report

- **Top Airlines Operating Now:** {top_airlines}  
- **Most Active Departure Airports:** {top_dep_airports}  
- **Busiest Route Right Now:** {top_route_str}  
- **Flight Status Breakdown:** {status_info}  
""")
