"""Methodology page."""
import streamlit as st

def show():
    """Display the Methodology page."""
    st.title("📊 Methodology")
    
    st.markdown("""
    ## EuroStartup Radar: Analysis Methodology
    
    ### Overview
    The EuroStartup Radar provides a comprehensive analysis of the European startup ecosystem, 
    identifying growth regions, emerging opportunities, and sector distribution across the continent.
    
    ### Data Sources
    
    - **City Selection**: 21 major European startup hubs across different regions
    - **Regions Covered**: 
      - Western Europe (UK, France, Netherlands, Spain, Portugal)
      - DACH (Germany, Austria, Switzerland)
      - Nordics (Sweden, Finland, Estonia)
      - CEE (Poland, Czech Republic)
    
    ### Key Metrics
    
    #### 1. **Attractiveness Index (0-100)**
    A composite score measuring a city's viability as a startup hub, based on:
    - Availability of talent and skilled workforce
    - Access to funding and venture capital
    - Quality of infrastructure and facilities
    - Government support and regulatory environment
    - Networking opportunities and community support
    
    #### 2. **Community Votes**
    Reflects the collective interest and recognition from the startup community.
    Higher votes indicate stronger ecosystem presence and visibility.
    
    #### 3. **Funding (€ Millions)**
    Approximate total venture capital and founder funding in the city's ecosystem.
    
    ### City Status Classification
    
    - **Established**: Mature startup hubs with sustained activity and proven track record
      - Examples: London, Berlin, Paris, Stockholm
      - Characteristics: High votes, high attractiveness index
    
    - **Rising**: Emerging hubs showing strong growth trajectory
      - Examples: Warsaw, Tallinn, Helsinki
      - Characteristics: Increasing votes, solid attractiveness index
    
    - **Hidden Gem**: Cities with high potential but lower market attention
      - Examples: Lisbon, Krakow
      - Characteristics: Moderate to high attractiveness, lower comparative votes
    
    - **Undervalued**: Cities with untapped potential for entrepreneurs
      - Characteristics: Growing ecosystem, attractive for new ventures
    
    ### Sector Classification
    
    Five major tech sectors are tracked:
    
    - **Fintech**: Financial technology and blockchain startups
    - **Edtech**: Education technology platforms
    - **Healthtech**: Healthcare and biotech innovation
    - **SaaS**: Software-as-a-Service businesses
    - **Deeptech**: Deep technology and hard tech ventures
    
    ### Analysis Methodology
    
    #### City Intelligence
    Provides an overview of all tracked cities with comparative metrics.
    Useful for general ecosystem research and regional comparisons.
    
    #### Sector Map
    Shows sector distribution across regions and cities.
    Helps identify sector specialization in different hubs.
    
    #### Undervalued Cities
    Identifies hidden opportunities where entrepreneurs and investors might find:
    - Better valuations
    - Less competition
    - High growth potential
    
    #### Country Deep Dive
    Detailed analysis of individual countries' startup ecosystems.
    
    #### Germany Deep Dive
    Special focus on Germany as Europe's largest startup ecosystem.
    
    ### Limitations & Disclaimers
    
    - Data is based on historical information and community votes as of 2024/2025
    - Market conditions and rankings are subject to change
    - Analysis should not be the sole basis for investment decisions
    - Actual business conditions may vary from metrics shown
    
    ### Updates & Feedback
    
    This analysis is regularly updated with new data and community feedback.
    For corrections or additional information, please submit feedback.
    
    ---
    
    **Last Updated**: March 2025
    """)
    
    st.divider()
    
    st.subheader("Data Quality")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Cities Analyzed", 21, "🏙️")
    
    with col2:
        st.metric("Regions Covered", 5, "🌍")
    
    with col3:
        st.metric("Sectors Tracked", 5, "📈")
