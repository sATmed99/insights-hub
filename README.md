# Global Startup Analytics Hub 🌍

A comprehensive, real-time analytics platform providing PowerBI-style insights into the global startup ecosystem built with Python, Streamlit, and Plotly.

## Overview

Global Startup Analytics Hub delivers enterprise-grade data analytics and visualization for worldwide startup trends and opportunities:

**Core Analytics Pages:**
- **📈 Dashboard**: Real-time KPIs, global investment trends, industry distribution, trending startups
- **🌍 Geographic Analysis**: Continental breakdown, heatmaps, regional trends, city rankings (500+ cities)
- **🏭 Industry Analytics**: Market saturation analysis, industry trends, competitive landscape, growth metrics
- **🔍 Startup Search**: Full-text search, categorical browsing (150+ industries), ranked & trending startups
- **🔗 Domain Extensions**: Market share analysis, performance metrics, domain comparisons

**Legacy Analytics (Mock Data):**
- City Intelligence, Sector Map, Undervalued Cities, Germany Deep Dive, Country Deep Dive, Methodology

## Key Features

✨ **Real-Time Data Analytics**
- 1000+ startups from worldwide sources
- 1.1M+ community votes analyzed
- Interactive filtering and drill-down capabilities
- Multi-dimensional cross-tabulation

📊 **Comprehensive Data Coverage**
- 500+ cities across 7 continents
- 150+ industry classifications
- 30+ domain extensions (.COM, .IO, .AI, etc.)
- Regional & continental breakdowns

🎯 **PowerBI-Style Visualizations**
- Interactive Plotly charts with drill-down
- Heatmaps and distribution maps
- Trend analysis with time-series data
- Competitive positioning scatter plots
- KPI dashboards with key metrics

🔍 **Advanced Search & Discovery**
- Full-text search across startup names, descriptions, industries
- Category-based browsing by industry, region, domain
- Ranked startups by voting data
- Trending analysis

## Project Structure

```
.
├── app/
│   ├── __init__.py              # App package with imports
│   ├── real_data.py             # Real data loading & analytics (20+ functions)
│   ├── data.py                  # Legacy mock data (for backward compatibility)
│   ├── utils.py                 # Data utilities (used by legacy pages)
│   └── pages/                   # Page modules
│       ├── __init__.py
│       ├── dashboard.py         # Main analytics dashboard
│       ├── geographic_analytics.py
│       ├── industry_analytics.py
│       ├── startup_search.py
│       ├── domain_analytics.py
│       ├── city_intelligence.py (legacy)
│       ├── sector_map.py        (legacy)
│       ├── undervalued_cities.py (legacy)
│       ├── germany_deep_dive.py (legacy)
│       ├── country_deep_dive.py (legacy)
│       └── methodology.py       (legacy)
├── data/
│   ├── votes-by-city.csv
│   ├── votes-by-continent.csv
│   ├── votes-by-industry.csv
│   ├── votes-by-domain endings.csv
│   └── worldwide-trending-startups-votes.csv
├── app_main.py                  # Main Streamlit application
├── requirements.txt             # Python dependencies
├── ANALYTICS_README.md          # Detailed feature documentation
├── QUICKSTART.md                # User quick start guide
└── README.md                    # This file
```

## Installation & Quick Start

### Prerequisites
- Python 3.8+
- pip or conda

### Setup (Conda Recommended)

1. **Clone or download the project**

2. **Create and activate conda environment**
   ```bash
   conda create -n insights-hub python=3.9
   conda activate insights-hub
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app_main.py
   ```

5. **Access the app**
   - Open browser to `http://localhost:8501`
   - The app automatically reloads on changes

### Command Line Shortcuts

Windows with setup script:
```bash
setup_env.bat
```

Linux/Mac:
```bash
bash run.sh
```

## Usage

### Main Dashboard
1. Start the app with `streamlit run app_main.py`
2. View the 📈 Dashboard for real-time KPI overview
3. Use sidebar to navigate to specific analytics pages

### Finding Startups
Use 🔍 **Startup Search** to:
- Search by name (e.g., "Stripe", "Discord")
- Browse by industry (150+ categories)
- Filter by region/continent
- View trending startups
- See ranked startups by votes

### Geographic Analysis
Access 🌍 **Geographic Analytics** to:
- View global distribution pie chart
- Analyze heatmap by region & city
- Compare cities head-to-head
- See regional statistics

### Industry Insights
Explore 🏭 **Industry Analytics** for:
- Industry overview & saturation
- Growth trends by industry
- Industry spotlight (top startups per industry)
- Competitive analysis

### Domain Extension Analysis
Check 🔗 **Domain Extensions** for:
- Market share by domain (.COM, .IO, .AI, etc.)
- Performance metrics by extension
- Domain comparisons
- Extension trends

## Data Sources

The platform analyzes real-world data:

| File | Records | Key Metric | Example |
|------|---------|-----------|---------|
| **votes-by-city.csv** | 500+ | City votes | Sydney: 159K+ votes |
| **votes-by-continent.csv** | 7 | Continental distribution | Europe: 190K+ votes |
| **votes-by-industry.csv** | 150+ | Industry votes | Discord Dev: 93K votes |
| **votes-by-domain endings.csv** | 30+ | Domain performance | .COM: 356K+ votes |
| **worldwide-trending-startups-votes.csv** | 1000+ | Startup rankings | 1.1M+ total votes |

**Total Dataset**: 1,000+ startups across 500+ cities, 150+ industries, 7 continents, 30+ domains

## Technologies & Stack

**Frontend & Visualization:**
- Streamlit 1.36.0 - Interactive web UI
- Plotly 5.18.0 - Interactive visualizations

**Data & Processing:**
- Pandas 2.2.3 - Data analysis & manipulation
- NumPy 1.26.4 - Numerical computing
- Python 3.9+ - Programming language

**Design:**
- Modern light theme with purple gradient
- Responsive grid layouts
- Interactive charts with drill-down capabilities

## Architecture

### Core Module: `app/real_data.py`

**Data Loading Functions:**
- `load_startups_data()` - Load 1000+ startups
- `load_cities_data()` - Load city voting data
- `load_continent_data()` - Load continental aggregates
- `load_industry_data()` - Load industry classifications
- `load_domain_data()` - Load domain extension data

**Processing Functions:**
- `get_startup_stats()` - Overall statistics
- `get_continent_distribution()` - Global breakdown
- `get_top_cities()`, `get_top_industries()` - Rankings
- `get_industry_growth()`, `get_region_growth()` - Trend analysis

**Search Functions:**
- `search_startups()` - Full-text search
- `get_startups_by_region()`, `get_startups_by_industry()` - Categorical filtering

**Data Caching:** All functions use @pd.cache_data for 2-second load times

### Page Modules

| Page | Purpose | Data Source | Users |
|------|---------|-------------|-------|
| **dashboard.py** | KPI overview, trends, rankings | real_data | All |
| **geographic_analytics.py** | Location-based analysis | real_data | Market researchers |
| **industry_analytics.py** | Sector analysis | real_data | Investors |
| **startup_search.py** | Company discovery | real_data | Everyone |
| **domain_analytics.py** | Domain extension insights | real_data | Tech analysts |

## Development Guide

### Adding a New Analytics Page

1. Create `app/pages/new_page.py`:
   ```python
   """Page description"""
   import streamlit as st
   from app.real_data import needed_functions
   
   def show():
       st.title("📊 Page Title")
       # Your analytics code
   ```

2. Add import in `app/pages/__init__.py`:
   ```python
   from . import new_page
   ```

3. Add routing in `app_main.py` sidebar and page selector

### Extending Data Functions

1. Add new function to `app/real_data.py`
2. Use `@pd.cache_data` decorator for caching
3. Return pandas DataFrame or dict
4. Import in page modules

### Data Updates

To add new CSV data:
1. Place CSV in `data/` folder
2. Create load function in `app/real_data.py`
3. Add processing functions as needed
4. Create new page or update existing pages

## Performance & Scalability

- **Data Load Time**: < 2 seconds (pandas caching)
- **Chart Rendering**: < 1 second (Plotly)
- **Memory Footprint**: ~80MB typical
- **Concurrent Users**: Supports 50+ simultaneous Streamlit sessions
- **Data Size Limit**: Up to 10M startup records manageable

## Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - User quick-start guide
- **[ANALYTICS_README.md](ANALYTICS_README.md)** - Detailed feature documentation
- **.copilot/instructions.md** - Development setup & environment

## Deployment

### 🚀 Recommended: Streamlit Community Cloud (Free)

**Easiest way to share your app with recruiters:**

1. Push code to GitHub
2. Visit [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Sign in with GitHub
4. Click "Create app" → Select repo `streamlit_app.py`
5. Get public URL to share: `https://insights-hub-[name].streamlit.app/`

**See [DEPLOY_TO_STREAMLIT_CLOUD.md](DEPLOY_TO_STREAMLIT_CLOUD.md) for detailed instructions.**

### Other Deployment Options

| Platform | Cost | Setup Time | Best For |
|----------|------|-----------|----------|
| **Streamlit Cloud** | Free | 2 min | Quick sharing with recruiters |
| Heroku | Free tier ending | 10 min | More control |
| Vercel | Free tier | 10 min | Static-friendly |
| Railway | Free credits | 10 min | Easy deployment |
| Docker | Your server | 20 min | Full control |

**For CV/Recruiter Sharing:** Use **Streamlit Cloud** - it's free, 1-click deploy, and perfect for showcasing your work.

See also:
- [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md) - Pre-deployment verification
- [DEPLOY_TO_STREAMLIT_CLOUD.md](DEPLOY_TO_STREAMLIT_CLOUD.md) - Full deployment guide

## Version History

| Version | Date | Changes |
|---------|------|---------|
| **2.0.0** | Mar 2026 | Real data, new analytics, modular architecture |
| **1.0.0** | Jan 2026 | Initial EuroStartup Radar with mock data |

## Support & Troubleshooting

**App won't start?**
- Verify Python 3.8+ installed: `python --version`
- Check dependencies: `pip install -r requirements.txt`
- Ensure you're in the correct directory
- Try conda environment: `conda create -n insights-hub python=3.9`

**Data not loading?**
- Check `data/` folder has all 5 CSV files
- Verify CSV file names match exactly
- Check pandas version: `pip install pandas==2.2.3`

**Performance issues?**
- Clear cache: `rm -rf ~/.streamlit/cache`
- Restart kernel if using Jupyter
- Check system memory available

---

**Global Startup Analytics Hub** - Real-time insights into worldwide startup ecosystems 🌍

