python_editor = "Visual Studio Code"
student_data = ["Carsten Brauer", "S8963350", "Sommersemester 2020", "MiMO", "Beuth Hochschule fuer Technik Berlin"]
tiny_game = "Tic Tac Toe, inspiriert von https://www.python-lernen.de/tic-tac-toe-python-tutorial.htm"
print(student_data)
print()
print(tiny_game)
print()
raster = []
feld = 0
spiel_laeuft = True
an_der_reihe = "X"
zuganzahl = 0

while feld < 10:
    raster.extend(str(feld))
    feld += 1

def raster_anzeigen():
    print (raster[1] + "|" + raster[2] + "|" + raster[3] )
    print (raster[4] + "|" + raster[5] + "|" + raster[6] )
    print (raster[7] + "|" + raster[8] + "|" + raster[9] )

def eingabe():
    global spiel_laeuft
    while True:
        zug = input("Bitte Feld-Nummer eingeben oder \"q\" zum Beenden druecken: ")
        if zug == "q":
            spiel_laeuft = False
            return
        try:
            zug = int(zug)
        except ValueError:
            print("Bitte Zahl zwischen 1 und 9 eingeben!")
        else:
            if zug > 0 and zug < 10:
                if raster[zug] == 'X' or raster[zug] == 'O':
                    print("Feld ist bereits belegt!")
                else:
                    return zug
            else:
                print("Bitte Zahl zwischen 1 und 9 eingeben!")

def spielerwechsel():
    global an_der_reihe
    if an_der_reihe == "X":
        an_der_reihe = "O"
    else:
        an_der_reihe = "X"

def spielende_check():
    if raster[1] == raster[2] == raster[3]:
        return raster[1]
    if raster[4] == raster[5] == raster[6]:
        return raster[4]
    if raster[7] == raster[8] == raster[9]:
        return raster[7]
    if raster[1] == raster[4] == raster[7]:
        return raster[1]
    if raster[2] == raster[5] == raster[8]:
        return raster[2]
    if raster[3] == raster[6] == raster[9]:
        return raster[3]
    if raster[1] == raster[5] == raster[9]:
        return raster[5]
    if raster[7] == raster[5] == raster[3]:
        return raster[5]

raster_anzeigen()
while spiel_laeuft:
    print()
    print ("Spieler " + an_der_reihe + " am Zug")
    zug = eingabe()
    if zug:
        zuganzahl += 1
        raster[zug] = an_der_reihe
        raster_anzeigen()
        gewonnen = spielende_check()
        if gewonnen:
            print ("Spieler " + gewonnen + " hat gewonnen!")
            spiel_laeuft = False
            break
        if zuganzahl == 9:
                print ("Spiel ist unentschieden ausgegangen")
                spiel_laeuft = False
        spielerwechsel()
print() 
input()
