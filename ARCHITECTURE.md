# Architecture & System Design - Global Startup Analytics Hub

## System Overview

```
┌─────────────────────────────────────────────────────────┐
│                  Streamlit Frontend                      │
│              (app_main.py - UI/Navigation)               │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  ┌─────────────────────────────────────────────────┐   │
│  │          app/pages/ (11 page modules)            │   │
│  │  Modern (Real Data) | Legacy (Mock Data)         │   │
│  └─────────────────────────────────────────────────┘   │
│                       ↓                                   │
│  ┌──────────────────────┬──────────────────────────┐   │
│  │  app/real_data.py    │   app/data.py & utils.py │   │
│  │  (Core Analytics)    │   (Legacy Support)        │   │
│  └──────────────────────┴──────────────────────────┘   │
│           ↓                      ↓                       │
└─────────────────────────────────────────────────────────┘
                    ↓
        ┌───────────────────────┐
        │  ./data/ CSV Files    │
        │  5 Real Datasets      │
        │  1.1M+ votes          │
        └───────────────────────┘
```

## Layer 1: Data Layer

### Data Sources (`./data/`)

| File | Records | Key Field | Schema |
|------|---------|-----------|--------|
| **votes-by-city.csv** | 500+ | city_name, votes | city, votes, lat, lng, continent |
| **votes-by-continent.csv** | 7 | continent, total_votes | continent, votes, percentage |
| **votes-by-industry.csv** | 150+ | industry_name, votes | industry, votes, market_share |
| **votes-by-domain endings.csv** | 30+ | domain, votes | domain, votes, percentage |
| **worldwide-trending-startups-votes.csv** | 1000+ | company_name, rank | rank, name, description, industry, region, votes |

**Data Loading Pipeline:**
```
CSV → pandas.read_csv() → DataFrame → @pd.cache_data → Memory Cache
```

### Core Data Module (`app/real_data.py`)

**Purpose:** Single source of truth for all data operations

**Architecture Principles:**
1. All CSV loading through explicitly defined functions
2. Caching with `@pd.cache_data` decorator (Streamlit best practice)
3. Returns pandas DataFrame or Python dict
4. Minimal data transformation (mostly pass-through)
5. Designed for composition - functions call other loaded data

**Function Categories:**

#### Category 1: Data Loading (with caching)
```python
@pd.cache_data
def load_startups_data():
    """Load 1000+ startups with votes"""
    return pd.read_csv('data/worldwide-trending-startups-votes.csv')

@pd.cache_data
def load_cities_data():
    """Load 500+ cities with vote counts"""
    return pd.read_csv('data/votes-by-city.csv')

# ... load_continent_data(), load_industry_data(), load_domain_data()
```

#### Category 2: Aggregation & Statistics
```python
def get_startup_stats():
    """Return dict: total_startups, total_votes, avg_votes, etc."""
    df = load_startups_data()
    return {
        'total_startups': len(df),
        'total_votes': df['votes'].sum(),
        'avg_votes': df['votes'].mean(),
        ...
    }

def get_continent_distribution():
    """Return pie chart data: continent -> vote count"""
    df = load_continent_data()
    return df.groupby('continent')['votes'].sum()
```

#### Category 3: Rankings
```python
def get_top_cities(limit=10):
    """Return top N cities by votes"""
    df = load_cities_data()
    return df.nlargest(limit, 'votes')

def get_trending_startups(limit=10):
    """Return top startups by votes"""
    df = load_startups_data()
    return df.nlargest(limit, 'votes')
```

#### Category 4: Search & Filter
```python
def search_startups(query, field='name'):
    """Full-text search across startups"""
    df = load_startups_data()
    return df[df[field].str.contains(query, case=False, na=False)]

def get_startups_by_region(region):
    """Filter startups by geographic region"""
    df = load_startups_data()
    return df[df['region'] == region]
```

#### Category 5: Growth & Trends
```python
def get_industry_growth():
    """Return industry growth metrics"""
    df1 = load_industry_data()
    # Calculate market share, growth, saturation
    return df1.sort_values('votes', ascending=False)
```

**Design Patterns:**
- **Composition**: `get_startup_stats()` calls `load_startups_data()`
- **Filtering**: Return DataFrames for downstream filtering
- **Sorting**: By votes (primary metric)
- **Caching**: Automatic via decorator - no manual cache management

## Layer 2: Page Layer

### Page Module Structure

Each page follows consistent pattern:

```python
"""Module docstring describing page purpose"""
import streamlit as st
import pandas as pd
import plotly.express as px
from app.real_data import needed_functions

def show():
    """Main page display function - REQUIRED"""
    st.title("📊 Page Title")
    
    # Layout
    col1, col2 = st.columns([2, 1])
    
    # Data loading
    data = get_data_function()
    
    # Visualization
    fig = px.bar(data, ...)
    st.plotly_chart(fig, use_container_width=True)
    
    # Statistics
    st.metric("Label", value)
```

### Modern Pages (Real Data)

#### 1. **dashboard.py** - Executive Overview
- **KPIs**: Total startups, total votes, avg per startup, top industry, top city
- **Charts**:
  - Continental distribution (pie chart)
  - Top 10 startups (bar chart)
  - Industry distribution (bar chart)
  - City rankings (table)
  - Votes trend (scatter plot of startup rank vs votes)
- **Functions Used**: get_startup_stats(), get_continent_distribution(), get_top_cities(), get_trending_startups(), load_startups_data()

#### 2. **geographic_analytics.py** - Location-Based Analysis
- **Tab 1: Continental View**
  - Stats table (continent, votes, %, rank)
  - Pie chart of continental distribution
- **Tab 2: Heatmap**
  - City-by-region heatmap (votes intensity)
  - Scatter plot (city lat/lng with size=votes)
- **Tab 3: Regional Breakdown**
  - Region selector dropdown
  - Top cities in region
  - Regional statistics
- **Tab 4: City Comparison**
  - Multiselect cities
  - Comparison bar chart
  - Side-by-side metrics
- **Functions Used**: load_cities_data(), load_continent_data(), get_top_cities(), get_startups_by_region()

#### 3. **industry_analytics.py** - Sector Analysis  
- **Tab 1: Overview**
  - Industry distribution bar chart
  - Total votes by industry
  - Statistics (# industries, avg votes)
- **Tab 2: Trends & Saturation**
  - Scatter plot: industry saturation vs engagement
  - X-axis: number of companies per industry
  - Y-axis: avg votes per company
- **Tab 3: Industry Spotlight**
  - Industry selector
  - Top companies in industry
  - Industry statistics
- **Tab 4: Competitive Analysis**
  - Compare industries
  - Market share comparison
  - Growth ranking
- **Functions Used**: load_industry_data(), load_startups_data(), search_startups()

#### 4. **startup_search.py** - Discovery & Search
- **Section 1: Search**
  - Text input (search name/description)
  - Results table (rank, name, votes, industry, region)
- **Section 2: Browse by Category**
  - Tabs: Industries | Regions | Domains
  - Multiselect in each tab
  - Result count and table
- **Section 3: Trending**
  - Top 20 startups table
  - Rank, name, votes, growth
- **Section 4: Rankings**
  - Ranked list 1-50
  - Filter by region/industry
- **Functions Used**: search_startups(), get_startups_by_region(), get_trending_startups()

#### 5. **domain_analytics.py** - Extension Insights
- **Section 1: Market Share**
  - Pie chart (.COM, .IO, .AI dominance)
  - Bar chart of top domains
- **Section 2: Performance Metrics**
  - Domains table (domain, votes, %, rank)
  - Statistics (avg votes, total domains)
- **Section 3: Comparison**
  - Multiselect domains
  - Comparison bar chart
  - Market share comparison
- **Section 4: Insights**
  - Key findings (e.g., ".COM dominates with 35% market share")
  - Growth opportunities (.AI, .IO emerging)
- **Functions Used**: load_domain_data(), load_startups_data()

### Legacy Pages (Mock Data)

- **city_intelligence.py** - Old European city analysis
- **sector_map.py** - Old sector distribution
- **undervalued_cities.py** - Old opportunity finder
- **germany_deep_dive.py** - Germany-specific (mock)
- **country_deep_dive.py** - Country-specific (mock)
- **methodology.py** - Explanation of old metrics

**Note:** Legacy pages use `app/data.py` (mock data) and `app/utils.py` functions. These are preserved for backward compatibility but should not be extended. New features should use real_data.py.

## Layer 3: UI/Navigation Layer

### Main Application (`app_main.py`)

**Responsibilities:**
1. Streamlit page configuration
2. CSS styling (light theme, gradient)
3. Sidebar navigation
4. Page routing logic

**Navigation Structure:**
```python
page = st.radio("Select Page", [
    "📈 Dashboard",           # Modern
    "🌍 Geographic Analysis", # Modern
    "🏭 Industry Analytics",  # Modern
    "🔍 Startup Search",      # Modern
    "🔗 Domain Extensions",   # Modern
    # Legacy pages...
])

if page == "📈 Dashboard":
    pages.dashboard.show()
# ... other routing
```

**CSS Styling:**
```css
:root {
    --accent-purple: #667eea;  /* Gradient start */
    --accent-pink: #764ba2;    /* Gradient end */
}
```

All Plotly charts use `template="plotly"` (light theme, NOT plotly_dark).

### Page Package (`app/pages/__init__.py`)

**Imports all page modules for central access:**
```python
from . import dashboard
from . import geographic_analytics
from . import industry_analytics
from . import startup_search
from . import domain_analytics
# ... legacy imports
```

Allows routing: `pages.dashboard.show()`

## Data Flow Example: User Searching for "Stripe"

```
1. User enters "Stripe" in startup_search.py search box
   ↓
2. Page calls: search_startups("Stripe")
   ↓
3. real_data.search_startups() executes:
   - Calls load_startups_data() [cached]
   - Filters: df[df['name'].str.contains("Stripe", case=False)]
   - Returns filtered DataFrame
   ↓
4. Page receives DataFrame with [Stripe Dev, Stripe Inc, ...]
   ↓
5. Page renders table + detailed info
   ↓
6. User sees: Rank, Name, Votes, Industry, Region, Links
```

## File Organization Summary

```
insights-hub/
├── app_main.py              [Layer 3: UI/Navigation]
├── app/
│   ├── __init__.py
│   ├── real_data.py         [Layer 1: Data - CORE MODULE]
│   ├── data.py              [Legacy mock, Layer 1]
│   ├── utils.py             [Legacy utilities, Layer 1]
│   └── pages/               [Layer 2: Pages]
│       ├── __init__.py
│       ├── dashboard.py     [Modern, real data]
│       ├── geographic_analytics.py [Modern, real data]
│       ├── industry_analytics.py   [Modern, real data]
│       ├── startup_search.py       [Modern, real data]
│       ├── domain_analytics.py     [Modern, real data]
│       ├── city_intelligence.py    [Legacy, mock data]
│       ├── sector_map.py           [Legacy, mock data]
│       └── ...
└── data/                    [Layer 1: CSV Data Source]
    ├── votes-by-city.csv
    ├── votes-by-continent.csv
    ├── votes-by-industry.csv
    ├── votes-by-domain endings.csv
    └── worldwide-trending-startups-votes.csv
```

## Design Principles

### 1. **Separation of Concerns**
- **real_data.py**: Only data loading/processing
- **Page modules**: Only visualization/UI
- **app_main.py**: Only routing/configuration

### 2. **Single Responsibility**
- Each function in real_data.py does ONE thing
- Each page module displays ONE type of analysis
- Each chart shows ONE metric/relationship

### 3. **DRY (Don't Repeat Yourself)**
- Shared functions in real_data.py
- Reusable page components
- CSS defined once in app_main.py

### 4. **Caching Strategy**
- CSV loads cached at function level
- Expensive calculations cached
- User interactions NOT cached (filters refresh data)

### 5. **Backward Compatibility**
- Legacy pages + mock data preserved
- No breaking changes to routing
- Users can access old data if needed

## Performance Characteristics

| Operation | Time | Cached |
|-----------|------|--------|
| CSV load | ~500ms | Yes (@pd.cache_data) |
| DataFrame filter | ~50ms | No (user varies) |
| Plotly render | ~100ms | Streamlit built-in |
| Page total | < 2s | First load only |
| Subsequent loads | < 500ms | Cache hit |

## Extensibility: Adding a New Analytics Page

**Step 1:** Create `app/pages/new_analytics.py`
```python
import streamlit as st
from app.real_data import get_startup_stats, load_startups_data

def show():
    st.title("📊 New Analytics")
    stats = get_startup_stats()
    st.metric("Total Startups", stats['total_startups'])
    # ... visualization code
```

**Step 2:** Add import to `app/pages/__init__.py`
```python
from . import new_analytics
```

**Step 3:** Add route to `app_main.py`
```python
page = st.radio("Select Page", [
    ...,
    "📊 New Analytics"  # Add here
])

if page == "📊 New Analytics":
    pages.new_analytics.show()
```

**That's it!** No changes to data layer needed (unless new functions required).

## Testing Strategy

### Unit Tests (for real_data.py functions)
```python
def test_load_startups():
    df = load_startups_data()
    assert len(df) > 1000
    assert 'votes' in df.columns
```

### Integration Tests (page rendering)
```bash
# Run app locally and manually verify:
- Dashboard loads in < 2s
- All charts render correctly
- Filters work as expected
```

### Performance Tests
- Monitor Streamlit server logs for slow operations
- Check page load times in browser dev tools
- Clear cache and do cold start test

## Future Enhancements

1. **Real-time Data**: Replace CSV with API calls
2. **Database**: Use PostgreSQL instead of CSV
3. **Authentication**: Add user login & permissions
4. **Caching**: Add Redis for distributed caching
5. **Notifications**: Alert on trending changes
6. **Export**: CSV/PDF report generation
7. **Comments**: User annotations on data

---

**Last Updated**: March 2026  
**Architecture Version**: 2.0 (Modular, Real-Data)  
**Maintainers**: Data Analytics Team
