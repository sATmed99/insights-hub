"""Geographic analytics page."""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app.real_data import (
    get_top_cities,
    get_continent_distribution,
    load_startups_data,
    get_startups_by_region,
)


def show():
    """Display the Geographic Analytics page."""
    st.title("🌍 Geographic Distribution")
    
    st.markdown("""
    Analyze startup distribution across continents, countries, and cities worldwide.
    """)
    
    # Get data
    startups_df = load_startups_data()
    cities_df = get_top_cities(50)
    cities_df["votes"] = pd.to_numeric(cities_df["votes"], errors="coerce").fillna(0)
    continent_df = get_continent_distribution()
    
    # Tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["Continental View", "Geographic Heatmap", "Regional Breakdown", "City Comparison"])
    
    with tab1:
        st.subheader("Continental Distribution")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Pie chart
            fig_pie = px.pie(
                continent_df,
                values="votes",
                names="region",
                title="Market Share by Continent",
                color_discrete_sequence=px.colors.qualitative.Set2
            )
            fig_pie.update_traces(textposition="inside", textinfo="label+percent")
            fig_pie.update_layout(template="plotly", height=400)
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            # Bar chart
            continent_sorted = continent_df.sort_values("votes", ascending=True)
            fig_bar = px.bar(
                continent_sorted,
                x="votes",
                y="region",
                orientation="h",
                color="votes",
                color_continuous_scale="Blues",
                title="Total Votes by Continent"
            )
            fig_bar.update_layout(
                template="plotly",
                height=400,
                showlegend=False,
                xaxis_title="Total Votes",
                yaxis_title=""
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        
        # Statistics table
        st.subheader("Continental Statistics")
        continent_stats = continent_df.copy()
        continent_stats["percentage"] = (continent_stats["votes"] / continent_stats["votes"].sum() * 100).round(1)
        continent_stats = continent_stats.sort_values("votes", ascending=False)
        
        st.dataframe(
            continent_stats,
            use_container_width=True,
            column_config={
                "region": st.column_config.TextColumn("Continent", width="medium"),
                "votes": st.column_config.NumberColumn("Total Votes", format="%d"),
                "percentage": st.column_config.NumberColumn("Market Share (%)", format="%.1f%%")
            },
            hide_index=True
        )
    
    with tab2:
        st.subheader("Global Startup Heatmap")
        
        # Get region distribution
        region_data = startups_df.groupby("region").agg({
            "votes": "sum",
            "Startups Name": "count"
        }).reset_index()
        region_data.columns = ["region", "total_votes", "startup_count"]
        region_data = region_data[region_data["region"] != ""]
        
        fig_scatter = px.scatter(
            region_data,
            x="startup_count",
            y="total_votes",
            size="total_votes",
            color="total_votes",
            hover_name="region",
            color_continuous_scale="Viridis",
            title="Startups Count vs Total Votes by Region"
        )
        fig_scatter.update_layout(
            template="plotly",
            height=500,
            xaxis_title="Number of Startups",
            yaxis_title="Total Community Votes"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    with tab3:
        st.subheader("Regional Breakdown")
        
        # Select region
        regions = sorted(startups_df[startups_df["region"] != ""]["region"].unique())
        selected_region = st.selectbox("Select Region", regions)
        
        region_startups = get_startups_by_region(selected_region)
        
        if len(region_startups) > 0:
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Startups", len(region_startups))
            with col2:
                st.metric("Total Votes", int(region_startups["votes"].sum()))
            
            st.divider()
            
            # Top cities in region
            city_data = region_startups.groupby("city").agg({
                "votes": "sum",
                "Startups Name": "count"
            }).reset_index()
            city_data.columns = ["city", "total_votes", "count"]
            city_data = city_data.nlargest(15, "total_votes")
            
            fig_cities = px.bar(
                city_data,
                x="total_votes",
                y="city",
                orientation="h",
                color="count",
                color_continuous_scale="Teal",
                title=f"Top Cities in {selected_region}",
                hover_data={"count": True}
            )
            fig_cities.update_layout(
                template="plotly",
                height=400,
                xaxis_title="Total Votes",
                yaxis_title="City"
            )
            st.plotly_chart(fig_cities, use_container_width=True)
            
            # Top industries in region
            st.subheader(f"Top Industries in {selected_region}")
            industry_data = region_startups.groupby("industry").agg({
                "votes": "sum"
            }).reset_index()
            industry_data.columns = ["industry", "votes"]
            industry_data = industry_data[industry_data["industry"] != ""]
            industry_data = industry_data.nlargest(10, "votes")
            
            fig_industries = px.pie(
                industry_data,
                values="votes",
                names="industry",
                title=f"Industry Distribution in {selected_region}"
            )
            fig_industries.update_layout(template="plotly", height=400)
            st.plotly_chart(fig_industries, use_container_width=True)
    
    with tab4:
        st.subheader("City Comparison")
        
        # Select cities to compare
        cities_list = sorted(cities_df["city"].unique())
        selected_cities = st.multiselect(
            "Select cities to compare",
            options=cities_list,
            default=cities_list[:5]
        )
        
        if selected_cities:
            comparison_df = cities_df[cities_df["city"].isin(selected_cities)].sort_values("votes", ascending=False)
            
            fig_comparison = px.bar(
                comparison_df,
                x="city",
                y="votes",
                color="votes",
                color_continuous_scale="Plasma",
                title="City Comparison"
            )
            fig_comparison.update_layout(
                template="plotly",
                height=400,
                xaxis_title="City",
                yaxis_title="Total Votes",
                showlegend=False
            )
            st.plotly_chart(fig_comparison, use_container_width=True)
            
            # Detailed comparison table
            st.subheader("Detailed Comparison")
            st.dataframe(
                comparison_df,
                use_container_width=True,
                column_config={
                    "city": st.column_config.TextColumn("City", width="large"),
                    "votes": st.column_config.NumberColumn("Total Votes", format="%d")
                },
                hide_index=True
            )
