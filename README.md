# EuroStartup Radar 🚀

A comprehensive analysis and visualization platform for European startup ecosystems built with Python, Streamlit, and Plotly.

## Overview

EuroStartup Radar provides insights into 21 major European startup hubs across the continent, offering:

- **City Intelligence**: Comparative analysis of cities by attractiveness, votes, and funding
- **Sector Map**: Distribution of tech sectors across European cities and regions
- **Undervalued Cities**: Identification of hidden opportunities and emerging hubs
- **Germany Deep Dive**: Detailed analysis of Germany's startup ecosystem
- **Country Deep Dive**: Individual country-level ecosystem analysis
- **Methodology**: Comprehensive explanation of metrics and analysis approach

## Features

✨ **Interactive Dashboards**
- Real-time data filtering by region, sector, and city status
- Dynamic visualizations with Plotly
- Responsive design with dark theme

📊 **Data Analysis**
- 21 European startup cities
- 5 tech sectors (Fintech, Edtech, Healthtech, SaaS, Deeptech)
- 5 major European regions
- Multi-dimensional metrics

🎯 **Insights**
- Attractiveness Index (0-100)
- Community voting system
- Funding metrics
- City status classification

## Project Structure

```
.
├── app/
│   ├── __init__.py           # App package
│   ├── data.py               # Mock data and data loading
│   ├── utils.py              # Data processing utilities
│   └── pages/                # Page modules
│       ├── __init__.py
│       ├── city_intelligence.py
│       ├── sector_map.py
│       ├── undervalued_cities.py
│       ├── germany_deep_dive.py
│       ├── country_deep_dive.py
│       └── methodology.py
├── app_main.py               # Main Streamlit application
├── main.py                   # Entry point
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── metadata.json             # Project metadata
```

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. **Clone or download the project**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run main.py
   ```

4. **Access the app**
   - Open your browser to `http://localhost:8501`
   - The app will automatically reload on changes

## Usage

### Running the App

```bash
streamlit run main.py
```

The app will start at `http://localhost:8501` by default.

### Navigation

Use the sidebar to:
- **Select Pages**: Navigate between different analysis views
- **Filter Data**: 
  - Select specific regions (DACH, Nordics, CEE, Western Europe, etc.)
  - Filter by tech sectors (Fintech, SaaS, Healthtech, Edtech, Deeptech)
  - Filter by city status (established, rising, hidden gem, undervalued)

### Pages

**1. City Intelligence**
- Overview of all tracked cities
- Top cities by attractiveness
- Regional statistics
- City rankings table

**2. Sector Map**
- Sector distribution across regions
- City sector specialization
- Density heatmaps
- Sector statistics

**3. Undervalued Cities**
- Hidden opportunities with high potential
- Attractiveness vs market attention analysis
- Opportunity classification
- CSV export

**4. Germany Deep Dive**
- Special focus on Germany (Europe's largest startup hub)
- Top German cities
- Sector distribution
- Detailed comparisons

**5. Country Deep Dive**
- Individual country ecosystem analysis
- City comparisons within countries
- Sector and status distributions
- CSV export

**6. Methodology**
- Comprehensive explanation of metrics
- Data sources and limitations
- City status classifications
- Sector definitions

## Data

### Mock Data Structure

Cities include the following metrics:
- `id`: Unique identifier
- `name`: City name
- `country`: Country name
- `countryCode`: ISO country code
- `region`: European region
- `votes`: Community votes
- `attractivenessIndex`: Composite score (0-100)
- `status`: City classification
- `sectors`: Startup count by sector
- `funding`: Total funding in €M
- `lat/lng`: Geographic coordinates

### Regions

- **DACH**: Germany, Austria, Switzerland
- **Nordics**: Sweden, Finland, Estonia
- **CEE**: Poland, Czech Republic, Hungary
- **Western Europe**: UK, France, Netherlands, Spain, Portugal
- **Other**: Belgium, Greece, etc.

### Sectors

- **Fintech**: Financial technology
- **Edtech**: Education technology
- **Healthtech**: Health and biotech
- **SaaS**: Software-as-a-Service
- **Deeptech**: Deep/hard tech

### City Status

- **Established**: Mature hubs with proven track record
- **Rising**: Emerging hubs with growth trajectory
- **Hidden Gem**: High potential, lower market attention
- **Undervalued**: Untapped opportunity for entrepreneurs

## Technologies

- **Frontend**: Streamlit
- **Visualization**: Plotly
- **Data Processing**: Pandas, NumPy
- **Language**: Python 3.8+

## Development

### Adding New Pages

1. Create a new file in `app/pages/`
2. Implement a `show()` function
3. Import in `app/pages/__init__.py`
4. Add to `app_main.py` navigation

### Modifying Data

Edit `app/data.py` to update or add cities.

### Adding Filters

Modify filters in `app_main.py` and `app/utils.py`

## Performance

- **Load Time**: < 2 seconds (cached data)
- **Interactive Charts**: Real-time updates with filters
- **Memory**: < 100MB typical usage

## License

This project is part of the EuroStartup Radar initiative.

## Version

**Current Version**: 1.0.0 (Python/Streamlit)  
**Last Updated**: March 2025

## Support

For issues, questions, or feedback:
- Review the Methodology page for understanding metrics
- Check requirements.txt for dependency compatibility
- Ensure Python 3.8+ is installed

---

**EuroStartup Radar** - Illuminating Europe's Tech Startup Ecosystems 🚀
