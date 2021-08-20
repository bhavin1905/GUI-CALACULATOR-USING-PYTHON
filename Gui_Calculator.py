#********************* GUI CALCULATOR ***************************
import tkinter                      
from tkinter import *
from tkinter.font import Font 
from tkinter import messagebox 


#Global declaration
val = ""            
A = 0
operator = ""


#button functions 
def btn_1_isclicked() :
    global val          #Scope of variable 
    val = val + "1"
    data.set(val)           #command that instruct the button

def btn_2_isclicked() :
    global val  
    val = val + "2"
    data.set(val)

def btn_3_isclicked() :
    global val  
    val = val + "3"
    data.set(val)

def btn_5_isclicked() :
    global val  
    val = val + "4"
    data.set(val)

def btn_6_isclicked() :
    global val  
    val = val + "5"
    data.set(val)

def btn_7_isclicked() :
    global val  
    val = val + "6"
    data.set(val)

def btn_9_isclicked() :
    global val  
    val = val + "7"
    data.set(val)

def btn_10_isclicked() :
    global val  
    val = val + "8"
    data.set(val)

def btn_11_isclicked() :
    global val  
    val = val + "9"
    data.set(val)

def btn_14_isclicked() :
    global val  
    val = val + "0"
    data.set(val)


#Operator button function
def btn_plus_isclicked() :
    global A 
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_minus_isclicked() :
    global A 
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_multi_isclicked() :
    global A 
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_division_isclicked() :
    global A 
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def c_pressed() : 
    global A
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    data.set(val)

def results() : 
    global A
    global operator
    global val
    val2 = val
    if operator == "+" :
        x = int((val2.split("+")[1]))
        c = A + x
        data.set(c)
        val = str(c)
    elif operator == "-" :
        x = int((val2.split("-")[1]))
        c = A - x
        data.set(c)
        val = str(c)
    elif operator == "*" :
        x = int((val2.split("*")[1]))
        c = A * x
        data.set(c)
        val = str(c)
    elif operator == "/" :
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division by zero is not allowed")
            A = ""
            val = ""
            data.set(val)
        else :
            c = int(A / x)
            data.set(c)
            val = str(c)

root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0, 0)            #Size adjust by here
root.title("Calaculator")       #In that we can display the app name 

data  = StringVar()
lbl = Label(
    root,
    text = "Lable",
    anchor = SE,
    font = ("Verdana", 22),
    textvariable = data, 
    background = "white",
    fg = "black"
)
lbl.pack(expand = True, fill = "both")


#Button rows 
btnrow1 = Frame(root,bg= "black")
btnrow1.pack(expand = True, fill = "both")


btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")


btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")


#Row one

btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_1_isclicked,
)
btn1.pack(side = LEFT, expand = True, fill= "both",)

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_2_isclicked,
)
btn2.pack(side = LEFT, expand = True, fill= "both",)

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_3_isclicked,
)
btn3.pack(side = LEFT, expand = True, fill= "both",)

btn4 = Button(
    btnrow1,
    text = "+",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_plus_isclicked,
)
btn4.pack(side = LEFT, expand = True, fill= "both",)


#Row two 

btn5 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_5_isclicked,
)
btn5.pack(side = LEFT, expand = True, fill= "both",)

btn6 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_6_isclicked,
)
btn6.pack(side = LEFT, expand = True, fill= "both",)

btn7 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_7_isclicked,
)
btn7.pack(side = LEFT, expand = True, fill= "both",)

btn8 = Button(
    btnrow2,
    text = "-",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_minus_isclicked,          #COMMAND TO WHAT THE TASK BUTTEN HAVE TO DO 
)
btn8.pack(side = LEFT, expand = True, fill= "both",)



#row 3

btn9 = Button(
    btnrow3,
    text = "7",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_9_isclicked,
)
btn9.pack(side = LEFT, expand = True, fill= "both",)

btn10 = Button(
    btnrow3,
    text = "8",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_10_isclicked,
)
btn10.pack(side = LEFT, expand = True, fill= "both",)

btn11 = Button(
    btnrow3,
    text = "9",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_11_isclicked,
)
btn11.pack(side = LEFT, expand = True, fill= "both",)

btn12 = Button(
    btnrow3,
    text = "*",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_multi_isclicked,
)
btn12.pack(side = LEFT, expand = True, fill= "both",)



#Row four 

btn13 = Button(
    btnrow4,
    text = "C",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = c_pressed,
)
btn13.pack(side = LEFT, expand = True, fill= "both",)

btn14 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_14_isclicked,
)   
btn14.pack(side = LEFT, expand = True, fill= "both",)

btn15 = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = results
)
btn15.pack(side = LEFT, expand = True, fill= "both",)

btn16 = Button(
    btnrow4,
    text = "/",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_division_isclicked
)
btn16.pack(side = LEFT, expand = True, fill= "both",)



root.mainloop()
