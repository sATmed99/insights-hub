"""Utility functions for data processing and analysis."""
import pandas as pd
from app.data import MOCK_CITIES, get_cities_dataframe

def filter_cities(regions=None, sectors=None, statuses=None):
    """Filter cities by regions, sectors, and statuses."""
    df = get_cities_dataframe()
    
    if regions and "All EU" not in regions:
        df = df[df["region"].isin(regions)]
    
    if statuses:
        df = df[df["status"].isin(statuses)]
    
    # Filter by sectors if provided
    if sectors:
        mask = df["sectors"].apply(
            lambda x: any(sector in x for sector in sectors)
        )
        df = df[mask]
    
    return df

def get_city_by_id(city_id):
    """Get a single city by ID."""
    for city in MOCK_CITIES:
        if city["id"] == city_id:
            return city
    return None

def get_germany_cities():
    """Get all cities in Germany."""
    return pd.DataFrame([c for c in MOCK_CITIES if c["countryCode"] == "DE"])

def get_sector_stats(df=None):
    """Get statistics for each sector."""
    if df is None:
        df = get_cities_dataframe()
    
    sector_stats = {}
    for sector in ["Fintech", "Edtech", "Healthtech", "SaaS", "Deeptech"]:
        total = df["sectors"].apply(lambda x: x.get(sector, 0)).sum()
        sector_stats[sector] = total
    
    return pd.DataFrame(list(sector_stats.items()), columns=["Sector", "Total Startups"])

def get_region_stats(df=None):
    """Get statistics for each region."""
    if df is None:
        df = get_cities_dataframe()
    
    region_stats = df.groupby("region").agg({
        "name": "count",
        "votes": "sum",
        "attractivenessIndex": "mean",
        "funding": "sum"
    }).reset_index()
    
    region_stats.columns = ["Region", "Cities", "Total Votes", "Avg Attractiveness", "Total Funding"]
    return region_stats.sort_values("Total Votes", ascending=False)

def get_status_stats(df=None):
    """Get statistics by city status."""
    if df is None:
        df = get_cities_dataframe()
    
    return df["status"].value_counts().reset_index()

def get_top_cities(df=None, n=10):
    """Get top cities by attractiveness index."""
    if df is None:
        df = get_cities_dataframe()
    
    return df.nlargest(n, "attractivenessIndex")[
        ["name", "country", "region", "attractivenessIndex", "votes", "funding"]
    ]

def get_undervalued_cities(df=None):
    """Get undervalued cities (high potential, lower votes)."""
    if df is None:
        df = get_cities_dataframe()
    
    # Filter for cities with "undervalued" or "hidden gem" status
    undervalued = df[df["status"].isin(["undervalued", "hidden gem", "rising"])]
    return undervalued[undervalued["attractivenessIndex"] >= 65].sort_values(
        "attractivenessIndex", ascending=False
    )

def get_dashboard_stats(df=None):
    """Get overall dashboard statistics."""
    if df is None:
        df = get_cities_dataframe()
    
    return {
        "total_cities": len(df),
        "total_votes": int(df["votes"].sum()),
        "avg_attractiveness": float(df["attractivenessIndex"].mean()),
        "total_funding": float(df["funding"].sum()),
        "established_cities": len(df[df["status"] == "established"]),
        "rising_cities": len(df[df["status"] == "rising"]),
    }
