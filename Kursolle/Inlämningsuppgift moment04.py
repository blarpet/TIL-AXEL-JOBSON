def calculation(bredd, höjd, längd):

    area = bredd*längd
    print(f"Arean är: {area}") 

    if bredd==längd:
        print("Detta är en kvadrat.")

    print("Höjd & Volym")
    print("------------")

    for i in range(1, höjd):
         print(f"{i}   |   {i*area} ")


Blist = []
Llist = []
Hlist = []


cal = str(input("Vill du skapa en rektangel min kära son?[Y/N]"))
while cal == "Y":
    längd = "a"
    höjd = "b"
    bredd = "c"
    while längd == "a":
        try:
            längd = int(input("Vad är längden på denna rektangel?"))
        except ValueError:
             print("Din hjärna är för liten men du för en till chans i livet din lilla babian unge.")
        Llist.append(längd)
    while höjd == "b":
        try:
            höjd = int(input("Vilken höjd vill du använda för denna rektangel?"))
        except ValueError:
            print("Din hjärna är för liten men du för en till chans i livet din lilla babian unge.")
        Hlist.append(höjd)
    while bredd == "c":
        try:
            bredd = int(input("Vad är bredden på denna rektangel?"))
        except ValueError:
            print("Din hjärna är för liten men du för en till chans i livet din lilla babian unge.")
        Blist.append(bredd)


    if höjd < 0:
        höjd = 1
    elif höjd > 10:
        höjd = 10


    calculation(bredd, höjd, längd)
    cal = str(input("Vill du skapa en till rektangel min första son? [Y/N]"))
    if cal == "N":
        break
q = str(input("Vill du ha lite data? [Y/N]"))
if q == "Y":
    print(f"De värden du satte för Bredd är:  {Blist}" )
    print(f"De värden du satte för Längd är:  {Llist}" )
    print(f"De värden du satte för Höjd är:   {Hlist}" )
if q == "N":
    print("if you do drugs you go to hell before you die")