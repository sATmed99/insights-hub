# Quick Start Guide - Global Startup Analytics Hub

## Data Verification ✅

The app uses **real data** from 5 CSV files in the `./data/` folder:
- ✅ `votes-by-city.csv` (500+ cities)
- ✅ `votes-by-continent.csv` (7 continents)
- ✅ `votes-by-industry.csv` (150+ industries)
- ✅ `votes-by-domain endings.csv` (30+ domain extensions)
- ✅ `worldwide-trending-startups-votes.csv` (1000+ startups)

**Total Dataset:** 1.1M+ votes | 1000+ startups | 500+ cities | 150+ industries | 7 continents

All data is loaded by `app/real_data.py` using cached pandas DataFrames for optimal performance.

---

## Launch the App

### Option 1: Automatic Browser Launch (Recommended)

#### Windows
Double-click or run:
```bash
launch.bat
```

#### Mac/Linux
```bash
chmod +x launch.sh
./launch.sh
```

#### Python (All Platforms)
```bash
python launch.py
```

**What it does:**
- ✅ Activates conda environment (if configured)
- ✅ Detects your default browser
- ✅ Automatically opens app in new browser tab
- ✅ Starts Streamlit server on http://localhost:8501

---

### Option 2: Manual Launch

#### With Conda Environment
```bash
conda activate insights-hub
streamlit run app_main.py
```

#### Without Conda
```bash
streamlit run app_main.py
```

Then open manually: `http://localhost:8501`

---

## Features in the App

### 📈 Dashboard
- 5 KPI metrics (Total Startups, Votes, Industries, Regions, Top City)
- Continental distribution pie chart
- Top 10 startups by votes
- Industry distribution
- City rankings table
- Vote distribution scatter plot

### 🌍 Geographic Analytics
- **Tab 1:** Continental overview with statistics
- **Tab 2:** Geographic heatmap (votes by region/city)
- **Tab 3:** Regional breakdown and comparison
- **Tab 4:** City-to-city comparison

### 🏭 Industry Analytics
- **Tab 1:** Industry overview and distribution
- **Tab 2:** Market saturation vs engagement analysis
- **Tab 3:** Industry spotlight with top companies
- **Tab 4:** Competitive comparison

### 🔍 Startup Search
- Full-text search (search by name, description, industry)
- Browse by category (Industry, Region, Domain)
- Trending startups ranking
- Top 50 ranked startups

### 🔗 Domain Analytics
- Market share pie chart (.COM, .IO, .AI dominance)
- Top domains by votes
- Domain comparison analysis
- Extension performance metrics

---

## First Run Setup

### 1. Install Environment (One-time)
```bash
conda create -n insights-hub python=3.9
conda activate insights-hub
pip install -r requirements.txt
```

### 2. Verify Data Files
Check that `./data/` folder contains 5 CSV files:
```bash
ls data/
```

Should show:
```
votes-by-city.csv
votes-by-continent.csv
votes-by-domain endings.csv
votes-by-industry.csv
worldwide-trending-startups-votes.csv
```

### 3. Launch the App
Use one of the methods above.

---

## Performance

| Metric | Time |
|--------|------|
| App startup | < 5 seconds |
| Page load (cached) | < 2 seconds |
| Chart rendering | < 1 second |
| Search execution | < 500ms |
| Subsequent page loads | < 500ms |

---

## Troubleshooting

### App doesn't open browser
- Manually visit: `http://localhost:8501`
- Check firewall settings
- Ensure port 8501 is available

### Data not loading
- Verify `./data/` folder exists with 5 CSV files
- Check file permissions
- Check CSV headers match expected format

### Conda environment error
```bash
# Recreate environment
conda env remove --name insights-hub
conda create -n insights-hub python=3.9
conda activate insights-hub
pip install -r requirements.txt
```

### Port 8501 already in use
```bash
streamlit run app_main.py --server.port=8502
```

---

## Architecture

- **Frontend:** Streamlit with Plotly visualizations
- **Backend:** Python with Pandas data processing
- **Data:** Real CSV files with @st.cache_data caching
- **Theme:** Light mode with purple gradient (#667eea → #764ba2)

---

## Next Steps

1. ✅ Launch the app
2. 📊 Explore the Dashboard
3. 🔍 Search for your favorite startup
4. 🌍 Analyze geographic trends
5. 🏭 Explore industry insights

---

**Happy Analyzing! 🚀**
