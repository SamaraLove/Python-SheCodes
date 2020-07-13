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
        
        if forecast_file == "data/forecast_5days_a.json" or forecast_file == "data/forecast_5days_b.json":
            print("5 Day Overview")
        elif forecast_file == "data/forecast_10days.json":
            print("8 Day Overview")
        else:
            pass

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
            if tot_max > max_tempc:
                tot_max = tot_max
            else: 
                tot_max = max_tempc
                Date_high = Date

        print(f"    The lowest temperature will be {format_temperature(tot_min)}, and will occur on {Date_low}.")  
        print(f"    The highest temperature will be {format_temperature(tot_max)}, and will occur on {Date_high}.")  
        print(f"    The average low this week is {format_temperature(average_low)}.")
        print(f"    The average high this week is {format_temperature(average_high)}.\n")

        #For loop for Daily messages
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
            
            print(f"-------- {Date} --------")
            print(f"Minimum Temperature: {min_temp}")
            print(f"Maximum Temperature: {max_temp}")
            print(f"Daytime: {Day_phrase}")
            print(f"    Chance of rain: {Day_rain}%")
            print(f"Nighttime: {Night_phrase}")
            print(f"    Chance of rain: {Night_rain}%\n")

