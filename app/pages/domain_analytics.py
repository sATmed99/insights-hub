"""Domain extension analytics page."""
import streamlit as st
import pandas as pd
import plotly.express as px
from app.real_data import (
    get_domain_distribution,
    get_domain_performance,
    load_startups_data,
    get_startups_by_domain,
)


def show():
    """Display the Domain Extension Analytics page."""
    st.title("🔗 Domain Extension Analytics")
    
    st.markdown("""
    Analyze domain extension trends and their impact on startup success and branding.
    """)
    
    # Get data
    domain_dist = get_domain_distribution()
    domain_perf = get_domain_performance()
    all_startups = load_startups_data()
    
    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Market Share", "Performance Metrics", "Domain Comparison", "Insights"])
    
    with tab1:
        st.subheader("Market Share by Domain Extension")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Pie chart
            fig_pie = px.pie(
                domain_dist,
                values="votes",
                names="domain_ending",
                title="Market Share by Domain Extension",
                color_discrete_sequence=px.colors.qualitative.Set2
            )
            fig_pie.update_traces(textposition="auto", textinfo="label+percent")
            fig_pie.update_layout(template="plotly", height=400)
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            # Sunburst chart would be nice, but bar chart works too
            domain_dist_sorted = domain_dist.sort_values("votes", ascending=True).tail(15)
            fig_bar = px.bar(
                domain_dist_sorted,
                x="votes",
                y="domain_ending",
                orientation="h",
                color="votes",
                color_continuous_scale="Blues",
                title="Top 15 Domain Extensions"
            )
            fig_bar.update_layout(
                template="plotly",
                height=400,
                showlegend=False,
                xaxis_title="Total Votes",
                yaxis_title="Domain"
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        
        # Statistics table
        st.subheader("Domain Extension Statistics")
        domain_table = domain_dist.copy()
        domain_table["percentage"] = (domain_table["votes"] / domain_table["votes"].sum() * 100).round(1)
        
        st.dataframe(
            domain_table,
            use_container_width=True,
            column_config={
                "domain_ending": st.column_config.TextColumn("Domain", width="small"),
                "votes": st.column_config.NumberColumn("Total Votes", format="%d"),
                "percentage": st.column_config.NumberColumn("Market Share (%)", format="%.1f%%")
            },
            hide_index=True
        )
    
    with tab2:
        st.subheader("Performance Metrics by Domain")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Average votes per domain
            fig_avg = px.bar(
                domain_perf.nlargest(15, "avg_votes"),
                x="avg_votes",
                y="domain",
                orientation="h",
                color="avg_votes",
                color_continuous_scale="Reds",
                title="Average Votes by Domain Extension"
            )
            fig_avg.update_layout(
                template="plotly",
                height=400,
                showlegend=False,
                xaxis_title="Average Votes",
                yaxis_title=""
            )
            st.plotly_chart(fig_avg, use_container_width=True)
        
        with col2:
            # Startup count by domain
            fig_count = px.bar(
                domain_perf.nlargest(15, "count"),
                x="count",
                y="domain",
                orientation="h",
                color="count",
                color_continuous_scale="Greens",
                title="Number of Startups by Domain"
            )
            fig_count.update_layout(
                template="plotly",
                height=400,
                showlegend=False,
                xaxis_title="Startup Count",
                yaxis_title=""
            )
            st.plotly_chart(fig_count, use_container_width=True)
        
        # Detailed performance table
        st.subheader("Detailed Performance Analysis")
        perf_table = domain_perf.copy().sort_values("total_votes", ascending=False)
        
        st.dataframe(
            perf_table.head(20),
            use_container_width=True,
            column_config={
                "domain": st.column_config.TextColumn("Domain", width="small"),
                "total_votes": st.column_config.NumberColumn("Total Votes", format="%d"),
                "count": st.column_config.NumberColumn("Startups", format="%d"),
                "avg_votes": st.column_config.NumberColumn("Avg Votes", format="%.1f"),
                "avg_ranking": st.column_config.NumberColumn("Avg Ranking", format="%.0f")
            },
            hide_index=True
        )
    
    with tab3:
        st.subheader("Domain Comparison")
        
        # Select domains to compare
        top_domains = domain_dist.nlargest(20, "votes")["domain_ending"].unique()
        
        col1, col2 = st.columns(2)
        
        with col1:
            domain1 = st.selectbox("Domain 1", top_domains, index=0)
        
        with col2:
            domain2 = st.selectbox("Domain 2", top_domains, index=1 if len(top_domains) > 1 else 0)
        
        if domain1 and domain2:
            dom1_startups = get_startups_by_domain(domain1)
            dom2_startups = get_startups_by_domain(domain2)
            
            # Comparison metrics
            comparison = pd.DataFrame({
                "Metric": ["Startups", "Total Votes", "Avg Votes", "Avg Ranking", "Top City"],
                f".{domain1}": [
                    len(dom1_startups),
                    int(dom1_startups["votes"].sum()),
                    f"{dom1_startups['votes'].mean():.0f}",
                    f"{dom1_startups['Ranking'].mean():.0f}",
                    dom1_startups["city"].value_counts().index[0] if len(dom1_startups) > 0 else "N/A"
                ],
                f".{domain2}": [
                    len(dom2_startups),
                    int(dom2_startups["votes"].sum()),
                    f"{dom2_startups['votes'].mean():.0f}",
                    f"{dom2_startups['Ranking'].mean():.0f}",
                    dom2_startups["city"].value_counts().index[0] if len(dom2_startups) > 0 else "N/A"
                ]
            })
            
            st.subheader("Comparative Analysis")
            st.dataframe(comparison, use_container_width=True, hide_index=True)
            
            # Visual comparison
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"### .{domain1}")
                st.write(f"**Startups:** {len(dom1_startups)}")
                st.write(f"**Market Share:** {(dom1_startups['votes'].sum() / (dom1_startups['votes'].sum() + dom2_startups['votes'].sum()) * 100):.1f}%")
                
                # Top industries
                if len(dom1_startups) > 0:
                    st.markdown("**Top Industries:**")
                    top_ind = dom1_startups["industry"].value_counts().head(5)
                    for ind, count in top_ind.items():
                        st.write(f"• {ind}: {int(count)}")
            
            with col2:
                st.markdown(f"### .{domain2}")
                st.write(f"**Startups:** {len(dom2_startups)}")
                st.write(f"**Market Share:** {(dom2_startups['votes'].sum() / (dom1_startups['votes'].sum() + dom2_startups['votes'].sum()) * 100):.1f}%")
                
                # Top industries
                if len(dom2_startups) > 0:
                    st.markdown("**Top Industries:**")
                    top_ind = dom2_startups["industry"].value_counts().head(5)
                    for ind, count in top_ind.items():
                        st.write(f"• {ind}: {int(count)}")
    
    with tab4:
        st.subheader("💡 Key Insights & Trends")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            top_domain = domain_dist.iloc[0]
            st.success(f"""
            **🏆 Dominant Domain**
            
            **.{top_domain['domain_ending']}** leads with **{int(top_domain['votes']):,}** votes
            
            Market share: **{(top_domain['votes'] / domain_dist['votes'].sum() * 100):.1f}%**
            """)
        
        with col2:
            avg_votes_com = domain_perf[domain_perf['domain'] == 'com']['avg_votes'].values
            if len(avg_votes_com) > 0:
                st.info(f"""
                **📊 .COM Performance**
                
                Average: **{avg_votes_com[0]:.0f}** votes
                
                Still the most trusted extension
                """)
        
        with col3:
            # Find emerging domain
            emerging = domain_perf[domain_perf['count'] > 10].nlargest(1, 'avg_votes')
            if len(emerging) > 0:
                st.warning(f"""
                **🚀 Emerging Domain**
                
                **.{emerging['domain'].values[0]}** shows strong potential
                
                Avg: **{emerging['avg_votes'].values[0]:.0f}** votes
                """)
        
        st.divider()
        
        # Insights section
        st.markdown("### Market Observations")
        
        insights = []
        
        # Calculate statistics
        com_share = domain_dist[domain_dist['domain_ending'] == 'com']['votes'].sum() / domain_dist['votes'].sum() * 100
        io_share = domain_dist[domain_dist['domain_ending'] == 'io']['votes'].sum() / domain_dist['votes'].sum() * 100 if 'io' in domain_dist['domain_ending'].values else 0
        
        insights.append(f"• **.COM** accounts for **{com_share:.1f}%** of all votes - it remains the most popular choice for startups")
        if io_share > 0:
            insights.append(f"• **.IO** captures **{io_share:.1f}%** of the market - popular for tech startups")
        
        top_3 = domain_perf.nlargest(3, 'avg_votes')
        insights.append(f"• Top performing extensions by average engagement: {', '.join([f'.{d}' for d in top_3['domain'].values])}")
        
        for insight in insights:
            st.write(insight)
