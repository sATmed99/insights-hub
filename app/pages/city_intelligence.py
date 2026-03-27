"""City Intelligence page."""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app.utils import filter_cities, get_top_cities, get_region_stats

def show():
    """Display the City Intelligence page."""
    st.title("🏙️ City Intelligence")
    
    # Get filter values from session state
    regions = st.session_state.get("selected_regions", ["All EU"])
    sectors = st.session_state.get("selected_sectors", ["Fintech", "SaaS", "Healthtech", "Edtech"])
    
    # Filter the data
    cities_df = filter_cities(regions=regions, sectors=sectors)
    
    # Display statistics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Cities", len(cities_df), "📍")
    
    with col2:
        st.metric("Total Votes", int(cities_df["votes"].sum()), "👍")
    
    with col3:
        st.metric("Avg Attractiveness", f"{cities_df['attractivenessIndex'].mean():.1f}", "⭐")
    
    with col4:
        st.metric("Total Funding (€M)", int(cities_df["funding"].sum()), "💰")
    
    st.divider()
    
    # Top cities chart
    st.subheader("Top Cities by Attractiveness")
    top_cities = get_top_cities(cities_df, n=15)
    
    fig = px.bar(
        top_cities,
        x="attractivenessIndex",
        y="name",
        orientation="h",
        color="attractivenessIndex",
        color_continuous_scale="Viridis",
        hover_data=["country", "region", "votes"],
        title="Top 15 Cities by Attractiveness Index"
    )
    fig.update_layout(
        xaxis_title="Attractiveness Index",
        yaxis_title="City",
        height=500,
        template="plotly_dark",
        hovermode="y unified"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Votes vs Attractiveness scatter plot
    st.subheader("Votes vs Attractiveness")
    fig_scatter = px.scatter(
        cities_df,
        x="votes",
        y="attractivenessIndex",
        size="funding",
        color="region",
        hover_data=["name", "country"],
        title="Cities: Votes vs Attractiveness (bubble size = funding)"
    )
    fig_scatter.update_layout(
        template="plotly_dark",
        height=500,
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Region statistics
    st.subheader("Region Statistics")
    region_stats = get_region_stats(cities_df)
    
    fig_region = px.bar(
        region_stats,
        x="Region",
        y="Total Votes",
        color="Avg Attractiveness",
        hover_data=["Cities", "Total Funding"],
        title="Votes and Attractiveness by Region"
    )
    fig_region.update_layout(
        template="plotly_dark",
        height=400,
    )
    st.plotly_chart(fig_region, use_container_width=True)
    
    # City ranking table
    st.subheader("City Rankings")
    ranking_df = cities_df[["name", "country", "region", "attractivenessIndex", "votes", "status", "funding"]].copy()
    ranking_df = ranking_df.sort_values("attractivenessIndex", ascending=False)
    ranking_df.columns = ["City", "Country", "Region", "Attractiveness", "Votes", "Status", "Funding (€M)"]
    
    st.dataframe(ranking_df, use_container_width=True)
