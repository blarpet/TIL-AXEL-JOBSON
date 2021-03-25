import PySimpleGUI as sg

def start_gui(): # Deklarerar vi funktionen.
    sg.ChangeLookAndFeel('Reds') # Tema sätts.
    sg.SetOptions(text_justification='left') # Texten sätts till höger.
    layout = [[sg.text('Tillämpad programmering', font=('Helvetica', 35))], 
            # Layout, [ [][][] ] Vi jobbar med listor i listor. Efter detta sätts font size.
              [sg.Input(key='-IN-')], # Input fältet skapas.
              [sg.Button('Counter:')]] # Knappen counter.

    window = sg.Window('Tillämpad progrmmering', layout,
                        font=("Helvetica", 22)) # Allt detta läggs sedan i ett objekt "sg.Window".

while True: # Skapar while true loop.
    event, values = window.read() # Sätter event och values för att köra window.read functionen.
    if event == sg.WIN_CLOSED or even == 'Exit': # Om fönstret är stängt eller även om 'Exit' eventet är true så breakar while loopen.
        break
    if event == 'Counter:': #Om event är counter så printas texten nedanför.
        print('This button has now been pressed: ')

event, values = window.read() # Sätter event och values för att köra window.read functionen.


start_gui() # Startar gui funktionen.
