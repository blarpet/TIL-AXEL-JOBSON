from tkinter import *
import tkinter

window = tkinter.Tk()
window.title("Welcome to Balls app")
window.geometry("500x500")
accountValue = 0


lbl1 = Label(window, text="Is this your first time using this program?")
lbl1.pack()

entry1 = tkinter.Entry(window)
entry1.pack()

def depositFunction():
    print("deposit")

def withdrawFunction():
    lbl2.after(0, lbl2.destroy)
    withdrawAmount = tkinter.Entry(window)
    withdrawAmount.pack()


def dep_or_wit():
    lbl2 = Label(window, text="Do you wish to withdraw or deposit?")
    lbl2.pack()

    depositButton = tkinter.Button(window, text="Deposit", command=depositFunction)
    depositButton.pack()
    withdrawButton = tkinter.Button(window, text="Withdraw", command=withdrawFunction)
    withdrawButton.pack()


def button_press():
    if entry1.get() == "yes":
        print("yes")
        entry1.after(0, entry1.destroy)
        lbl1.after(0, lbl1.destroy)
        button.after(0, button.destroy)
        accountValue = 1000
        dep_or_wit()

    elif entry1.get() == "no":
        print("no")
        entry1.after(0, entry1.destroy)
        lbl1.after(0, lbl1.destroy)
        button.after(0, button.destroy)
        dep_or_wit()


button = tkinter.Button(window, text="Enter", command=button_press)
button.pack()



    #lbl3 = Label(window, text="How much do you wish to deposit?")
    #commit1 = Button(window, text="Commit", command=clicked1)



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