from tkinter import *
import tkinter
#Denna kod är inte klar då jag inte hittade en lösning till problemet med att definera variablen i funktionen
window = tkinter.Tk()
window.title("Balls yeah yeah")
window.geometry("500x500")
accountValue = 0
deposit_var = tkinter.IntVar() #Converterar till integer
withdraw_var = tkinter.IntVar()

#sätter values
loop = True
balance = []
change = []
deposit = 0
withdrawal = 0

r = open("money.txt", "r") #Öppnar money.txt

accountValue = r.read()
r.close

#Det fungerar inte då jag hittade ingen lösning för hur jag kan defina en variable inom en funktion, den specificka variablen är accountValue i deposit och withdraw funktionerna

#accountValue = int(accountValue)

def depositFunction():
    print("deposit")
    #depositValue = deposit_var.get()
    #if depositValue >= 0:
    #    accountValue = accountValue + deposit
    #elif depositValue < 0:
    #    print("ERROR")
def withdrawFunction():
    print("withdraw")
    #withdrawValue = withdraw_var.get()
    #if withdrawValue >= 0:
    #    accountValue = accountValue - withdrawal
    #elif withdrawValue < 0: 
    #    print("ERROR")
def transactionHisFunction():
    print("show transaction")
def balanceHisFunction():
    print("show balance")

def newBankwindow():
    buttonYes.after(0, buttonYes.destroy)
    buttonNo.after(0, buttonNo.destroy) #Förstår ButtonNo efter den är använd, samma sak för buttonYes ^

    newWindow = Toplevel(window) #New window
    newWindow.title("Balls")
    newWindow.geometry("500x500") #Window size

    depositButton = tkinter.Button(newWindow, text="Deposit", command=depositFunction) #Deposit button widget
    depositButton.pack()
    depositEntry = tkinter.Entry(newWindow,textvariable = deposit_var, font=('calibre',10,'normal')) #Deposit entry widget
    depositEntry.pack()

    withdrawButton = tkinter.Button(newWindow, text="Withdraw", command=withdrawFunction) #Withdraw button widget
    withdrawButton.pack() #Bestämmer var widgeten skall vara på newWindow
    withdrawEntry = tkinter.Entry(newWindow,textvariable = withdraw_var, font=('calibre',10,'normal')) #Withdraw enter widget
    withdrawEntry.pack()

    transactionButton = tkinter.Button(newWindow, text="View Transaction History", command=transactionHisFunction)
    transactionButton.pack()
    balanceButton = tkinter.Button(newWindow, text="View Balance History", command=balanceHisFunction)
    balanceButton.pack()

def buttonYesPress(): #If its a new account it clears the past history of the account and adds 1000 currency
    accountValue = 1000
    b = open("balance.txt", "a")
    b.truncate(0)
    b.close
    c = open("change.txt", "a")
    c.truncate(0)
    c.close
    newBankwindow()

def buttonNoPress(): #Does really nothing except opens the new window
    newBankwindow()




lbl1 = Label(window, text="Is this your first time using this program?")
lbl1.pack()


buttonYes = tkinter.Button(window, text="Yes", command=buttonYesPress)
buttonYes.pack()

buttonNo = tkinter.Button(window, text="No")
buttonNo.pack()


window.mainloop()