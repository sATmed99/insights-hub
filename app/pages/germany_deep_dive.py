"""Germany Deep Dive page."""
import streamlit as st
import pandas as pd
import plotly.express as px
from app.utils import get_germany_cities, get_sector_stats

def show():
    """Display the Germany Deep Dive page."""
    st.title("🇩🇪 Germany Deep Dive")
    
    st.markdown("""
    Germany is the largest startup hub in continental Europe.
    Explore the detailed ecosystem of German tech cities.
    """)
    
    # Get Germany cities
    germany_df = get_germany_cities()
    
    # Statistics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("German Cities", len(germany_df), "🏙️")
    
    with col2:
        st.metric("Total Votes", int(germany_df["votes"].sum()), "👍")
    
    with col3:
        st.metric("Avg Attractiveness", f"{germany_df['attractivenessIndex'].mean():.1f}", "⭐")
    
    with col4:
        st.metric("Total Funding", f"€{germany_df['funding'].sum():.0f}M", "💰")
    
    st.divider()
    
    # Top German cities
    st.subheader("Top German Cities")
    
    fig = px.bar(
        germany_df.nlargest(10, "attractivenessIndex"),
        x="attractivenessIndex",
        y="name",
        orientation="h",
        color="attractivenessIndex",
        color_continuous_scale="RdYlGn",
        hover_data=["votes", "funding", "status"],
        title="German Cities by Attractiveness"
    )
    fig.update_layout(
        template="plotly",
        height=400,
        xaxis_title="Attractiveness Index",
        yaxis_title="City"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Votes distribution
    st.subheader("Votes Distribution")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_votes = px.scatter(
            germany_df,
            x="funding",
            y="votes",
            size="attractivenessIndex",
            color="status",
            hover_data=["name", "countryCode"],
            title="Funding vs Votes"
        )
        fig_votes.update_layout(template="plotly", height=400)
        st.plotly_chart(fig_votes, use_container_width=True)
    
    with col2:
        status_dist = germany_df["status"].value_counts()
        fig_status = px.pie(
            values=status_dist.values,
            names=status_dist.index,
            title="City Status Distribution"
        )
        fig_status.update_layout(template="plotly")
        st.plotly_chart(fig_status, use_container_width=True)
    
    # Sector distribution in Germany
    st.subheader("Sector Distribution in German Cities")
    
    sector_data = []
    for _, city in germany_df.iterrows():
        for sector, count in city["sectors"].items():
            sector_data.append({
                "City": city["name"],
                "Sector": sector,
                "Startups": count
            })
    
    sector_df = pd.DataFrame(sector_data)
    
    fig_sectors = px.bar(
        sector_df,
        x="City",
        y="Startups",
        color="Sector",
        barmode="stack",
        title="Sector Distribution Across German Cities"
    )
    fig_sectors.update_layout(
        template="plotly",
        height=400
    )
    st.plotly_chart(fig_sectors, use_container_width=True)
    
    # Regional comparison within Germany
    st.subheader("Detailed City Comparison")
    
    display_df = germany_df[[
        "name", "region", "votes", "attractivenessIndex", 
        "status", "funding"
    ]].copy()
    
    display_df.columns = ["City", "Region", "Votes", "Attractiveness", "Status", "Funding (€M)"]
    
    display_df = display_df.sort_values("Votes", ascending=False)
    
    st.dataframe(display_df, use_container_width=True)
