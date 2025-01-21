

# Please give me a Python list of sunrise times for Melbourne, 
# Australia, for Jan 2025 using data from the "time and date" website

# Can only do month by month, o/w crash
# ask for data from "Time and Date website", o/w slightly inaccurate


sunrise_times = [
    "06:01", "06:02", "06:03", "06:04", "06:04", "06:05", "06:06", "06:07",
    "06:08", "06:09", "06:10", "06:11", "06:12", "06:13", "06:14", "06:15",
    "06:16", "06:17", "06:19", "06:20", "06:21", "06:22", "06:23", "06:24",
    "06:25", "06:26", "06:27", "06:29", "06:30", "06:31", "06:32", 
    #Feb
    "06:34", "06:35", "06:37", "06:38", "06:39", "06:40", "06:41", "06:42", "06:43", "06:45",
    "06:46", "06:47", "06:48", "06:49", "06:50", "06:51", "06:52", "06:53", "06:54", "06:56",
    "06:57", "06:58", "06:59", "07:00", "07:01", "07:02", "07:03", "07:04",
    #March
    "07:04", "07:05", "07:06", "07:07", "07:08", "07:09", "07:10", "07:11", "07:12", "07:13",
    "07:14", "07:15", "07:16", "07:17", "07:18", "07:19", "07:20", "07:21", "07:22", "07:23",
    "07:24", "07:25", "07:26", "07:27", "07:28", "07:29", "07:30", "07:31", "07:32", "07:33"
    #April
    "07:33", "07:34", "07:35", "07:36", "07:37", "07:38", "07:39", "07:40", "07:41", "07:42",
    "07:43", "07:44", "07:45", "07:46", "07:47", "07:48", "07:49", "07:50", "07:51", "07:52",
    "07:53", "07:54", "07:55", "07:56", "07:57", "07:58", "07:59", "08:00", "08:01", "08:02"  
]


sunset_times = [
    #jan
    "20:45", "20:45", "20:45", "20:45", "20:45", "20:45", "20:45",
    "20:45", "20:45", "20:45","20:45",  "20:44", "20:44", "20:44", 
    "20:43", "20:43", "20:43", "20:42", "20:42", "20:41", "20:41", 
    "20:40", "20:39", "20:39", "20:38", "20:37", "20:37", "20:36", 
    "20:35", "20:34", "20:33"
]

import math
from tkinter import *
from time import *
#import datetime
from datetime import datetime, timedelta
import calendar
mainwin = Tk()
mainwin.geometry("640x320+1+1") # x=1, y=1
canvas1 = Canvas(mainwin,width=640,height= 320,bg="black")
canvas1.place(x=0,y=0)
fonttiny = ("Courier",11)
fontbig = ("Arial",70)
fontmedium = ("Arial",45)
fontsmall = ("Arial",24)
mydaytext = canvas1.create_text(200,40,font=fontmedium,text="day",fill="yellow")
mytext = canvas1.create_text(200,110,font=fontbig,text="time",fill="#9090FF")
mydaytext2 = canvas1.create_text(200,180,font=fontsmall,text="day",fill="yellow")

def day_of_year(date): 
    return date.timetuple().tm_yday 

today = datetime.today() 
now = datetime.now()
year = now.year
month = now.month
currentday = now.day

def totalminutes(mytime):
    hours, minutes = map(int, mytime.split(":"))
    return 60*hours+minutes

sundrawn = False
mypic = 0

def draw_sun(canvas, x, y, radius):
    global mypic
    mypic = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="yellow", outline="")

def draw_sungrey(canvas, x, y, radius):
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="grey", outline="")

def drawarrow(canvas,x1,y1,x2,y2):
    canvas.create_line(x1, y1, x2, y2, arrow=LAST, fill="yellow")


sunrisetext = canvas1.create_text(40,300,font=fontsmall,text=sunrise_times[day_of_year(today)-1],fill="#9090FF")
sunsettext = canvas1.create_text(380,300,font=fontsmall,text=sunset_times[day_of_year(today)-1],fill="#9090FF")


minsunrise = totalminutes(sunrise_times[day_of_year(today)-1])
minsunset =  totalminutes(sunset_times[day_of_year(today)-1])
suntime = minsunset-minsunrise

highsunhour = (minsunrise+minsunset)/2 // 60
highsunmin = (minsunrise+minsunset)/2 % 60

highsunstring = f"{int(highsunhour):02}:{int(highsunmin):02}"

canvas1.create_text(200,300,font=fontsmall,text=highsunstring,fill="#9090FF")




next_month = (now+timedelta(days=calendar.monthrange(year,month)[1])).month
next_month_name = (now+timedelta(days=calendar.monthrange(year,month)[1])).strftime("%B")
num_days = calendar.monthrange(year,month)[1]
next_num_days = calendar.monthrange(year,next_month)[1]


def str0(num):
    if num <= 9:
        return  "0"+str(num)
    else:
        return str(num) 


def makecalendartext():
    month_name = now.strftime("%B")
    calt = " "+month_name+"\n"
    calt = calt+  " M  T  W  T  F  S  S\n"
    first_weekday = calendar.monthrange(year,month)[0]
    for i in range(first_weekday):
        calt = calt + "   "
    for day in range(1,num_days+1):
        if day < currentday:
            calt = calt + " XX"
            partial = calt
        else:
            calt = calt + " " + str0(day)
            partial = partial + "   "
        if (first_weekday+day) % 7 == 0:
            calt = calt + "\n"
            partial = partial + "\n"
    calt = calt + "\n\n"+" "+next_month_name+"\n"
    calt = calt+  " M  T  W  T  F  S  S\n"
    partial = partial + "\n\n"+" "+next_month_name+"\n"
    partial = partial+  " M  T  W  T  F  S  S\n"
    next_first_weekday = calendar.monthrange(year,next_month)[0]
    for i in range(next_first_weekday):
        calt = calt + "   "
        partial = partial + "   "
    for day in range(1,next_num_days+1):
        calt = calt + " " + str0(day)
        partial = partial + "   "
        if (next_first_weekday+day) % 7 == 0:
            calt = calt + "\n"
            partial = partial + "\n"
    return calt,partial

canvas1.create_text(520,160,font=fonttiny,text=makecalendartext()[0],justify="left",fill="yellow")
canvas1.create_text(520,160,font=fonttiny,text=makecalendartext()[1],justify="left",fill="#AAAAAA")
   

def timer1():
    t = localtime()
    mysec = str0(t.tm_sec)
    mymin = str0(t.tm_min)
    myhour = t.tm_hour
    if myhour > 12: myhour = myhour - 12
    myhour = str(myhour)
    canvas1.itemconfigure(mytext,text=myhour+":"+mymin+":"+mysec)
    now = datetime.now()
    todaystr = now.strftime("%A")
    canvas1.itemconfigure(mydaytext,text=todaystr)
    todaystr2 = now.strftime("%d %B %Y")
    canvas1.itemconfigure(mydaytext2,text=todaystr2)
    mainwin.after(100,timer1)

def drawtimersun(x):
    global sundrawn, mypic
    y = 100*math.sin(x/400*math.pi)
    if sundrawn == True:
        canvas1.delete(mypic)
        draw_sungrey(canvas1, x, 320-y, 1)
    sundrawn = True
    draw_sun(canvas1, x, 320-y, 10)
    

def timersun():
    t = localtime()
    mymin = t.tm_min
    myhour = t.tm_hour
    minloc = myhour*60+mymin-minsunrise
    minscale = 400*minloc/suntime
    drawtimersun(minscale)
    mainwin.after(600000,timersun)

timer1()
timersun()

mainwin.mainloop() 