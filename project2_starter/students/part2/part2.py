import json
import plotly.express as px
import pandas as pd
from datetime import datetime

# tutorial-env
# pip install virtualenv
# Set-Executionpolicy unrestricted
# virtualenv tutorial-env
# tutorial-env/Scripts/activate
# pip install -r .\requirements.txt     
# 
DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')

def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    degrees = (temp_in_farenheit - 32) * 5/9 

    # if float(degrees).is_integer():
    #     output = int(degrees)
    # else: 
    #     output = round(degrees,1)
    output = round(degrees,1)


    return output                                                         

forecast_file = "data/forecast_5days_a.json"

# pd.read_json (r'data/forecast_5days_a.json')


# json_data = json.load(json_file)
        
df = {}
Days =[]
min_list =[]
max_list = []
min_temp_rf_list = []
min_temp_rfs_list = []
# df.update({'temperature': ['0°C', '10°C', '20°C', '30°C', '40°C']})

with open(forecast_file) as json_file:
    json_data = json.load(json_file)
    for day in json_data['DailyForecasts']:
        Date = convert_date(day['Date'])
        min_temp = convert_f_to_c(day['Temperature']['Minimum']['Value'])
        max_temp = convert_f_to_c(day['Temperature']['Maximum']['Value'])

        min_temp_rf = convert_f_to_c(day['RealFeelTemperature']['Minimum']['Value'])
        min_temp_rfs = convert_f_to_c(day['RealFeelTemperatureShade']['Minimum']['Value'])

        Days.append(Date)
        min_list.append(min_temp)
        max_list.append(max_temp)
        min_temp_rf_list.append(min_temp_rf)
        min_temp_rfs_list.append(min_temp_rfs)

    df.update({"Day": Days})
    df.update({"min_temp": min_list})
    df.update({"max_temp": max_list})
    df.update({"min_temp_rf": min_temp_rf_list})
    df.update({"min_temp_rfs": min_temp_rfs_list})
    # df = {"min_temp": min_list}
    print(df)

fig_1 = px.line(df, x="Day", y=["min_temp", "max_temp"], title = "Daily Forecast")
fig_1.show()


fig_2 = px.scatter(df, x="Day", y=["min_temp", "min_temp_rf","min_temp_rfs"], title = "Daily Forecast - Minimum temperatures")
# fig_2.update_layout(
#     yaxis_title="Temperature (deg)",

# )
fig_2.show()