"""Sector Map page."""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app.utils import filter_cities, get_sector_stats
from app.data import get_cities_dataframe

def show():
    """Display the Sector Map page."""
    st.title("🗺️ Sector Map")
    
    # Get filter values from session state
    regions = st.session_state.get("selected_regions", ["All EU"])
    sectors = st.session_state.get("selected_sectors", ["Fintech", "SaaS", "Healthtech", "Edtech"])
    
    # Filter the data
    cities_df = filter_cities(regions=regions, sectors=sectors)
    
    st.markdown("""
    Explore the distribution of tech startups across different sectors in European cities.
    """)
    
    # Sector overview
    st.subheader("Sector Overview")
    
    sector_stats = get_sector_stats(cities_df)
    
    fig = px.bar(
        sector_stats,
        x="Sector",
        y="Total Startups",
        color="Sector",
        title="Total Startups by Sector",
        height=400
    )
    fig.update_layout(
        template="plotly",
        showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Sector by region heatmap
    st.subheader("Sector Distribution by Region")
    
    sector_region_data = []
    regions_list = cities_df["region"].unique()
    sectors_list = ["Fintech", "Edtech", "Healthtech", "SaaS", "Deeptech"]
    
    for region in regions_list:
        region_df = cities_df[cities_df["region"] == region]
        for sector in sectors_list:
            total = region_df["sectors"].apply(lambda x: x.get(sector, 0)).sum()
            sector_region_data.append({
                "Region": region,
                "Sector": sector,
                "Count": total
            })
    
    sector_region_df = pd.DataFrame(sector_region_data)
    
    fig_heatmap = px.density_heatmap(
        sector_region_df,
        x="Sector",
        y="Region",
        z="Count",
        color_continuous_scale="Viridis",
        nbinsx=5,
        nbinsy=5,
        title="Sector Density by Region"
    )
    fig_heatmap.update_layout(
        template="plotly",
        height=500,
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)
    
    # Sector specialization by city
    st.subheader("City Sector Specialization")
    
    top_cities = cities_df.nlargest(10, "votes")
    
    sector_city_data = []
    for _, city in top_cities.iterrows():
        for sector, count in city["sectors"].items():
            sector_city_data.append({
                "City": city["name"],
                "Sector": sector,
                "Count": count
            })
    
    sector_city_df = pd.DataFrame(sector_city_data)
    
    fig_city_sector = px.bar(
        sector_city_df,
        x="City",
        y="Count",
        color="Sector",
        barmode="stack",
        title="Sector Distribution in Top 10 Cities",
        height=400
    )
    fig_city_sector.update_layout(
        template="plotly",
    )
    st.plotly_chart(fig_city_sector, use_container_width=True)
    
    # Sector statistics table
    st.subheader("Sector Statistics")
    
    all_cities_df = get_cities_dataframe()
    sector_stats_full = get_sector_stats(all_cities_df)
    
    st.dataframe(sector_stats_full, use_container_width=True)
