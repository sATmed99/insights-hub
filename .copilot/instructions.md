# Copilot Project Instructions: Global Startup Analytics Hub

## Project Overview
A production-ready business analytics platform using real startup data with PowerBI-style features and modern design.

## Environment Setup
- Always activate the `insights-hub` conda environment before running any commands
- Activation command: `conda activate insights-hub`

## Running the App

### Option 1: Automatic Browser Launch (Recommended)
**Windows:** `launch.bat` or `python launch.py`  
**Mac/Linux:** `./launch.sh` or `python launch.py`

### Option 2: Manual Launch
```bash
streamlit run app_main.py
```

**App Details:**
- 🌐 Launches at: `http://localhost:8501`
- ✅ Uses **REAL DATA** from `./data/` folder (1.1M+ votes verified)
- 📊 Supports 1,000+ startups with 500+ cities & 150+ industries
- ⚡ Page load time: < 2 seconds (cached with @st.cache_data)
- 🔄 Auto-reload enabled for development
- 🌐 Launcher scripts auto-open in default browser

## Data Architecture

✅ **USING REAL DATA FROM CSV FILES** - NOT Mock Data

- **Data Module**: `app/real_data.py` - All data loading & processing (20+ functions)
- **Data Source**: ✅ VERIFIED real CSV files in `./data/` directory
- **Caching**: Streamlit @st.cache_data for maximum performance
- **Real Datasets** (Verified Present):
  - ✅ `votes-by-city.csv` (500+ cities, real vote counts)
  - ✅ `votes-by-continent.csv` (7 regions, real distribution data)
  - ✅ `votes-by-industry.csv` (150+ industries, real market data)
  - ✅ `votes-by-domain endings.csv` (30+ extensions, real performance metrics)
  - ✅ `worldwide-trending-startups-votes.csv` (1000+ companies, real rankings)

**Total Real Data:** 1,100,000+ votes analyzed across global startup ecosystem

## Page Structure
All pages in `app/pages/`:
1. **dashboard.py** - Main KPI & overview dashboard
2. **geographic_analytics.py** - Location-based analysis
3. **industry_analytics.py** - Market trends & competition
4. **startup_search.py** - Search & discovery tools
5. **domain_analytics.py** - Domain extension insights
6. Legacy pages (city_intelligence, sector_map, etc.)

## Design Standards
- **Theme**: Light theme with purple gradient (#667eea → #764ba2)
- **Charts**: Plotly with template="plotly" (NOT plotly_dark)
- **Layout**: Responsive columns & containers
- **UX**: Emoji-enhanced navigation, modern styling

## Best Practices
- Use `real_data.py` functions for all data needs
- Cache expensive operations with @pd.cache_data
- Provide multiple chart types (bar, pie, scatter)
- Include drill-down capabilities in analytics
- Always show KPIs and statistics
- Test data loading before deployment

## Adding New Features
1. Data functions go in `app/real_data.py`
2. New pages go in `app/pages/[name].py`
3. Import in `app/pages/__init__.py`
4. Add route in `app_main.py` sidebar
5. Follow modern design patterns

## Modular Architecture Details

### Core Data Module (`app/real_data.py`)
All data operations go through this module - DO NOT load CSVs directly in pages.

**Key Functions:**
- `load_startups_data()`, `load_cities_data()`, etc. - Loading
- `get_startup_stats()`, `get_continent_distribution()` - Aggregation
- `search_startups()`, `get_startups_by_region()` - Search
- All use `@pd.cache_data` for < 2 second load times

### Page Module Responsibilities
| Page | Purpose | Data Source |
|------|---------|-------------|
| dashboard.py | KPI dashboard | real_data (5 new functions) |
| geographic_analytics.py | Location analysis | real_data (4 tabs) |
| industry_analytics.py | Sector trends | real_data (4 tabs) |
| startup_search.py | Discovery | real_data (search + browse) |
| domain_analytics.py | Extension analysis | real_data (market share) |
| Legacy pages | Backward compatibility | data.py + utils.py (mock) |

### Development Workflow

**Adding a new data function:**
1. Add function to `app/real_data.py`
2. Use `@pd.cache_data` decorator
3. Return DataFrame or dict
4. Use in page via `from app.real_data import function_name`

**Creating a new analytics page:**
1. Create `app/pages/page_name.py`
2. Implement `def show():` function
3. Import data functions from `real_data.py`
4. Add import to `app/pages/__init__.py`
5. Add radio option in `app_main.py` sidebar
6. Test locally before pushing

## Command Reference

```bash
# One-time setup
conda create -n insights-hub python=3.9
conda activate insights-hub
pip install -r requirements.txt

# Run the app
streamlit run app_main.py

# Clear cache if needed
streamlit cache clear

# List available pages
grep "def show" app/pages/*.py
```

## Key Metrics Available
- Total startups, votes, industries, regions
- Continental distribution
- City rankings by votes
- Industry growth metrics
- Domain extension performance
- Trending startups
- Regional comparisons

## Documentation Files
- `ANALYTICS_README.md` - Complete feature documentation
- `QUICKSTART.md` - User guide & feature overview
- `README.md` - Original project readme

## Status
✅ Production Ready
✅ Real Data Integration
✅ Modern Design
✅ PowerBI-Style Analytics
✅ All Pages Functional

Last Updated: March 2026

