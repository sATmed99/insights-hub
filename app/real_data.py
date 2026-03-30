"""Real data loading and processing from CSV files."""
import pandas as pd
import streamlit as st
from pathlib import Path
import numpy as np

# Get the data directory
DATA_DIR = Path(__file__).parent.parent / "data"


@st.cache_data
def load_cities_data():
    """Load city votes data."""
    try:
        df = pd.read_csv(DATA_DIR / "votes-by-city.csv")
        df.columns = ["city", "votes"]
        return df
    except Exception as e:
        print(f"Error loading cities data: {e}")
        return pd.DataFrame()


@st.cache_data
def load_continent_data():
    """Load continent votes data."""
    try:
        df = pd.read_csv(DATA_DIR / "votes-by-continent.csv")
        df.columns = ["region", "votes"]
        return df
    except Exception as e:
        print(f"Error loading continent data: {e}")
        return pd.DataFrame()


@st.cache_data
def load_industry_data():
    """Load industry votes data."""
    try:
        df = pd.read_csv(DATA_DIR / "votes-by-industry.csv")
        df.columns = ["industry", "votes", "avg_ranking"]
        return df
    except Exception as e:
        print(f"Error loading industry data: {e}")
        return pd.DataFrame()


@st.cache_data
def load_domain_data():
    """Load domain extension votes data."""
    try:
        df = pd.read_csv(DATA_DIR / "votes-by-domain endings.csv")
        df.columns = ["domain_ending", "votes"]
        return df
    except Exception as e:
        print(f"Error loading domain data: {e}")
        return pd.DataFrame()


@st.cache_data
def load_startups_data():
    """Load worldwide trending startups data."""
    try:
        df = pd.read_csv(DATA_DIR / "worldwide-trending-startups-votes.csv")
        # Clean up data
        df = df.fillna("")
        df["votes"] = pd.to_numeric(df["votes"], errors="coerce").fillna(0)
        df["Ranking"] = pd.to_numeric(df["Ranking"], errors="coerce").fillna(0)
        return df
    except Exception as e:
        print(f"Error loading startups data: {e}")
        return pd.DataFrame()


def get_top_cities(n=20):
    """Get top N cities by votes."""
    df = load_cities_data()
    df["votes"] = pd.to_numeric(df["votes"], errors="coerce").fillna(0)
    return df.nlargest(n, "votes")


def get_top_industries(n=20):
    """Get top N industries by votes."""
    df = load_industry_data()
    df["votes"] = pd.to_numeric(df["votes"], errors="coerce").fillna(0)
    return df[df["industry"] != "None assigned"].nlargest(n, "votes")


def get_continent_distribution():
    """Get continent distribution."""
    df = load_continent_data()
    df["votes"] = pd.to_numeric(df["votes"], errors="coerce").fillna(0)
    return df[df["region"] != "misc"].sort_values("votes", ascending=False)


def get_domain_distribution(n=15):
    """Get top N domain extensions by votes."""
    df = load_domain_data()
    df["votes"] = pd.to_numeric(df["votes"], errors="coerce").fillna(0)
    return df.nlargest(n, "votes")


def get_startup_stats():
    """Get overall startup statistics."""
    df = load_startups_data()
    return {
        "total_startups": len(df),
        "total_votes": int(df["votes"].sum()),
        "avg_votes": float(df["votes"].mean()),
        "total_industries": len(df["industry"].unique()),
        "total_regions": len(df["region"].unique()),
        "top_startup": df.loc[df["Ranking"].idxmin()] if len(df) > 0 else None,
        "highest_voted": df.loc[df["votes"].idxmax()] if len(df) > 0 else None,
    }


def get_startups_by_region(region):
    """Get startups in a specific region."""
    df = load_startups_data()
    return df[df["region"] == region].sort_values("votes", ascending=False)


def get_startups_by_industry(industry):
    """Get startups in a specific industry."""
    df = load_startups_data()
    return df[df["industry"] == industry].sort_values("votes", ascending=False)


def get_startups_by_domain(domain):
    """Get startups with a specific domain ending."""
    df = load_startups_data()
    return df[df["Domain ending"] == domain].sort_values("votes", ascending=False)


def search_startups(query):
    """Search startups by name or description."""
    df = load_startups_data()
    query = query.lower()
    mask = (
        df["Startups Name"].str.lower().str.contains(query, na=False)
        | df["description"].str.lower().str.contains(query, na=False)
        | df["industry"].str.lower().str.contains(query, na=False)
    )
    return df[mask].sort_values("votes", ascending=False)


def get_industry_growth():
    """Get industry growth metrics."""
    df = load_startups_data()
    industry_stats = df.groupby("industry").agg({
        "votes": ["sum", "count", "mean"],
        "Ranking": "mean"
    }).reset_index()
    industry_stats.columns = ["industry", "total_votes", "count", "avg_votes", "avg_ranking"]
    industry_stats = industry_stats[industry_stats["industry"] != ""]
    return industry_stats.sort_values("total_votes", ascending=False)


def get_region_growth():
    """Get region growth metrics."""
    df = load_startups_data()
    region_stats = df.groupby("region").agg({
        "votes": ["sum", "count", "mean"],
        "Ranking": "mean"
    }).reset_index()
    region_stats.columns = ["region", "total_votes", "count", "avg_votes", "avg_ranking"]
    return region_stats.sort_values("total_votes", ascending=False)


def get_domain_performance():
    """Get performance metrics by domain extension."""
    df = load_startups_data()
    domain_stats = df.groupby("Domain ending").agg({
        "votes": ["sum", "count", "mean"],
        "Ranking": "mean"
    }).reset_index()
    domain_stats.columns = ["domain", "total_votes", "count", "avg_votes", "avg_ranking"]
    return domain_stats.sort_values("total_votes", ascending=False)


def get_trending_startups(n=20):
    """Get trending startups (highest votes)."""
    df = load_startups_data()
    df["votes"] = pd.to_numeric(df["votes"], errors="coerce").fillna(0)
    return df.nlargest(n, "votes")[
        ["Startups Name", "industry", "region", "city", "votes", "Ranking", "Domain ending"]
    ]


def get_top_ranked_startups(n=20):
    """Get top ranked startups (best ranking)."""
    df = load_startups_data()
    df["Ranking"] = pd.to_numeric(df["Ranking"], errors="coerce").fillna(0)
    df = df[df["Ranking"] > 0]
    return df.nsmallest(n, "Ranking")[
        ["Startups Name", "industry", "region", "city", "votes", "Ranking", "Domain ending"]
    ]
