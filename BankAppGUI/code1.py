from tkinter import *

window = Tk()
window.title("Welcome to Balls app")
window.geometry("500x500")


lbl1 = Label(window, text="Is this your first time using this program?")
lbl1.grid(column=0, row=0)
accountValue = 0

continue1 = False
depsoitstart = False
withdrawalstart = False

def diebitch():
    btn1.after(0, btn1.destroy)
    btn2.after(0, btn2.destroy)
    lbl1.after(0, lbl1.destroy)
    accountValue = 1000
    continue1 = True

def diebitch2():
    btn1.after(0, btn1.destroy)
    btn2.after(0, btn2.destroy)
    lbl1.after(0, lbl1.destroy)
    continue1 = True

def deposit():
    btn3.after(0, btn3.destroy)
    btn4.after(0, btn4.destroy)
    lbl2.after(0, lbl2.destroy)     
    depsoitstart = True

def withdrawal():
    btn3.after(0, btn3.destroy)
    btn4.after(0, btn4.destroy)
    lbl2.after(0, lbl2.destroy)
    withdrawalstart = True

def clicked1():
    print(text=window.get())

btn1 = Button(window, text="YES", command=diebitch)
btn1.grid(column=2, row=0)

btn2 = Button(window, text="NO", command=diebitch2)
btn2.grid(column=3, row=0)

if  continue1 == True:
    lbl2 = Label(window, text="Do you wish to deposit or withdrawal?")
    btn3 = Button(window, text="Deposit")
    btn4 = Button(window, text="Withdrawal")

if depsoitstart == True:
    lbl3 = Label(window, text="How much do you wish to deposit?")
    commit1 = Button(window, text="Commit", command=clicked1)



#lbl = Label(window, text="Hello and welcome to the bank my fella")
#lbl.grid(column=0, row=0)

#lbl = Label(window, text="Deposit")
#lbl.grid(column=0, row=2)

#lbl = Label(window, text="Withdrawal")
#lbl.grid(column=0, row=4)

#txt = Entry(window,width=10)
#txt.grid(column=1, row=2)
#txt = Entry(window,width=10)
#txt.grid(column=1, row=4)




#def clicked():
    #res = "Welcome to " + txt.get()
    #lbl.configure(text= res)

#btn1 = Button(window, text="Commit")
#btn2 = Button(window, text="Commit")
##btn = Button(window, text="Commit", command=clicked)
#btn1.grid(column=2, row=2)
#btn2.grid(column=2, row=4)

window.mainloop()