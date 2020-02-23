import datetime
import pytz
from tkinter import *
 
from tkinter.ttk import *
 
window = Tk()
window.geometry('270x250')
window.config(bg="#101356")
window.title("Timezone converter")
result=StringVar()
lbl = Label(window, text="Enter year(YYYY):",background="#101356",foreground='white') 
lbl.grid(column=0, row=1)
time1 = Entry(window,width=19)
time1.grid(column=1, row=1)
lb2 = Label(window, text="Enter month(MM):",background="#101356",foreground='white') 
lb2.grid(column=0, row=2)
time2 = Entry(window,width=19)
time2.grid(column=1, row=2)
lb3 = Label(window, text="Enter day(DD):",background="#101356",foreground='white') 
lb3.grid(column=0, row=3)
time3 = Entry(window,width=19)
time3.grid(column=1, row=3)
lb4 = Label(window, text="Enter hour(HH):",background="#101356",foreground='white') 
lb4.grid(column=0, row=4)
time4 = Entry(window,width=19)
time4.grid(column=1, row=4)
lb5 = Label(window, text="Enter minitue(MM):",background="#101356",foreground='white') 
lb5.grid(column=0, row=5)
time5 = Entry(window,width=19)
time5.grid(column=1, row=5)
lb6 = Label(window, text="Enter second(SS):",background="#101356",foreground='white') 
lb6.grid(column=0, row=6)
time6 = Entry(window,width=19)
time6.grid(column=1, row=6)

lb0 = Label(window, text="select required place:",background="#101356",foreground='white')
 
lb0.grid(column=0, row=7)
combo = Combobox(window)
li=[]
for tz in pytz.all_timezones:
  li.append(tz)
combo['values']=tuple(li)

combo.current(0) #set the selected item
 
combo.grid(column=1, row=7)
place=combo.get()
def clicked():
    year=int(time1.get())
    month=int(time2.get())
    day=int(time3.get())
    hour=int(time4.get())
    minute=int(time5.get())
    second=int(time6.get())
    user_time=datetime.datetime(year,month,day,hour,minute,second)
    zone=""+combo.get()
    other_timezone=pytz.timezone(zone)
    time_result=pytz.utc.localize(user_time).astimezone(other_timezone)
    print(time_result)
    result.set(time_result)
    res=Label(window,text="Your Zone time : ",background="#101356",foreground='white')
    res.grid(column=0, row=9,columnspan=2)
    Label(window,textvariable=result,background="#101356",foreground='white').grid(column=0,row=10,columnspan=2)
    
    #lbl.configure(text="Button was clicked !!")
 
btn = Button(window, text="Get time", command=clicked)
 
btn.grid(column=0, row=8,columnspan=2)

 

window.mainloop()
