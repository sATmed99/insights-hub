@echo off
call C:\Users\Tanvir Kabir Shaon\miniconda3\Scripts\activate.bat insights-hub
pip install streamlit==1.36.0
pip install pandas==2.2.3
pip install plotly==5.18.0
pip install dash==2.14.1
pip install dash-bootstrap-components==1.5.0
pip install numpy==1.26.4
pip install folium==0.14.0
pip install streamlit-folium==0.19.0
pip install geopy==2.4.0
echo Installation complete!
pause