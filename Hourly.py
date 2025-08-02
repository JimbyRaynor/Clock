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

def setAfternoon():
    textbox1.delete("1.0","end-1c")
    if DayofWeek == "Mon":
       textbox1.insert(INSERT,"Clean Microwave\n")
    textbox1.insert(INSERT,"Open window 2 PM\n")
    textbox1.insert(INSERT,"Backup to Github\n")
    if DayofWeek == "Sat":
       textbox1.insert(INSERT,"9AM Google meet call\n")
       textbox1.insert(INSERT,"Backup Steam Deck to USB\n")
       textbox1.insert(INSERT,"Clean Showers\n")
       textbox1.insert(INSERT,"Empty tissue bins\n")
       textbox1.insert(INSERT,"Sanding\n")
       textbox1.insert(INSERT,"Nails\n")
       textbox1.insert(INSERT,"Nose/Ears\n")
       textbox1.insert(INSERT,"Vacuuming\n")
       textbox1.insert(INSERT,"Empty Recycling Bin\n")
       textbox1.insert(INSERT,"Check plants around gas hot water heater\n")
       textbox1.insert(INSERT,"Check garage roof\n")
       textbox1.insert(INSERT,"Add sunrise/sunset dates to clock\n")
       textbox1.insert(INSERT,"Tidy letters\n")
       textbox1.insert(INSERT,"Trim grass edges\n")
       textbox1.insert(INSERT,"Clear roof spouting\n")
    if DayofWeek == "Tue":
       textbox1.insert(INSERT,"Vacuuming\n")
       textbox1.insert(INSERT,"Clean Floor\n")
    if DayofWeek == "Sun" or DayofWeek == "Tue" or DayofWeek == "Thu":
       textbox1.insert(INSERT,"Google Call\n")
       textbox1.insert(INSERT,"Distribute Exercise Sheets\n")
    if DayofWeek == "Sun":
       textbox1.insert(INSERT,"Advertise Computing Lecture\n")
       textbox1.insert(INSERT,"Vacuum behind heaters\n")
       textbox1.insert(INSERT,"Put Rubbish Out\n")
    if DayofWeek == "Thu":
       textbox1.insert(INSERT,"Clean solar panels\n")

textbox1 = Text(mainwin,width=24,height=8,font=fonttiny,bg="black",fg="orange")
textbox1.place(x=0,y=0)
canvas1 = Canvas(mainwin,width=220,height=330,bg="black")
canvas1.place(x=380,y=0)

setAfternoon()

CPUusage = LEDlib.LEDtextobj(canvas1,x=0,y=14,text="CPU",colour="light green", pixelsize =3, charwidth=22)
CPUusage2 = LEDlib.LEDtextobj(canvas1,x=70,y=7,text="%",colour="yellow", pixelsize =4, charwidth=29)

ProcList = []
for i in range(14):
  Proc = LEDlib.LEDtextobj(canvas1,x=0,y=44+20*i,text=" ",colour="white", pixelsize =2, charwidth=14, solid = True)
  ProcList.append(Proc)

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
      if "python" in proc.info['name']:
         processes.append("python: "+str(proc.info['cpu_percent'])+"%")
      elif proc.info['cpu_percent'] > 1.0:
         processes.append(proc.info['name']+": "+str(proc.info['cpu_percent'])+"%")   
   proctext = "Apps: \n"
   for p in processes:
      proctext = proctext+p+'\n'
   return proctext

updateCpuUsage()

mainwin.mainloop()