"""Undervalued Cities page."""
import streamlit as st
import pandas as pd
import plotly.express as px
from app.utils import get_undervalued_cities, filter_cities

def show():
    """Display the Undervalued Cities page."""
    st.title("💎 Undervalued Cities")
    
    st.markdown("""
    Discover hidden opportunities: cities with high attractiveness potential but lower market attention.
    These cities represent emerging startup hubs that may offer better valuations and less competition.
    """)
    
    # Get all undervalued cities
    all_cities = get_undervalued_cities()
    
    # Filter by selected regions if applicable
    regions = st.session_state.get("selected_regions", ["All EU"])
    if regions and "All EU" not in regions:
        all_cities = all_cities[all_cities["region"].isin(regions)]
    
    # Statistics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Hidden Opportunities", len(all_cities), "🎯")
    
    with col2:
        avg_attract = all_cities["attractivenessIndex"].mean()
        st.metric("Avg Attractiveness", f"{avg_attract:.1f}", "⭐")
    
    with col3:
        avg_votes = all_cities["votes"].mean()
        st.metric("Avg Community Votes", int(avg_votes), "👍")
    
    st.divider()
    
    # Attractiveness vs Votes
    st.subheader("Hidden Gems: Attractiveness vs Market Attention")
    
    fig = px.scatter(
        all_cities,
        x="votes",
        y="attractivenessIndex",
        size="funding",
        color="status",
        hover_data=["name", "country", "region"],
        title="Undervalued Cities - Attractiveness vs Votes (bubble = funding)",
        color_discrete_map={
            "undervalued": "#FF6B6B",
            "hidden gem": "#4ECDC4",
            "rising": "#95E1D3"
        }
    )
    fig.update_layout(
        template="plotly",
        height=500,
        xaxis_title="Community Votes",
        yaxis_title="Attractiveness Index"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # By status
    st.subheader("Opportunities by Type")
    
    col1, col2 = st.columns(2)
    
    with col1:
        status_counts = all_cities["status"].value_counts()
        fig_status = px.pie(
            values=status_counts.values,
            names=status_counts.index,
            title="Count by Opportunity Type",
            color_discrete_sequence=["#FF6B6B", "#4ECDC4", "#95E1D3"]
        )
        fig_status.update_layout(template="plotly")
        st.plotly_chart(fig_status, use_container_width=True)
    
    with col2:
        region_counts = all_cities["region"].value_counts()
        fig_region = px.pie(
            values=region_counts.values,
            names=region_counts.index,
            title="Opportunities by Region"
        )
        fig_region.update_layout(template="plotly")
        st.plotly_chart(fig_region, use_container_width=True)
    
    # Detailed table
    st.subheader("Undervalued Cities - Detailed View")
    
    display_df = all_cities[[
        "name", "country", "region", "status", "attractivenessIndex",
        "votes", "funding", "attractivenessIndex"
    ]].copy()
    
    display_df.columns = [
        "City", "Country", "Region", "Type", "Attractiveness", 
        "Votes", "Funding (€M)", "Potential Score"
    ]
    
    display_df = display_df.sort_values("Attractiveness", ascending=False)
    
    st.dataframe(display_df, use_container_width=True)
    
    # Export option
    csv = display_df.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="undervalued_cities.csv",
        mime="text/csv"
    )
