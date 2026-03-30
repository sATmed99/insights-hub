"""Global Startup Analytics Hub - Main Application"""
import streamlit as st
from app import pages

# Page configuration
st.set_page_config(
    page_title="Global Startup Analytics Hub",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom modern CSS
st.markdown("""
<style>
    :root {
        --main-bg: #f8f9fa;
        --main-text: #1a1a1a;
        --accent-purple: #667eea;
        --accent-pink: #764ba2;
    }
    
    .header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .stat-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 1rem 0;
    }
    
    .page-title {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🌍 Analytics Hub")
    st.markdown("---")
    
    # Logo / Branding
    st.markdown("""
    ### Global Startup Ecosystem Analytics
    Real-time insights into worldwide startup trends
    """)
    
    st.markdown("---")
    
    # Navigation
    st.subheader("📊 Navigation")
    page = st.radio(
        "Select Page",
        options=[
            "📈 Dashboard",
            "🌍 Geographic Analysis",
            "🏭 Industry Analytics",
            "🔍 Startup Search",
            "🔗 Domain Extensions",
            "🏙️ City Intelligence",
            "🗺️ Sector Map",
            "💎 Undervalued Cities",
            "🇩🇪 Germany Deep Dive",
            "🌎 Country Deep Dive",
            "📋 Methodology"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Info section
    st.markdown("""
    ### 📊 About This Hub
    
    This analytics platform provides:
    
    - **Real-time Data**: Startup votes & trends from global sources
    - **Geographic Insights**: City & regional analysis
    - **Industry Trends**: Market analysis by sector
    - **Company Discovery**: Search & filter startups
    - **Domain Analysis**: Extension performance metrics
    
    **Data Sources:**
    - Worldwide startup voting data
    - Industry classifications
    - Geographic distribution
    - Domain extension analysis
    """)
    
    st.markdown("---")
    
    st.markdown("""
    🔗 [Report Issue](https://github.com)
    
    **Last Updated**: March 2026
    """)

# Page routing
if page == "📈 Dashboard":
    pages.dashboard.show()
elif page == "🌍 Geographic Analysis":
    pages.geographic_analytics.show()
elif page == "🏭 Industry Analytics":
    pages.industry_analytics.show()
elif page == "🔍 Startup Search":
    pages.startup_search.show()
elif page == "🔗 Domain Extensions":
    pages.domain_analytics.show()
elif page == "🏙️ City Intelligence":
    pages.city_intelligence.show()
elif page == "🗺️ Sector Map":
    pages.sector_map.show()
elif page == "💎 Undervalued Cities":
    pages.undervalued_cities.show()
elif page == "🇩🇪 Germany Deep Dive":
    pages.germany_deep_dive.show()
elif page == "🌎 Country Deep Dive":
    pages.country_deep_dive.show()
elif page == "📋 Methodology":
    pages.methodology.show()

