"""Dashboard page - Main analytics overview."""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app.real_data import (
    get_startup_stats,
    get_continent_distribution,
    get_top_cities,
    get_top_industries,
    get_trending_startups,
    load_startups_data,
)


def show():
    """Display the Dashboard page."""
    # Header
    st.markdown("""
    <style>
        .header-title {
            font-size: 3em;
            font-weight: bold;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5em;
        }
        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5em;
            border-radius: 10px;
            text-align: center;
        }
        .stat-label {
            font-size: 0.9em;
            opacity: 0.9;
            margin-bottom: 0.3em;
        }
        .stat-value {
            font-size: 2.5em;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='header-title'>🌍 Global Startup Analytics Hub</div>", unsafe_allow_html=True)
    st.markdown("Real-time insights into the worldwide startup ecosystem", unsafe_allow_html=True)
    
    # Get statistics
    stats = get_startup_stats()
    
    # KPI Cards
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            "📊 Total Startups",
            f"{stats['total_startups']:,}",
            "Tracked globally"
        )
    
    with col2:
        st.metric(
            "⭐ Total Votes",
            f"{stats['total_votes']:,}",
            "Community engagement"
        )
    
    with col3:
        st.metric(
            "📈 Avg Votes",
            f"{stats['avg_votes']:.0f}",
            "Per startup"
        )
    
    with col4:
        st.metric(
            "🏭 Industries",
            f"{stats['total_industries']:,}",
            "Tracked"
        )
    
    with col5:
        st.metric(
            "🌐 Regions",
            f"{stats['total_regions']:,}",
            "Covered"
        )
    
    st.divider()
    
    # Main visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🌍 Global Distribution by Continent")
        continent_df = get_continent_distribution()
        
        fig_continent = px.pie(
            continent_df,
            values="votes",
            names="region",
            color_discrete_sequence=px.colors.qualitative.Set2,
            title="Startup Votes by Continent"
        )
        fig_continent.update_traces(
            textposition="inside",
            textinfo="label+percent"
        )
        fig_continent.update_layout(
            template="plotly",
            showlegend=True,
            height=400
        )
        st.plotly_chart(fig_continent, use_container_width=True)
    
    with col2:
        st.subheader("🏆 Top 15 Industries")
        industries_df = get_top_industries(15)
        
        fig_industries = px.bar(
            industries_df,
            x="votes",
            y="industry",
            orientation="h",
            color="votes",
            color_continuous_scale="Viridis",
            title="Most Voted Industries"
        )
        fig_industries.update_layout(
            template="plotly",
            height=400,
            yaxis_title="Industry",
            xaxis_title="Total Votes",
            showlegend=False
        )
        st.plotly_chart(fig_industries, use_container_width=True)
    
    st.divider()
    
    # Geographic Analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏙️ Top 20 Cities")
        cities_df = get_top_cities(20)
        cities_df["votes"] = pd.to_numeric(cities_df["votes"], errors="coerce").fillna(0)
        
        fig_cities = px.bar(
            cities_df,
            x="votes",
            y="city",
            orientation="h",
            color="votes",
            color_continuous_scale="Blues",
            title="Startup Hubs by Votes"
        )
        fig_cities.update_layout(
            template="plotly",
            height=500,
            yaxis_title="City",
            xaxis_title="Total Votes",
            showlegend=False
        )
        st.plotly_chart(fig_cities, use_container_width=True)
    
    with col1:
        st.subheader("🚀 Trending Startups")
        trending_df = get_trending_startups(15)
        
        fig_trending = px.bar(
            trending_df,
            x="votes",
            y="Startups Name",
            orientation="h",
            color="votes",
            color_continuous_scale="Reds",
            title="Top Voted Startups"
        )
        fig_trending.update_layout(
            template="plotly",
            height=500,
            yaxis_title="Startup",
            xaxis_title="Votes",
            showlegend=False
        )
        st.plotly_chart(fig_trending, use_container_width=True)
    
    with col2:
        st.subheader("📊 Industry Deep Dive")
        
        startups_df = load_startups_data()
        industry_summary = startups_df.groupby("industry").agg({
            "votes": "sum",
            "Startups Name": "count"
        }).reset_index()
        industry_summary.columns = ["industry", "total_votes", "count"]
        industry_summary = industry_summary[industry_summary["industry"] != ""]
        industry_summary = industry_summary.nlargest(15, "total_votes")
        
        fig_industry_scatter = px.scatter(
            industry_summary,
            x="count",
            y="total_votes",
            size="total_votes",
            color="total_votes",
            hover_name="industry",
            color_continuous_scale="Rainbow",
            title="Industries: Count vs Total Votes"
        )
        fig_industry_scatter.update_layout(
            template="plotly",
            height=500,
            xaxis_title="Number of Startups",
            yaxis_title="Total Votes"
        )
        st.plotly_chart(fig_industry_scatter, use_container_width=True)
    
    st.divider()
    
    # Key Insights
    st.subheader("💡 Key Insights")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        top_city = cities_df.iloc[0]
        st.info(f"""
        **🏆 Leading Startup Hub**
        {top_city['city']} leads globally with **{int(top_city['votes']):,}** votes
        """)
    
    with col2:
        top_industry = industries_df.iloc[0]
        st.info(f"""
        **📈 Dominant Industry**
        {top_industry['industry']} has **{int(top_industry['votes']):,}** votes
        """)
    
    with col3:
        top_continent = continent_df.iloc[0]
        st.info(f"""
        **🌍 Leading Continent**
        {top_continent['region'].title()} accounts for **{top_continent['votes']:,}** votes
        """)
