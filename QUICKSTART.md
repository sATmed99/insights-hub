# 🚀 Quick Start Guide

## Launch the App

```bash
# Navigate to project directory
cd d:\Mother_Folder\Tithy_Mother_Folder\German_University_Application_Folder\Applied_Universities\German-University\Winter2026\insights-hub

# Activate conda environment
conda activate insights-hub

# Run the app
streamlit run app_main.py
```

**App opens at:** `http://localhost:8501`

## What You'll See

### 📈 Dashboard
Your main analytics hub with:
- **KPIs**: 5 key metrics (startups, votes, industries, regions, engagement)
- **Continental Market Share**: Where startups are globally
- **Top 15 Industries**: Which sectors are trending
- **Top 20 Cities**: Leading startup hubs
- **Trending Startups**: Most voted companies
- **Key Insights**: Market leaders summary

### 🌍 Geographic Analysis
Explore by location:
- Continental distribution (pie + bar charts)
- Regional breakdown by continent
- City comparison tools
- Market saturation heatmap

### 🏭 Industry Analytics
Market trends:
- Industry overview & statistics
- Market saturation analysis
- Industry spotlight deep dives
- Head-to-head industry comparison
- Engagement metrics

### 🔍 Startup Search
Find companies:
- Full-text search by name
- Browse by industry/region/domain
- View trending startups
- See top ranked companies
- Direct links to websites

### 🔗 Domain Extensions
Domain trends:
- .COM dominance (35.6% market share)
- .IO and .INFO performance
- Domain comparison tools
- Emerging extension insights

## Key Features

✅ **1,000+ startups** tracked globally
✅ **Real data** from 5 CSV datasets
✅ **Interactive visualizations** with Plotly
✅ **Modern design** with gradient colors & light theme
✅ **PowerBI-style analytics** with drill-downs
✅ **Search & discovery** tools
✅ **Market insights** automatically calculated
✅ **Geographic analysis** by continent/city

## Data at a Glance

| Metric | Value |
|--------|-------|
| Total Startups | 1,000+ |
| Global Votes | 1.1M+ |
| Cities Analyzed | 500+ |
| Industries | 150+ |
| Continents | 7 |
| Domain Extensions | 30+ |

## Top Markets

**Leading City:** Sydney, Australia (159K votes)
**Top Industry:** Discord Development (93K votes)
**Dominant Domain:** .COM (35.6% market share)
**Leading Region:** Europe (19% of global votes)

## Tips for Using the App

1. **Dashboard First**: Start here for overall market overview
2. **Geographic**: Understand where opportunities are
3. **Industry**: Find trending sectors and competition levels
4. **Search**: Discover specific companies of interest
5. **Domain**: See branding trends across startups

## File Structure

```
insights-hub/
├── app_main.py              ← Launch file
├── app/
│   ├── real_data.py        ← Real data loading (1000+ startups)
│   └── pages/
│       ├── dashboard.py
│       ├── geographic_analytics.py
│       ├── industry_analytics.py
│       ├── startup_search.py
│       ├── domain_analytics.py
│       └── [legacy pages...]
├── data/                    ← CSV datasets
│   ├── votes-by-city.csv
│   ├── votes-by-continent.csv
│   ├── votes-by-industry.csv
│   ├── votes-by-domain endings.csv
│   └── worldwide-trending-startups-votes.csv
└── requirements.txt
```

## Example Queries You Can Answer

- "What are the top 10 startups globally?"
- "Which continent has the most startups?"
- "Is SaaS or AI more popular?"
- "What's the performance of .io vs .com domains?"
- "Which cities are startup hotspots?"
- "What industries are emerging?"
- "Are niche domains growing?"

## Features Comparison

| Feature | Dashboard | Geographic | Industry | Search | Domain |
|---------|-----------|-----------|----------|--------|--------|
| KPIs | ✅ | - | - | - | - |
| Charts | ✅ | ✅ | ✅ | ✅ | ✅ |
| Search | - | - | - | ✅ | - |
| Comparison | - | ✅ | ✅ | - | ✅ |
| Deep Dive | - | ✅ | ✅ | ✅ | ✅ |
| Export | - | - | - | - | - |

## Troubleshooting

**App won't start?**
- Ensure conda environment is activated: `conda activate insights-hub`
- Check Python version: `python --version` (3.9+ required)

**No data showing?**
- Verify CSV files are in `./data/` directory
- Check file naming matches exactly

**Performance slow?**
- Data is cached, first load takes longer
- Refresh page if needed

## Environment Details

- **Python**: 3.9+
- **Streamlit**: 1.36+
- **Pandas**: 2.2+ 
- **Plotly**: 5.18+
- **OS**: Windows (PowerShell support)

## Next Steps

1. ✅ Run the app
2. 📊 Explore the Dashboard
3. 🌍 Check Geographic patterns
4. 🔍 Search for companies of interest
5. 📝 Draw insights for your use case

---

**App Status**: Production Ready ✅
**Data Status**: Real & Updated ✅
**Last Updated**: March 2026
