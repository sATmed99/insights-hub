"""Industry analytics page."""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app.real_data import (
    get_top_industries,
    get_industry_growth,
    load_startups_data,
    get_startups_by_industry,
)


def show():
    """Display the Industry Analytics page."""
    st.title("🏭 Industry Analytics")
    
    st.markdown("""
    Deep dive into startup industries: market trends, competition, and opportunities.
    """)
    
    # Get data
    startups_df = load_startups_data()
    industry_growth = get_industry_growth()
    
    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Industry Overview", "Market Trends", "Industry Spotlight", "Competitive Analysis"])
    
    with tab1:
        st.subheader("Industry Overview")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                "Total Industries",
                len(industry_growth)
            )
        
        with col2:
            st.metric(
                "Avg Startups per Industry",
                f"{industry_growth['count'].mean():.0f}"
            )
        
        st.divider()
        
        # Top industries bar chart
        top_industries = get_top_industries(20)
        fig_bar = px.bar(
            top_industries,
            x="votes",
            y="industry",
            orientation="h",
            color="votes",
            color_continuous_scale="Viridis",
            title="Top 20 Industries by Total Votes"
        )
        fig_bar.update_layout(
            template="plotly",
            height=500,
            yaxis_title="Industry",
            xaxis_title="Total Votes",
            showlegend=False
        )
        st.plotly_chart(fig_bar, use_container_width=True)
        
        # Industries table
        st.subheader("Industry Statistics")
        industry_table = industry_growth.head(30).copy()
        industry_table["market_share_%"] = (industry_table["total_votes"] / industry_table["total_votes"].sum() * 100).round(1)
        
        st.dataframe(
            industry_table,
            use_container_width=True,
            column_config={
                "industry": st.column_config.TextColumn("Industry", width="large"),
                "total_votes": st.column_config.NumberColumn("Total Votes", format="%d"),
                "count": st.column_config.NumberColumn("Startups", format="%d"),
                "avg_votes": st.column_config.NumberColumn("Avg Votes", format="%.1f"),
                "avg_ranking": st.column_config.NumberColumn("Avg Ranking", format="%.0f"),
                "market_share_%": st.column_config.NumberColumn("Market Share (%)", format="%.1f%%")
            },
            hide_index=True
        )
    
    with tab2:
        st.subheader("Market Trends")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Industry Growth (by Startup Count)")
            top_by_count = industry_growth.nlargest(15, "count")
            fig_count = px.bar(
                top_by_count,
                x="count",
                y="industry",
                orientation="h",
                color="count",
                color_continuous_scale="Blues",
                title="Industries with Most Startups"
            )
            fig_count.update_layout(
                template="plotly",
                height=400,
                showlegend=False,
                xaxis_title="Number of Startups",
                yaxis_title=""
            )
            st.plotly_chart(fig_count, use_container_width=True)
        
        with col2:
            st.subheader("Average Engagement (Avg Votes)")
            top_by_avg = industry_growth.nlargest(15, "avg_votes")
            fig_avg = px.bar(
                top_by_avg,
                x="avg_votes",
                y="industry",
                orientation="h",
                color="avg_votes",
                color_continuous_scale="Reds",
                title="Industries with Highest Avg Votes"
            )
            fig_avg.update_layout(
                template="plotly",
                height=400,
                showlegend=False,
                xaxis_title="Average Votes per Startup",
                yaxis_title=""
            )
            st.plotly_chart(fig_avg, use_container_width=True)
        
        st.divider()
        
        # Scatter plot: Market Saturation
        fig_scatter = px.scatter(
            industry_growth,
            x="count",
            y="avg_votes",
            size="total_votes",
            color="total_votes",
            hover_name="industry",
            color_continuous_scale="Rainbow",
            title="Market Saturation vs Engagement (bubble size = total votes)"
        )
        fig_scatter.update_layout(
            template="plotly",
            height=500,
            xaxis_title="Number of Startups (Saturation)",
            yaxis_title="Average Votes (Engagement)"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    with tab3:
        st.subheader("Industry Spotlight")
        
        # Select industry
        industries = sorted(industry_growth["industry"].unique())
        selected_industry = st.selectbox("Select Industry", industries)
        
        industry_startups = get_startups_by_industry(selected_industry)
        
        if len(industry_startups) > 0:
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Startups", len(industry_startups))
            with col2:
                st.metric("Total Votes", int(industry_startups["votes"].sum()))
            with col3:
                st.metric("Avg Votes", f"{industry_startups['votes'].mean():.0f}")
            with col4:
                st.metric("Avg Ranking", f"{industry_startups['Ranking'].mean():.0f}")
            
            st.divider()
            
            # Distribution by region
            col1, col2 = st.columns(2)
            
            with col1:
                region_dist = industry_startups.groupby("region").agg({
                    "votes": "sum",
                    "Startups Name": "count"
                }).reset_index()
                region_dist.columns = ["region", "votes", "count"]
                region_dist = region_dist[region_dist["region"] != ""]
                
                fig_region = px.pie(
                    region_dist,
                    values="votes",
                    names="region",
                    title=f"{selected_industry} - Geographic Distribution"
                )
                fig_region.update_layout(template="plotly", height=400)
                st.plotly_chart(fig_region, use_container_width=True)
            
            with col2:
                domain_dist = industry_startups.groupby("Domain ending").agg({
                    "votes": "sum"
                }).reset_index().nlargest(10, "votes")
                
                fig_domain = px.bar(
                    domain_dist,
                    x="votes",
                    y="Domain ending",
                    orientation="h",
                    color="votes",
                    color_continuous_scale="Blues",
                    title=f"{selected_industry} - Top Domain Extensions"
                )
                fig_domain.update_layout(
                    template="plotly",
                    height=400,
                    showlegend=False
                )
                st.plotly_chart(fig_domain, use_container_width=True)
            
            # Top startups in industry
            st.subheader(f"Top Startups in {selected_industry}")
            top_startups = industry_startups.nlargest(10, "votes")[[
                "Startups Name", "region", "city", "votes", "Ranking", "Domain ending"
            ]]
            
            st.dataframe(
                top_startups,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Startups Name": st.column_config.TextColumn("Startup", width="large"),
                    "region": st.column_config.TextColumn("Region", width="medium"),
                    "city": st.column_config.TextColumn("City", width="large"),
                    "votes": st.column_config.NumberColumn("Votes", format="%d"),
                    "Ranking": st.column_config.NumberColumn("Ranking", format="%.0f"),
                    "Domain ending": st.column_config.TextColumn("Domain", width="small")
                }
            )
    
    with tab4:
        st.subheader("Competitive Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            industry1 = st.selectbox("Compare Industry", industries, key="ind1")
        
        with col2:
            industry2 = st.selectbox("With Industry", industries, key="ind2", index=1 if len(industries) > 1 else 0)
        
        if industry1 and industry2:
            ind1_data = get_startups_by_industry(industry1)
            ind2_data = get_startups_by_industry(industry2)
            
            comparison_data = pd.DataFrame({
                "Metric": ["Startups", "Total Votes", "Avg Votes", "Avg Ranking"],
                industry1: [
                    len(ind1_data),
                    int(ind1_data["votes"].sum()),
                    f"{ind1_data['votes'].mean():.0f}",
                    f"{ind1_data['Ranking'].mean():.0f}"
                ],
                industry2: [
                    len(ind2_data),
                    int(ind2_data["votes"].sum()),
                    f"{ind2_data['votes'].mean():.0f}",
                    f"{ind2_data['Ranking'].mean():.0f}"
                ]
            })
            
            st.subheader("Comparative Metrics")
            st.dataframe(comparison_data, use_container_width=True, hide_index=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader(f"{industry1}")
                st.write(f"**Startups:** {len(ind1_data)}")
                st.write(f"**Votes:** {int(ind1_data['votes'].sum()):,}")
                st.write(f"**Market Share:** {(ind1_data['votes'].sum() / (ind1_data['votes'].sum() + ind2_data['votes'].sum()) * 100):.1f}%")
            
            with col2:
                st.subheader(f"{industry2}")
                st.write(f"**Startups:** {len(ind2_data)}")
                st.write(f"**Votes:** {int(ind2_data['votes'].sum()):,}")
                st.write(f"**Market Share:** {(ind2_data['votes'].sum() / (ind1_data['votes'].sum() + ind2_data['votes'].sum()) * 100):.1f}%")
