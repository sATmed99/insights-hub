"""Insights Hub - Main Application"""
import streamlit as st
import pandas as pd
from app import pages
from app.data import get_regions, get_sectors, get_statuses

# Page configuration
st.set_page_config(
    page_title="Insights Hub",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for dark theme
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background-color: #1a1a1a;
    }
    
    .stApp {
        background-color: #050505;
        color: #e4e4e7;
    }
    
    .metric-card {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "selected_regions" not in st.session_state:
    st.session_state.selected_regions = ["All EU"]

if "selected_sectors" not in st.session_state:
    st.session_state.selected_sectors = ["Fintech", "SaaS", "Healthtech", "Edtech"]

if "selected_statuses" not in st.session_state:
    st.session_state.selected_statuses = get_statuses()

# Sidebar navigation
with st.sidebar:
    st.title("� Insights Hub")
    st.markdown("---")
    
    # Navigation
    st.subheader("Navigation")
    page = st.radio(
        "Select Page",
        options=[
            "City Intelligence",
            "Sector Map",
            "Undervalued Cities",
            "Germany Deep Dive",
            "Country Deep Dive",
            "Methodology"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Filters
    st.subheader("Filters")
    
    # Region filter
    st.markdown("**Regions**")
    regions = get_regions()
    selected_regions = st.multiselect(
        "Select Regions",
        options=regions,
        default=st.session_state.selected_regions,
        label_visibility="collapsed"
    )
    st.session_state.selected_regions = selected_regions or ["All EU"]
    
    # Sector filter
    st.markdown("**Sectors**")
    sectors = get_sectors()
    selected_sectors = st.multiselect(
        "Select Sectors",
        options=sectors,
        default=st.session_state.selected_sectors,
        label_visibility="collapsed"
    )
    st.session_state.selected_sectors = selected_sectors or sectors
    
    # Status filter (for future use)
    st.markdown("**City Status**")
    statuses = get_statuses()
    selected_statuses = st.multiselect(
        "Select Status",
        options=statuses,
        default=st.session_state.selected_statuses,
        label_visibility="collapsed"
    )
    st.session_state.selected_statuses = selected_statuses or statuses
    
    st.markdown("---")
    
    # About section
    st.markdown("""
    ### About
    Insights Hub is a business analytics platform for exploring market ecosystems.
    
    **Latest Update**: March 2025
    """)

# Main content
if page == "City Intelligence":
    pages.city_intelligence.show()
elif page == "Sector Map":
    pages.sector_map.show()
elif page == "Undervalued Cities":
    pages.undervalued_cities.show()
elif page == "Germany Deep Dive":
    pages.germany_deep_dive.show()
elif page == "Country Deep Dive":
    pages.country_deep_dive.show()
elif page == "Methodology":
    pages.methodology.show()
