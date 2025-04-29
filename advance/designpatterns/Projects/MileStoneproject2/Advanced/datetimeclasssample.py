from datetime import datetime

def timemodule():
    mytime = datetime.time(2, 20)
    print(mytime) # 02:20:00

    mytime = datetime.time(13, 20, 1, 20)
    print(mytime) # 13:20:01.000020

    mydatetime = datetime.datetime(2021, 10, 3, 14, 20, 1)
    print(mydatetime) # 2021-10-03 14:20:01

def caltodaydate():

    # Get the current date and time
    mytime = datetime.now()

    # Access time attributes
    print(mytime.minute)  # Prints the current minute
    print(mytime.hour)  # Prints the current hour
    print(mytime.microsecond)  # Prints the current microsecond


def calendardate():
    mydatetime = datetime(2021, 10, 3, 14, 20, 1)
    print(mydatetime) # 2021-10-03 14:20:01

    mydatetime = mydatetime.replace(year=2020) # 2020-10-03 14:20:01
    print(mydatetime)


calendardate()