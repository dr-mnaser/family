#import calendar  # Core Python Module
#from datetime import datetime  # Core Python Module
#import datetime
from datetime import datetime, timedelta
import streamlit as st  # pip install streamlit
import psutil
import pandas as pd
import json


# -------------- SETTINGS --------------
page_title = "Mohamed Naser's Family"
page_icon = ":family:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# --- DROP DOWN VALUES FOR SELECTING THE PERIOD ---

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Define a function to get the current CPU and memory usage of the system
def get_system_usage():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    return cpu_percent, mem_percent

# Function to calculate age in years, months, and days
def calculate_age(birthdate):
    today = datetime.today()
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day
    
    # Adjust for negative values
    if days < 0:
        months -= 1
        # Calculate the number of days in the previous month
        previous_month = (today.replace(day=1) - timedelta(days=1)).day
        days += previous_month

    if months < 0:
        years -= 1
        months += 12
    
    return years, months, days

# Define a function to check if the app can serve a new user based on the current resource usage
def can_serve_user():
    cpu_percent, mem_percent = get_system_usage()
    # Check if the current CPU and memory usage are below the threshold
    if cpu_percent < 90 and mem_percent < 90:
        return True
    else:
        return False

def main():
# Check if the app can serve a new user
    if can_serve_user():    
        # Birthdate:
        # Load Firebase credentials from Streamlit secrets
        dates_json = st.secrets["database"]["DATES"]

        # Parse the credentials
        dates_all = json.loads(dates_json)

        birthdate1 = datetime(dates_all["mohamed_year"], dates_all["mohamed_month"], dates_all["mohamed_day"])
        birthdate2 = datetime(dates_all["shimaa_year"], dates_all["shimaa_month"], dates_all["shimaa_day"])
        birthdate3 = datetime(dates_all["maryam_year"], dates_all["maryam_month"], dates_all["maryam_day"])
        birthdate4 = datetime(dates_all["jannah_year"], dates_all["jannah_month"], dates_all["jannah_day"])
        birthdate5 = datetime(dates_all["sarah_year"], dates_all["sarah_month"], dates_all["sarah_day"])

        # Calculate age
        age_years1, age_months1, age_days1 = calculate_age(birthdate1)
        age_years2, age_months2, age_days2 = calculate_age(birthdate2)
        age_years3, age_months3, age_days3 = calculate_age(birthdate3)
        age_years4, age_months4, age_days4 = calculate_age(birthdate4)
        age_years5, age_months5, age_days5 = calculate_age(birthdate5)
        
        st.text("Mohamed Naser's Family Ages:")

        data = [{'Name': "Mohamed Naser",'Years':age_years1, 'Months':age_months1, 'Days':age_days1},
                {'Name': "Shimaa Abdelsalam",'Years':age_years2, 'Months':age_months2, 'Days':age_days2},
                {'Name': "Maryam Naser",'Years':age_years3, 'Months':age_months3, 'Days':age_days3},
                {'Name': "Jannah Naser",'Years':age_years4, 'Months':age_months4, 'Days':age_days4},
                {'Name': "Sarah Naser",'Years':age_years5, 'Months':age_months5, 'Days':age_days5},
                ]
        df = pd.DataFrame.from_dict(data)
        st.write(df)


        # col4, col6, col7 = st.columns(3)
        
        # # Display the metrics
        # col4.metric("Years:", f"{age_years}")
        # col6.metric("Months:", f"{age_months}")
        # col7.metric("Days:", f"{age_days}")

    
main()