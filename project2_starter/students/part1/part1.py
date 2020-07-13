import json
from datetime import datetime

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


def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = total/num_items

    if float(mean).is_integer():
        output = int(mean)
    else: 
        output = round(mean,1)
    
    return output


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """

    with open(forecast_file) as json_file:
        json_data = json.load(json_file)
        output = []   
        if forecast_file == "data/forecast_5days_a.json" or forecast_file == "data/forecast_5days_b.json":
            Overview_St = "5 Day Overview"
        elif forecast_file == "data/forecast_10days.json":
            Overview_St = "8 Day Overview"
        else:
            pass
        output.append(Overview_St)

        tot_min = 50 #placeholder amount
        tot_max = 0 #placeholder amount
        sum_low = 0
        sum_high = 0
        average_low = 0
        average_high = 0
        num_items = 0

        #For loop for initial overview message
        for day in json_data['DailyForecasts']:
            # print(day)
            Date = convert_date(day['Date'])
            min_tempc = convert_f_to_c(day['Temperature']['Minimum']['Value'])
            max_tempc = convert_f_to_c(day['Temperature']['Maximum']['Value'])
            sum_low += min_tempc
            sum_high += max_tempc
            num_items = num_items +1 
            average_low = calculate_mean(sum_low, num_items)
            average_high = calculate_mean(sum_high, num_items)

            if tot_min < min_tempc:
                tot_min = tot_min
            else: 
                tot_min = min_tempc
                Date_low = Date
            if tot_max > max_tempc or tot_max == max_tempc:
                tot_max = tot_max
            else: 
                tot_max = max_tempc
                Date_high = Date
            
        low_temp = f"\n    The lowest temperature will be {format_temperature(tot_min)}, and will occur on {Date_low}.\n"
        high_temp = f"    The highest temperature will be {format_temperature(tot_max)}, and will occur on {Date_high}.\n" 
        avg_low_temp = f"    The average low this week is {format_temperature(average_low)}.\n"
        avg_high_temp =f"    The average high this week is {format_temperature(average_high)}.\n\n"
        output.append(low_temp)
        output.append(high_temp)
        output.append(avg_low_temp)
        output.append(avg_high_temp)

        # final = f"{Overview_St}\n{low_temp}\n{high_temp}\n{avg_low_temp}\n{avg_high_temp}"
        # output.append(final)

        # print(output)
        #For loop for Daily messages
        dates =[]
        for day in json_data['DailyForecasts']:
            Date = convert_date(day['Date'])
            min_tempc = convert_f_to_c(day['Temperature']['Minimum']['Value'])
            min_temp = format_temperature(min_tempc)
            max_tempc = convert_f_to_c(day['Temperature']['Maximum']['Value'])
            max_temp = format_temperature(max_tempc)
            Day_phrase = day['Day']['LongPhrase']
            Day_rain = day['Day']['RainProbability']
            Night_phrase = day['Night']['LongPhrase']
            Night_rain = day['Night']['RainProbability']
            
            Date =f"-------- {Date} --------\n"
            min_temp=f"Minimum Temperature: {min_temp}\n"
            max_temp=f"Maximum Temperature: {max_temp}\n"
            Day_phrase=f"Daytime: {Day_phrase}\n"
            Day_rain=f"    Chance of rain:  {Day_rain}%\n"
            Night_phrase=f"Nighttime: {Night_phrase}\n"
            Night_rain=f"    Chance of rain:  {Night_rain}%\n\n"

            output.append(Date)
            output.append(min_temp)
            output.append(max_temp)
            output.append(Day_phrase)
            output.append(Day_rain)
            output.append(Night_phrase)
            output.append(Night_rain)

        final_output= ''.join(output)
        # print(final_output)
        return final_output

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))





