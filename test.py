import tkinter

root = tkinter.Tk()
root.geometry("300x300")
root.title("Try code")

entrgy = tkinter.Entry(root)
entrgy.pack()

def on_button():
    if entrgy.get() == "yes":
        slabel = tkinter.Label(root, text="Screen was entered")
        slabel.pack()
    else:
        tlabel = tkinter.Label(root, text="")
        tlabel.pack()

button = tkinter.Button(root, text="Enter", command=on_button)
button.pack()

root.mainloop()