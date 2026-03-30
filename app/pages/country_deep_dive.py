"""Country Deep Dive page."""
import streamlit as st
import pandas as pd
import plotly.express as px
from app.data import get_cities_dataframe

def show():
    """Display the Country Deep Dive page."""
    st.title("🌍 Country Deep Dive")
    
    st.markdown("""
    Compare startup ecosystems across different European countries.
    """)
    
    all_cities = get_cities_dataframe()
    
    # Select a country
    countries = sorted(all_cities["country"].unique())
    selected_country = st.selectbox("Select a Country", countries)
    
    # Filter for selected country
    country_df = all_cities[all_cities["country"] == selected_country]
    
    # Statistics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Cities", len(country_df), "🏙️")
    
    with col2:
        st.metric("Total Votes", int(country_df["votes"].sum()), "👍")
    
    with col3:
        st.metric("Avg Attractiveness", f"{country_df['attractivenessIndex'].mean():.1f}", "⭐")
    
    with col4:
        st.metric("Total Funding", f"€{country_df['funding'].sum():.0f}M", "💰")
    
    st.divider()
    
    # Cities in the country
    st.subheader(f"Cities in {selected_country}")
    
    fig = px.bar(
        country_df.sort_values("attractivenessIndex", ascending=False),
        x="attractivenessIndex",
        y="name",
        orientation="h",
        color="votes",
        color_continuous_scale="Viridis",
        hover_data=["region", "votes", "funding"],
        title=f"Cities in {selected_country} by Attractiveness"
    )
    fig.update_layout(
        template="plotly",
        height=max(300, len(country_df) * 30),
        xaxis_title="Attractiveness Index",
        yaxis_title="City"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Sector distribution
    st.subheader(f"Sector Distribution in {selected_country}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        sector_data = []
        for _, city in country_df.iterrows():
            for sector, count in city["sectors"].items():
                sector_data.append({
                    "Sector": sector,
                    "Startups": count
                })
        
        sector_df = pd.DataFrame(sector_data)
        sector_summary = sector_df.groupby("Sector")["Startups"].sum().reset_index()
        
        fig_sectors = px.pie(
            sector_summary,
            values="Startups",
            names="Sector",
            title=f"Sector Distribution in {selected_country}"
        )
        fig_sectors.update_layout(template="plotly")
        st.plotly_chart(fig_sectors, use_container_width=True)
    
    with col2:
        status_counts = country_df["status"].value_counts()
        fig_status = px.pie(
            values=status_counts.values,
            names=status_counts.index,
            title=f"City Status Distribution in {selected_country}"
        )
        fig_status.update_layout(template="plotly")
        st.plotly_chart(fig_status, use_container_width=True)
    
    # Funding vs Attractiveness
    st.subheader("Funding vs Attractiveness")
    
    fig_scatter = px.scatter(
        country_df,
        x="votes",
        y="attractivenessIndex",
        size="funding",
        color="status",
        hover_data=["name", "region"],
        title=f"Funding vs Attractiveness in {selected_country}"
    )
    fig_scatter.update_layout(
        template="plotly",
        height=400
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Detailed comparison table
    st.subheader("City Details")
    
    display_df = country_df[[
        "name", "region", "votes", "attractivenessIndex",
        "status", "funding"
    ]].copy()
    
    display_df.columns = ["City", "Region", "Votes", "Attractiveness", "Status", "Funding (€M)"]
    display_df = display_df.sort_values("Votes", ascending=False)
    
    st.dataframe(display_df, use_container_width=True)
    
    # Export option
    csv = display_df.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name=f"{selected_country}_cities.csv",
        mime="text/csv"
    )
