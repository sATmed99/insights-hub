"""Startup search and company details page."""
import streamlit as st
import pandas as pd
import plotly.express as px
from app.real_data import (
    load_startups_data,
    search_startups,
)


def show():
    """Display the Startup Search page."""
    st.title("🔍 Startup Search & Discovery")
    
    st.markdown("""
    Search and discover startups in our global database with detailed information and metrics.
    """)
    
    # Search bar
    col1, col2 = st.columns([3, 1])
    
    with col1:
        search_query = st.text_input(
            "Search startups by name or industry",
            placeholder="e.g., AI, fintech, blockchain...",
            label_visibility="collapsed"
        )
    
    with col2:
        search_button = st.button("🔍 Search", use_container_width=True)
    
    # Get data
    all_startups = load_startups_data()
    
    if search_query and search_button:
        # Search
        results = search_startups(search_query)
        
        if len(results) > 0:
            st.success(f"Found **{len(results)}** startups")
            st.divider()
            
            # Display results
            for idx, startup in results.head(10).iterrows():
                with st.container(border=True):
                    col1, col2, col3 = st.columns([2, 1, 1])
                    
                    with col1:
                        st.markdown(f"### {startup['Startups Name']}")
                        if startup['description']:
                            st.markdown(f"_{startup['description'][:200]}..._")
                    
                    with col2:
                        st.metric("Votes", int(startup["votes"]))
                    
                    with col3:
                        st.metric("Ranking", int(startup["Ranking"]) if startup["Ranking"] > 0 else "N/A")
                    
                    col1, col2, col3, col4, col5 = st.columns(5)
                    
                    with col1:
                        st.caption(f"🌍 {startup['region']}")
                    with col2:
                        st.caption(f"🏭 {startup['industry']}")
                    with col3:
                        st.caption(f"🏙️ {startup['city']}")
                    with col4:
                        st.caption(f"🔗 {startup['Domain ending']}")
                    with col5:
                        st.caption(f"🔗 [Website]({startup['Startups URL']})" if startup['Startups URL'] else "No URL")
        else:
            st.warning("No startups found matching your search.")
    
    else:
        # Show trending startups
        st.subheader("🚀 Trending Startups (Top Voted)")
        
        trending = all_startups.nlargest(20, "votes")
        
        # Create columns for display
        col1, col2, col3 = st.columns([2, 1, 1])
        col1.markdown("**Startup Name**")
        col2.markdown("**Votes**")
        col3.markdown("**Ranking**")
        st.divider()
        
        for idx, startup in trending.iterrows():
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.markdown(f"[{startup['Startups Name']}]({startup['Startups URL']})")
            with col2:
                st.markdown(f"`{int(startup['votes'])} votes`")
            with col3:
                st.markdown(f"`Rank {int(startup['Ranking'])}`" if startup['Ranking'] > 0 else "`-`")
        
        st.divider()
        
        # Browse by category
        st.subheader("📂 Browse by Category")
        
        tab1, tab2, tab3, tab4 = st.tabs(["By Industry", "By Region", "By Domain", "Top Ranked"])
        
        with tab1:
            industries = sorted(all_startups[all_startups["industry"] != ""]["industry"].unique())
            selected_industry = st.selectbox("Select Industry", industries, key="ind_select")
            
            industry_startups = all_startups[all_startups["industry"] == selected_industry].nlargest(20, "votes")
            
            if len(industry_startups) > 0:
                st.write(f"**{len(industry_startups)} startups in {selected_industry}**")
                
                for idx, startup in industry_startups.iterrows():
                    col1, col2, col3 = st.columns([2, 1, 1])
                    
                    with col1:
                        st.markdown(f"[{startup['Startups Name']}]({startup['Startups URL']})")
                    with col2:
                        st.markdown(f"`{int(startup['votes'])} ⭐`")
                    with col3:
                        st.markdown(f"`{startup['city']}`")
        
        with tab2:
            regions = sorted(all_startups[all_startups["region"] != ""]["region"].unique())
            selected_region = st.selectbox("Select Region", regions, key="region_select")
            
            region_startups = all_startups[all_startups["region"] == selected_region].nlargest(20, "votes")
            
            if len(region_startups) > 0:
                st.write(f"**{len(region_startups)} startups in {selected_region}**")
                
                for idx, startup in region_startups.iterrows():
                    col1, col2, col3 = st.columns([2, 1, 1])
                    
                    with col1:
                        st.markdown(f"[{startup['Startups Name']}]({startup['Startups URL']})")
                    with col2:
                        st.markdown(f"`{int(startup['votes'])} ⭐`")
                    with col3:
                        st.markdown(f"`{startup['industry']}`")
        
        with tab3:
            domains = sorted(all_startups[all_startups["Domain ending"] != ""]["Domain ending"].unique())
            selected_domain = st.selectbox("Select Domain", domains, key="domain_select")
            
            domain_startups = all_startups[all_startups["Domain ending"] == selected_domain].nlargest(20, "votes")
            
            if len(domain_startups) > 0:
                st.write(f"**{len(domain_startups)} startups with .{selected_domain}**")
                
                for idx, startup in domain_startups.iterrows():
                    col1, col2, col3 = st.columns([2, 1, 1])
                    
                    with col1:
                        st.markdown(f"[{startup['Startups Name']}]({startup['Startups URL']})")
                    with col2:
                        st.markdown(f"`{int(startup['votes'])} ⭐`")
                    with col3:
                        st.markdown(f"`{startup['region']}`")
        
        with tab4:
            ranked = all_startups[all_startups["Ranking"] > 0].nsmallest(20, "Ranking")
            
            if len(ranked) > 0:
                st.write("**Top Ranked Startups**")
                
                for idx, startup in ranked.iterrows():
                    col1, col2, col3 = st.columns([2, 1, 1])
                    
                    with col1:
                        st.markdown(f"[{startup['Startups Name']}]({startup['Startups URL']})")
                    with col2:
                        st.markdown(f"`Rank #{int(startup['Ranking'])}`")
                    with col3:
                        st.markdown(f"`{int(startup['votes'])} votes`")
