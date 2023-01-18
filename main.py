from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repeats=0
timer=None
timer_break=None


# ---------------------COUNT START & TIMER RESET MECHANISM------------------------ # 
def start_button():
    count(WORK_MIN,counter=0)

def reset_button():
    window.after_cancel(timer)
    # window.after_cancel(timer_break)
    timer_label.config(text="Timer",fg=RED)
    canvas.itemconfig(timer_text,text="00:00")
    checkmark_label.config(text=" ")
    global repeats
    repeats=0



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
    
def count(WORK_MIN,counter):
    timer_label.config(text="Timer",fg=RED)
    global repeats
    global timer
    mark="✔"
    canvas.itemconfig(timer_text,text=f"{WORK_MIN:02}:{counter:02}")
    if counter==0 and WORK_MIN>0:
        WORK_MIN-=1
        counter=60 
    if counter > 0 and WORK_MIN >=0:
        timer=window.after(1000,count,WORK_MIN,counter-1)
    if counter==0 and WORK_MIN==0:
        for _ in range(repeats):
            mark+="✔"
        checkmark_label.config(text=mark)
        repeats+=1    
        if repeats <=3:
            take_break(SHORT_BREAK_MIN,counter=0)
        else:
            repeats=0  
            take_break(LONG_BREAK_MIN,counter=0)



# ---------------------------- BREAK MECHANISM ------------------------------- # 

def take_break(timer,counter):
    # global timer_break
    timer_label.config(text="Break",fg=YELLOW)
    canvas.itemconfig(timer_text,text=f"{timer:02}:{counter:02}")
    if counter==0 and timer>0:
        timer-=1
        counter=60
    if counter > 0 and timer >=0:
        timer_break=window.after(1000,take_break,timer,counter-1)
    if counter==0 and timer==0:   
        count(WORK_MIN,counter)


# ---------------------------- UI SETUP ------------------------------- #

#window setup
window=Tk()
window.title("Pomodoro")
window.config(padx=50,pady=50,background=GREEN)
background=PhotoImage(file="tomato.png")

#Label
timer_label=Label(text="Timer",fg=RED,font=(FONT_NAME,24,"bold"),bg=GREEN)
timer_label.grid(row=0,column=1)

#Buttons
start=Button(text="Start",background=GREEN,fg=RED,command=start_button,highlightthickness=0,font=(FONT_NAME,10,"bold"))
start.grid(row=2,column=0)

reset=Button(text="reset",background=GREEN,fg=RED,command=reset_button,highlightthickness=0,font=(FONT_NAME,10,"bold"))
reset.grid(row=2,column=2)

#check mark
checkmark_label=Label(text=" ",fg=RED,bg=GREEN,font=(FONT_NAME,15,"normal"))
checkmark_label.grid(row=3,column=1)


#Tomato and timer image
canvas=Canvas(width=200,height=224,bg=GREEN,highlightthickness=0)
canvas.create_image(100,112,image=background)
timer_text=canvas.create_text(100,140,text="00:00",font=(FONT_NAME,30,"bold"),fill="white")
canvas.grid(row=1,column=1)



window.mainloop()