# Day 12 task: Convert timestamps in logs to a different format. This is messy at the moment, as I've just
# been trying to figure out how the different time-related modules work. 

import datetime
import time
import pytz



def main():
    print(datetime.datetime.now(datetime.timezone.utc))
    # Store the UTC timestamp of the provided ISO timestamp
    utc_time = datetime.datetime.fromisoformat('2026-03-21T20:54:02.262Z')
    print(f"UTC time: {utc_time}")

    # Convert the utc_time to a local timestamp
    local_time = utc_time.astimezone(pytz.timezone("US/Mountain"))
    print(f"UTC in local time: {local_time}")

    # Convert the given epoch timestamp to a local time stamp using the time library
    epoch_convert = time.ctime(1774127027)
    print(f"This is the conversion from epoch using time.ctime(): {epoch_convert}")

    # Convert given epoch timestamp into a struct_time ojbect expressed by default in UTC
    utc = time.gmtime(1774127027)
    print(f"The is conversion from epoch into a UTC struct_time object: {utc}")

    # Convert the previous struct_time object into a human readable time stamp.
    asc_time = time.asctime(utc)
    print(f"This is the human readable conversion of the struct_time object, using time.asctime(): {asc_time}")
    timezones = pytz.all_timezones
    # print("Availabe pytz timezones:\n")
    # for zone in timezones:
        # print(f"{zone}")
    
    

# def get_time(timestamp):

main()
