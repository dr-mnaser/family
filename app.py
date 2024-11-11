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

# Function to calculate age in years, months, and days, and time until next birthday
def calculate_age_and_next_birthday(birthdate):
    today = datetime.today()
    
    # Calculate age in years, months, and days
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day
    
    # Adjust for negative values in the days and months
    if days < 0:
        months -= 1
        previous_month = (today.replace(day=1) - timedelta(days=1)).day
        days += previous_month

    if months < 0:
        years -= 1
        months += 12

    # Calculate the next birthday
    next_birthday = birthdate.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    
    # Calculate the time difference until the next birthday
    months_until_birthday = next_birthday.month - today.month
    days_until_birthday = next_birthday.day - today.day
    
    if days_until_birthday < 0:
        months_until_birthday -= 1
        previous_month_days = (next_birthday.replace(day=1) - timedelta(days=1)).day
        days_until_birthday += previous_month_days

    if months_until_birthday < 0:
        months_until_birthday += 12

    return (years, months, days), (months_until_birthday, days_until_birthday)

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

        # Calculate age and get next birthday
        (age_years1, age_months1, age_days1), (months_until_birthday1, days_until_birthday1) = calculate_age_and_next_birthday(birthdate1)
        (age_years2, age_months2, age_days2), (months_until_birthday2, days_until_birthday2) = calculate_age_and_next_birthday(birthdate2)
        (age_years3, age_months3, age_days3), (months_until_birthday3, days_until_birthday3) = calculate_age_and_next_birthday(birthdate3)
        (age_years4, age_months4, age_days4), (months_until_birthday4, days_until_birthday4) = calculate_age_and_next_birthday(birthdate4)
        (age_years5, age_months5, age_days5), (months_until_birthday5, days_until_birthday5) = calculate_age_and_next_birthday(birthdate5)
        
        # if (age_months1 == 0) and (age_days1 == 0): 
        #     # Birthday header with emojis
        #     st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنت طيب يا محمد 🎂🎉</h1>", unsafe_allow_html=True)
        #     st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
        #     st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 You Are Now {age_years1} Years Old 🎂</h2>", unsafe_allow_html=True)
        # if (age_months2 == 0) and (age_days2 == 0):
        #     #st.header("كل سنة وإنتي طيبة يا شيماء")
        #     st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنتي طيبة يا شيماء 🎂🎉</h1>", unsafe_allow_html=True)
        #     st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
        #     st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 You Are Now {age_years2} Years Old 🎂</h2>", unsafe_allow_html=True)
        # if (age_months3 == 0) and (age_days3 == 0):
        #     #st.header("كل سنة وإنتي طيبة يا مريم")
        #     st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنتي طيبة يا مريم 🎂🎉</h1>", unsafe_allow_html=True)
        #     st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
        #     st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 You Are Now {age_years3} Years Old 🎂</h2>", unsafe_allow_html=True)
        # if (age_months4 == 0) and (age_days4 == 0):
        #     #st.header("كل سنة وإنتي طيبة يا جنة")
        #     st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنتي طيبة يا جنة 🎂🎉</h1>", unsafe_allow_html=True)
        #     st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
        #     st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 You Are Now {age_years4} Years Old 🎂</h2>", unsafe_allow_html=True)
        # if (age_months5 == 0) and (age_days5 == 0):
        #     #st.header("كل سنة وإنتي طيبة يا سارة")
        #     st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنتي طيبة يا سارة 🎂🎉</h1>", unsafe_allow_html=True)
        #     st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
        #     st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 You Are Now {age_years5} Years Old 🎂</h2>", unsafe_allow_html=True)

        
        # Birthday celebrations and checks for each individual
        if (age_months1 == 0) and (age_days1 == 0):
            # Exact birthday for محمد
            st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنت طيب يا محمد 🎂🎉</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 You Are Now {age_years1} Years Old 🎂</h2>", unsafe_allow_html=True)

        elif (age_months1 == 0) and (age_days1 <= 3):
            # Recent birthday within the last 4 days
            st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنت طيب يا محمد 🎂🎉</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 Your Age Now is {age_years1} Years and {age_days1} Days 🎂</h2>", unsafe_allow_html=True)

        elif (age_months1 == 11) and (age_days1 >= 28):
            # Upcoming birthday within the month
            st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنت طيب يا محمد 🎂🎉</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 You Will Be {age_years1 + 1} in {days_until_birthday1} Days 🎂</h2>", unsafe_allow_html=True)

        # Same birthday celebration structure for other individuals

        if (age_months2 == 0) and (age_days2 == 0):
            # Exact birthday for شيماء
            st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنتي طيبة يا شيماء 🎂🎉</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 You Are Now {age_years2} Years Old 🎂</h2>", unsafe_allow_html=True)

        elif (age_months2 == 0) and (age_days2 <= 3):
            # Recent birthday within the last 4 days
            st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنتي طيبة يا شيماء 🎂🎉</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 Your Age Now is {age_years2} Years and {age_days2} Days 🎂</h2>", unsafe_allow_html=True)

        elif (age_months2 == 11) and (age_days2 >= 28):
            # Upcoming birthday within the month
            st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنتي طيبة يا شيماء 🎂🎉</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 You Will Be {age_years2 + 1} in {days_until_birthday2} Days 🎂</h2>", unsafe_allow_html=True)

        if (age_months3 == 0) and (age_days3 == 0):
            # Exact birthday for مريم
            st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنتي طيبة يا مريم 🎂🎉</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 You Are Now {age_years3} Years Old 🎂</h2>", unsafe_allow_html=True)

        elif (age_months3 == 0) and (age_days3 <= 3):
            # Recent birthday within the last 4 days
            st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنتي طيبة يا مريم 🎂🎉</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 Your Age Now is {age_years3} Years and {age_days3} Days 🎂</h2>", unsafe_allow_html=True)

        elif (age_months3 == 11) and (age_days3 >= 28):
            # Upcoming birthday within the month
            st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنتي طيبة يا مريم 🎂🎉</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 You Will Be {age_years3 + 1} in {days_until_birthday3} Days 🎂</h2>", unsafe_allow_html=True)

        if (age_months4 == 0) and (age_days4 == 0):
            # Exact birthday for جنة
            st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنتي طيبة يا جنة 🎂🎉</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 You Are Now {age_years4} Years Old 🎂</h2>", unsafe_allow_html=True)

        elif (age_months4 == 0) and (age_days4 <= 3):
            # Recent birthday within the last 4 days
            st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنتي طيبة يا جنة 🎂🎉</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 Your Age Now is {age_years4} Years and {age_days4} Days 🎂</h2>", unsafe_allow_html=True)

        elif (age_months4 == 11) and (age_days4 >= 28):
            # Upcoming birthday within the month
            st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنتي طيبة يا جنة 🎂🎉</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 You Will Be {age_years4 + 1} in {days_until_birthday4} Days 🎂</h2>", unsafe_allow_html=True)

        if (age_months5 == 0) and (age_days5 == 0):
            # Exact birthday for سارة
            st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنتي طيبة يا سارة 🎂🎉</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 You Are Now {age_years5} Years Old 🎂</h2>", unsafe_allow_html=True)

        elif (age_months5 == 0) and (age_days5 <= 3):
            # Recent birthday within the last 4 days
            st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنتي طيبة يا سارة 🎂🎉</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 Your Age Now is {age_years5} Years and {age_days5} Days 🎂</h2>", unsafe_allow_html=True)

        elif (age_months5 == 11) and (age_days5 >= 28):
            # Upcoming birthday within the month
            st.markdown("<h1 style='text-align: center;'>🎉🎂 كل سنة وإنتي طيبة يا سارة 🎂🎉</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>🎈🎈🎈🎈🎈🎈</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #ff6347;'>🎂 You Will Be {age_years5 + 1} in {days_until_birthday5} Days 🎂</h2>", unsafe_allow_html=True)

        st.text("Mohamed Naser's Family Time Unitl Birthdays:")
        data0 = [{'Name': "Mohamed Naser",'Months':months_until_birthday1, 'Days':days_until_birthday1},
                {'Name': "Shimaa Abdelsalam",'Months':months_until_birthday2, 'Days':days_until_birthday2},
                {'Name': "Maryam Naser",'Months':months_until_birthday3, 'Days':days_until_birthday3},
                {'Name': "Jannah Naser",'Months':months_until_birthday4, 'Days':days_until_birthday4},
                {'Name': "Sarah Naser",'Months':months_until_birthday5, 'Days':days_until_birthday5},
                ]
        df0 = pd.DataFrame.from_dict(data0)
        #df0.index = range(1, len(df0) + 1)  # Set index to start from 1
        #df0.index = [1, 2, 3, 4, 5]
        df0.set_index("Name", inplace=True)
        st.write(df0)
        
        st.text("Mohamed Naser's Family Ages:")
        data = [{'Name': "Mohamed Naser",'Years':age_years1, 'Months':age_months1, 'Days':age_days1},
                {'Name': "Shimaa Abdelsalam",'Years':age_years2, 'Months':age_months2, 'Days':age_days2},
                {'Name': "Maryam Naser",'Years':age_years3, 'Months':age_months3, 'Days':age_days3},
                {'Name': "Jannah Naser",'Years':age_years4, 'Months':age_months4, 'Days':age_days4},
                {'Name': "Sarah Naser",'Years':age_years5, 'Months':age_months5, 'Days':age_days5},
                ]
        df = pd.DataFrame.from_dict(data)
        #df.index = range(1, len(df) + 1)  # Set index to start from 1
        #df.index = [1, 2, 3, 4, 5]
        df.set_index("Name", inplace=True)
        st.write(df)
    
main()