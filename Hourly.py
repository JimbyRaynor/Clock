from tkinter import *
import datetime
import psutil
import sys

sys.path.insert(0, "/home/deck/Documents") # needed to load LEDlib
import LEDlib

mainwin = Tk()
mainwin.geometry("600x330")
mainwin.configure(bg="black")

fontmedium = ("Arial",45)
fontsmall = ("Arial",24)
fonttiny = ("Arial",18)

currentDate = datetime.datetime.now()
DayofWeek = currentDate.strftime("%a")

Notes = []

def add(mystring):
   Notes.append(mystring.upper())

def addnotes():
    add("Open window 2PM")
    add("Backup to Github")
    if DayofWeek == "Fri":
       add("Washing")
       add("Clean Microwave")
       add("Dishwasher")
       add("Fill water bottles")
    if DayofWeek == "Sat":
       add("9AM Google meet call")
       add("Backup Steam Deck to USB")
       add("Clean Showers")
       add("Wash Showerhead")
       add("Empty tissue bins")
       add("Nose/Ears")
       add("Vacuuming")
       add("Empty Recycling Bin")
       add("Check garage roof")
       add("Add sunrise/sunset dates to clock")
       add("Clear roof spouting")
    if DayofWeek == "Tue":
       add("Vacuuming")
       add("Washing")
       add("Dishwasher")
    if DayofWeek == "Sun" or DayofWeek == "Tue" or DayofWeek == "Thu":
       add("Google Call")
       add("Distribute Exercise Sheets")
    if DayofWeek == "Sun":
       add("Advertise Computing Lecture")
       add("Vacuum behind heaters")
       add("Put Rubbish Out")
    if DayofWeek == "Thu":
       add("Clean solar panels")
       add("    only use water")
       add("Clean Floor\n")


canvas1 = Canvas(mainwin,width=220,height=330,bg="black")
canvas1.place(x=380,y=0)

canvasReminder = Canvas(mainwin,width=379,height=330,bg="black")
canvasReminder.place(x=0,y=0)

CPUusage = LEDlib.LEDtextobj(canvas1,x=0,y=14,text="CPU",colour="light green", pixelsize =3, charwidth=22)
CPUusage2 = LEDlib.LEDtextobj(canvas1,x=70,y=7,text="%",colour="yellow", pixelsize =4, charwidth=29)

addnotes()

ProcList = []
for i in range(14):
  Proc = LEDlib.LEDtextobj(canvas1,x=0,y=44+20*i,text=" ",colour="light blue", pixelsize =2, charwidth=14, solid = True)
  ProcList.append(Proc)


NoteList = []
for i in range(min(14,len(Notes))):
  note = LEDlib.LEDtextobj(canvasReminder,x=0,y=4+23*i,text=Notes[i],colour="light green", pixelsize =2, charwidth=14, solid = False)
  NoteList.append(note)

def resetProcs():
    for i in range(14):
       ProcList[i].update(" ")

processes = []
def updateCpuUsage():
    resetProcs()
    usage = psutil.cpu_percent(interval=1)
    CPUusage2.update(str(usage)+"%")
    getTopProc()
    for i in range(min(14,len(processes))):
       ProcList[i].update(processes[i])
    mainwin.after(1000, updateCpuUsage)


def getTopProc(n=4):
   processes.clear()
   for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
      name = " "+proc.info['name']
      cpu = proc.info['cpu_percent'] 
      python = False
      kworker = False
      code = False
      if name.find("kworker") >= 0: 
         kworker = True
      if name.find("python") >= 0: 
         python = True
         processes.append(name+": "+str(proc.info['cpu_percent'])+"%")
      if name.find("code") >= 0 and cpu > 0.4: 
         python = True
         processes.append(name+": "+str(proc.info['cpu_percent'])+"%")
      if cpu > 0.9 and not python and not kworker and not code:
         processes.append(name[1:10]+": "+str(proc.info['cpu_percent'])+"%") 
   processes.sort()  

updateCpuUsage()

mainwin.mainloop()