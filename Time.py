from jdatetime import timedelta,datetime,JalaliToGregorian,GregorianToJalali
from win10toast import ToastNotifier
import time
import datetime as dt
from dal.Repository import Repository
import threading

current_jalali_date = datetime.now()
year = current_jalali_date.year
month = current_jalali_date.month
def get_month_dates(year, month):
    month_to_num = datetime.j_month_fa_to_num(month)
    days = ['روز']
    if month_to_num == 12:
        last_day = datetime(year + 1, 1, 1) - timedelta(days=1)
        for item in range(last_day.day):
                item=item+1
                days.append(str(item))
                return days
    else:
        last_day = datetime(year, month_to_num + 1, 1) - timedelta(days=1)
        for item in range(last_day.day):
            item+=1
            days.append(str(item))
        return days
def getDay():
    days = ['روز']
    for i in range (31):
        days.append((str(i)))
    return days


def getTime():
    hours = ['ساعت']
    for i in range(24):
        hours.append(str(i))
    return hours
def getMinute():
    minute = ['دقیقه']
    for i in range(60):
        minute.append(str(i))
    return minute


def getGregorian(year,month,day,hour,minute):
        get_month = datetime.now().month
        gregorian = JalaliToGregorian(int(year),int(get_month),int(day))
        return dt.datetime(gregorian.gyear,gregorian.gmonth,gregorian.gday,int(hour),int(minute))


def getJalali(year,month,day,hour,minute):
        time = GregorianToJalali(year,month,day)
        return datetime(time.jyear,time.jmonth,time.jday,hour,minute)







"""

def display_notification():
    try:
        result = Read()
        for item in result:
            if dt.datetime.now().date() == item.time.date() and dt.datetime.now().hour == item.time.hour and dt.datetime.now().minute == item.time.minute:
                toaster = ToastNotifier()
                toaster.show_toast("Reminder", item.task, duration=120)

    except Exception as e:
        print("Error", f"An error occurred: {e}")


def background_task():
    print("hello")
    while True:
        display_notification()
        time.sleep(1) 

background_thread = threading.Thread(target=background_task)
background_thread.daemon = True
background_thread.start()

"""