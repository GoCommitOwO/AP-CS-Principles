import time

def unix_time_to_date(timecode):
    time_tuple = time.gmtime(timecode)
    # Extract individual components
    hour = time_tuple.tm_hour
    minute = time_tuple.tm_min
    am_pm = "AM" if hour < 12 else "PM"
    hour = hour % 12 if hour % 12 != 0 else 12
    month = time_tuple.tm_mon
    day = time_tuple.tm_mday
    year = str(time_tuple.tm_year)[-2:]
    # Format the date and time string
    formatted_date = "{:02}:{:02} {} {:02}/{:02}/{}".format(hour, minute, am_pm, month, day, year)
    return formatted_date

# Example usage
unix_time = int(input("Please enter your Unix timecode: "))
formatted_date = unix_time_to_date(unix_time)
print("\n\nUnix Time:", unix_time)
print("Formatted Date:", formatted_date)
