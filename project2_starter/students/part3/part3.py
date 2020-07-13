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

def convert_time(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%H:%M:%S')

    # 2020-06-21T07:00:00+08:00
    #  Monday 22 June 2020.

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

# forecast_file = "data/historical_6hours.json"
# forecast_file = "data/historical_24hours_a.json"
forecast_file = "data/historical_24hours_b.json"

        
df = {}
Days =[]
time_ls = []
temp_list =[]
min_temp_rf_list = []
weather_text_ls =[]
max_UV = 0
UV_hours = 0
tot_min = 50 
tot_max = 0 
min_temp_time =0
max_temp_time = 0
rain_tot = 0
rain_hr = 0
rain_no = 0
day_hrs = 0
night_hr = 0
with open(forecast_file) as json_file:
    json_data = json.load(json_file)
    for hour in json_data:
        date = convert_date(hour['LocalObservationDateTime'])
        time = convert_time(hour['LocalObservationDateTime'])
        weather_text=hour['WeatherText']
        # print(weather_text)
        UV=hour['UVIndex']
        # print(f"UV: {UV}")
        is_Rain = hour['HasPrecipitation']
        is_Day = hour['IsDayTime']

        temp = hour['Temperature']['Metric']['Value']
        min_temp_rf = hour['RealFeelTemperature']['Metric']['Value']
        # print(temp)

        rain = hour['PrecipitationSummary']['Precipitation']['Metric']['Value']

        print(f"Rain: {rain}, total: {rain_tot}")
        print(rain_hr)
        if is_Rain == True:
            if rain !=0:
                rain_tot += rain
                rain_hr += 1
            else:
                pass
            
        else:
            rain_no += 1
            print("no rain")
        if is_Day == True:
            day_hrs += 1
        else:
            night_hr+= 1

        if max_UV > UV:
            max_UV = max_UV
        elif max_UV == UV:
            max_UV = max_UV
            UV_hours = UV_hours + 1
        else:
            max_UV = UV
            date_UV = date
            time_UV = time    
        

        if tot_min < temp:
            tot_min = tot_min
        else: 
            tot_min = temp
            date_low = date
            min_temp_time = time
        if tot_max > temp:
        # or tot_max == temp:
            tot_max = tot_max
        else: 
            tot_max = temp
            date_high = date
            max_temp_time = time
        

        weather_text_ls.append(weather_text)
        time_ls.append(time)
        Days.append(date)
        temp_list.append(temp)
        min_temp_rf_list.append(min_temp_rf)

    high_UV = f"The highest UV will be {max_UV} on {date_UV} at {time_UV} and will last for {UV_hours} hours.\n"
    low_temp = f"\n    The lowest temperature will be {format_temperature(tot_min)}, and will occur on {date_low} at {min_temp_time}.\n"
    high_temp = f"    The highest temperature will be {format_temperature(tot_max)}, and will occur on {date_high} at {max_temp_time}.\n" 

    rain_fell =  f"Rain fall in past X hours: {rain_tot}mm"
    rain_hours = f"Rain lasted a total of {rain_hr}hrs over the past 24 hours"
    day_hours = f"There were {day_hrs}hrs of daylight in the past 24hours"
    # {night_hr}night"


    print(high_UV)
    print(low_temp)
    print(high_temp)
    print(rain_fell)
    print(rain_hours)
    print(day_hours)

    df.update({"weather_text": weather_text_ls})
    df.update({"time": time_ls})
    df.update({"Day": Days})
    df.update({"temperature": temp_list})
    df.update({"min_temp_rf": min_temp_rf_list})
    


# A single graph that contains two box plots, one for the temperature and one for the real feel temperature.
fig_1 = px.box(df, y=["min_temp", "min_temp_rf"], title = "Historical 6 hours - Minimum and Real Feel Temperatures")
fig_1.update_layout(
    yaxis_title="Temperature (deg)",

)
# fig_1.show()

# A bar graph showing the number of times each “WeatherText” category occurs
fig_2 = px.bar(df, x="weather_text", title = "Historical 6 hours")
# fig_2.show()