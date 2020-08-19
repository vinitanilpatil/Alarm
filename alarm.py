import random, webbrowser, datetime, time
from datetime import datetime, timedelta

print("Hello I Am A Alarm Clock Made By Vinit Sir!")

url1 = "file:///C:/coding/Alarm/LEW_2.html"
url2 = "file:///C:/coding/Alarm/LookElseWhere.html"
Time = time.strftime("%H:%M:%S")

print("")
print ("Currently it is:", Time)
minutes_of_sleep = int(input("Enter the number of minutes you would like to set alarm:"))
hours_of_sleep = int(input("Enter the number of hours you would like to set alarm:"))
print("")

Alarm = (datetime.now() + timedelta(hours=hours_of_sleep) + timedelta(minutes=minutes_of_sleep)).strftime('%H:%M:%S')
print("You will be told the time at:", Alarm)
yes_no = str(input("Would you like to set this alarm? [Y/N]")).lower()
print("")

while yes_no == "y" or yes_no == "yes":

    while Time != Alarm:
        print("Sir The Time Is:", time.strftime("%H:%M:%S"))
        Time = time.strftime("%H:%M:%S")
        time.sleep(1)
        if Time == Alarm:
            print("")
            print("Time to look else where!")
            url = random.choice([url1, url2])
            webbrowser.open(url)
            break