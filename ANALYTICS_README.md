# 🌍 Global Startup Analytics Hub

A comprehensive business analytics solution for exploring the worldwide startup ecosystem using real data and interactive visualizations.

## ✨ Features

### **Real-Time Analytics**
- **5+ datasets** with 1000+ startups tracked globally
- Vote aggregation by city, continent, industry, and domain
- Real-time insights calculated from source data

### **Core Pages**

#### 📈 Dashboard
The main analytics hub displaying:
- **KPIs**: Total startups, votes, industries, regions
- **Geographic distribution**: Continent-level market analysis
- **Industry heatmap**: Top performers and emerging sectors
- **Trending startups**: Most voted companies worldwide
- **Key insights**: Leading hubs, dominant industries, market leaders

#### 🌍 Geographic Analysis
Explore startups by location:
- **Continental view**: Market share and voting distribution
- **Regional breakdown**: City-level analysis per region
- **City comparison**: Head-to-head metrics
- **Heatmap**: Startups vs. total votes visualization

#### 🏭 Industry Analytics
Deep dive into market trends:
- **Industry overview**: Statistics across all sectors
- **Market trends**: Growth metrics and saturation analysis
- **Industry spotlight**: Detailed analysis of selected industries
- **Competitive analysis**: Compare two industries directly
- **Scatter plot**: Market saturation vs. engagement

#### 🔍 Startup Search
Discover and explore companies:
- **Full-text search**: Find startups by name or description
- **Browse by category**: Filter by industry, region, or domain
- **Trending section**: Top-voted startups from the community
- **Top ranked**: Best-ranked companies
- **Direct links**: Visit startup websites

#### 🔗 Domain Extension Analytics
Understand domain trends:
- **Market share**: .com, .io, .info, and 25+ extensions
- **Performance metrics**: Average votes and startup count per domain
- **Domain comparison**: Head-to-head analysis
- **Insights**: Emerging and dominant domain extensions
- **.com snapshot**: 35.6% market share (356K+ votes)

### **Data-Driven Pages**
- **City Intelligence**: Urban startup ecosystem analysis
- **Sector Map**: Industry distribution mapping
- **Undervalued Cities**: Hidden gem discovery
- **Germany Deep Dive**: Detailed European market analysis
- **Country Comparison**: Multi-country startup metrics
- **Methodology**: Data sources and analysis framework

## 📊 Data Sources

### Included Datasets
```
data/
├── votes-by-city.csv              # 500+ cities, vote aggregation
├── votes-by-continent.csv         # 7 continental regions
├── votes-by-industry.csv          # 150+ industries with rankings
├── votes-by-domain endings.csv    # 30+ domain extensions
└── worldwide-trending-startups-votes.csv  # 1000+ startup companies
```

### Data Metrics
- **Total Startups**: 1000+
- **Global Coverage**: 7 continents
- **Industries Tracked**: 150+
- **Cities Analyzed**: 500+
- **Domain Extensions**: 30+

## 🚀 Getting Started

### Installation
```bash
# Activate conda environment
conda activate insights-hub

# Install dependencies (if needed)
pip install -r requirements.txt
```

### Running the App
```bash
streamlit run app_main.py
```

The app will open at `http://localhost:8501`

## 🎨 Design & UX

### Modern Interface
- **Gradient headers**: Purple to pink color scheme
- **Light theme**: Clean, professional appearance
- **Interactive visualizations**: Plotly charts with hover details
- **Responsive layout**: Works on desktop and tablet
- **Intuitive navigation**: Emoji-labeled tabs and sections

### Visualizations
- Bar charts: Rankings and comparisons
- Pie charts: Market share analysis
- Scatter plots: Correlation analysis
- Heatmaps: Regional distribution
- Line charts: Trend analysis

## 📈 Key Insights from Data

### Market Leaders
- **Top City**: Sydney, Australia (159K votes)
- **Top Industry**: Discord Development (93K votes)
- **Dominant Domain**: .COM (356K votes, 35.6% share)
- **Leading Continent**: Europe (190K+ votes)

### Market Trends
- Tech-focused domains (.io, .app, .ai) gaining traction
- SaaS and infrastructure industries leading growth
- Geographic diversification across all continents
- Average startup engagement increasing

## 🔧 Technical Stack

- **Frontend**: Streamlit
- **Analytics**: Pandas, NumPy
- **Visualization**: Plotly Express
- **Data Format**: CSV
- **Python Version**: 3.9+

## 📁 Project Structure

```
insights-hub/
├── app_main.py                 # Main application entry
├── app/
│   ├── __init__.py
│   ├── real_data.py           # Data loading & processing
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── dashboard.py       # Main dashboard
│   │   ├── geographic_analytics.py
│   │   ├── industry_analytics.py
│   │   ├── startup_search.py
│   │   ├── domain_analytics.py
│   │   └── [legacy pages...]
│   ├── data.py                # Mock data (legacy)
│   └── utils.py               # Utilities
├── data/
│   ├── votes-by-city.csv
│   ├── votes-by-continent.csv
│   ├── votes-by-industry.csv
│   ├── votes-by-domain endings.csv
│   └── worldwide-trending-startups-votes.csv
└── requirements.txt
```

## 💡 Usage Tips

### Dashboard
- **KPIs**: Quick overview of ecosystem size
- **Continental View**: Understand regional market sizes
- **Trending**: See what the community is voting for
- **Insights Cards**: Key statistics at a glance

### Geographic Analysis
- Use **Regional Breakdown** tab to dive into specific areas
- **City Comparison** shows competitive positioning
- **Heatmap** reveals market saturation levels

### Industry Analytics
- Check **Market Trends** for saturation signals
- Use **Industry Spotlight** for deep dives
- **Competitive Analysis** compares two sectors

### Startup Search
- Full-text search works on name, description, industry
- Browse tabs let you explore by category
- Direct website links for further research

## 🔍 Query Examples

### Questions You Can Answer
- "What are the top startups?"
- "Which city has the most startups?"
- "What industries are trending?"
- "Is .io or .com more popular?"
- "What startups focus on AI?"
- "Which region is growing fastest?"
- "How saturated is the SaaS market?"

## 📊 PowerBI-Style Features

This app includes enterprise analytics capabilities:
- ✅ Multi-dimensional analysis
- ✅ Interactive dashboards
- ✅ Drill-down capabilities
- ✅ Comparative analytics
- ✅ KPI tracking
- ✅ Market insights
- ✅ Trend analysis
- ✅ Geographic mapping

## 🎯 Future Enhancements

- [ ] Time-series trending analysis
- [ ] Predictive analytics
- [ ] Geographic mapping with real coordinates
- [ ] Investment tracking
- [ ] Founder network analysis
- [ ] Funding round tracking
- [ ] Exit analysis

## 📝 Notes

- All data is sourced from public startup databases
- Votes represent community engagement and interest
- Rankings reflect startup quality scores
- Domain extensions show branding choices
- Geographic data is city-level granular

## 🤝 Contributing

To add new features or pages:
1. Create new page in `app/pages/`
2. Import in `app/pages/__init__.py`
3. Add route in `app_main.py`
4. Update sidebar navigation

## 📄 License

Part of German University Application Project - Winter 2026

## 📧 Support

For issues or questions, refer to the methodology page or check GitHub issues.

---

**Last Updated**: March 2026  
**Built with**: Streamlit + Plotly + Pandas  
**Status**: Production Ready ✅
