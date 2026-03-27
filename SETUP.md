# EuroStartup Radar - Setup & Deployment Guide

## Quick Start (Fastest Way)

### For Linux/macOS:
```bash
chmod +x run.sh
./run.sh
```

### For Windows (PowerShell):
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run main.py
```

### For Windows (CMD):
```cmd
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
streamlit run main.py
```

---

## Detailed Setup Steps

### 1. Prerequisites
Ensure you have:
- **Python 3.8 or higher** installed
- **pip** package manager
- **Git** (optional, for cloning)

Check your Python version:
```bash
python3 --version
```

### 2. Create Virtual Environment

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `streamlit`: Web app framework
- `pandas`: Data processing
- `plotly`: Interactive visualizations
- `dash`: Interactive components (optional, future enhancement)
- `numpy`: Numerical computing
- `folium`: Map visualization
- `streamlit-folium`: Streamlit integration for Folium

### 4. Run the Application

```bash
streamlit run main.py
```

The app will automatically open in your browser at `http://localhost:8501`

---

## Troubleshooting

### Issue: `streamlit: command not found`
**Solution:**
- Activate your virtual environment first
- On Linux/macOS: `source venv/bin/activate`
- On Windows: `venv\Scripts\activate`

### Issue: `ModuleNotFoundError: No module named 'pandas'`
**Solution:**
- Ensure virtual environment is activated
- Run: `pip install -r requirements.txt`

### Issue: Port 8501 already in use
**Solution:**
```bash
streamlit run main.py --server.port 8502
```

### Issue: Memory issues with large data
**Solution:**
- Close other applications
- The app uses lazy loading and caching by default
- Check available RAM: `free -h` (Linux/macOS) or Task Manager (Windows)

---

## Development

### Project Structure
```
.
├── main.py                    # Entry point (streamlit run this)
├── app_main.py                # Main application logic
├── app/
│   ├── data.py               # Data loading and mock data
│   ├── utils.py              # Data processing utilities
│   └── pages/                # Individual page components
│       ├── city_intelligence.py
│       ├── sector_map.py
│       ├── undervalued_cities.py
│       ├── germany_deep_dive.py
│       ├── country_deep_dive.py
│       └── methodology.py
├── requirements.txt          # Python dependencies
└── README.md                 # Main documentation
```

### Adding a New Page

1. Create a new file in `app/pages/new_page.py`:
```python
def show():
    """Display the New Page."""
    import streamlit as st
    st.title("📄 New Page")
    st.markdown("Your content here")
```

2. Import in `app/pages/__init__.py`:
```python
from . import new_page
```

3. Add to navigation in `app_main.py`:
```python
elif page == "New Page":
    pages.new_page.show()
```

### Modifying Mock Data

Edit `app/data.py` to add or update cities:
```python
MOCK_CITIES = [
    {"id": "22", "name": "Your City", ...},
    ...
]
```

---

## Deployment

### Cloud Deployment Options

#### 1. Streamlit Cloud (Recommended for Streamlit apps)
- Free tier available
- Automatic updates from GitHub
- Custom domains supported
- Visit: https://streamlit.io/cloud

**Steps:**
1. Push code to GitHub public repo
2. Sign up at streamlit.io/cloud
3. Connect GitHub repo
4. Deploy with one click

#### 2. Heroku
```bash
# Create Procfile
echo "web: streamlit run main.py --logger.level=error" > Procfile

# Deploy
git push heroku main
```

#### 3. Docker
```
# Build Docker image
docker build -t eurostartup-radar .

# Run container
docker run -p 8501:8501 eurostartup-radar
```

#### 4. AWS / Azure / Google Cloud
Use their container or serverless offerings with Docker

---

## Performance Optimization

### Caching
Data is cached automatically by Streamlit. Clear cache if needed:
- Python: `st.cache_data.clear()`
- In browser: Click "Always rerun" option

### Memory Usage
- Current app: ~50-100MB
- 21 cities, 5 sectors, multiple visualizations

### Load Times
- Initial load: ~2 seconds
- Page navigation: <1 second
- Filters update: <500ms

---

## Environment Variables

Create `.env` file if needed (optional):
```env
STREAMLIT_SERVER_PORT=8501
STREAMLIT_LOGGER_LEVEL=info
STREAMLIT_CLIENT_THEME_BASE=dark
```

---

## Monitoring

### Check Streamlit Logs
```bash
# Linux/macOS
tail -f ~/.streamlit/logs/streamlit_run_*.log

# Windows
# Logs appear in the terminal where you ran streamlit
```

### Health Check
Visit: http://localhost:8501 in browser

---

## Updating the App

### Pull Latest Changes
```bash
git pull origin main
```

### Restart Streamlit
- Press `Ctrl+C` in terminal
- Run `streamlit run main.py` again

### Update Dependencies
```bash
pip install -r requirements.txt --upgrade
```

---

## Uninstall

To remove the app and virtual environment:

**Linux/macOS:**
```bash
deactivate
rm -rf venv/
```

**Windows:**
```powershell
deactivate
rmdir /s venv
```

---

## Support & Resources

- **Streamlit Docs**: https://docs.streamlit.io
- **Plotly Docs**: https://plotly.com/python
- **Pandas Docs**: https://pandas.pydata.org/docs
- **Python Docs**: https://docs.python.org/3

---

**Version**: 1.0.0  
**Last Updated**: March 2025
