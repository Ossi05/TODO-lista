from TODOManager import LueTXT, PoistaTODO, TulostaTODO
from TODOManager.TODOLista import TODO
from time import sleep


def main():
    LueTXT.LueTODO()

    while True:
        print("\n1. Tulosta tehtävät"
              "\n2. Lisää tehtävä"
              "\n3. Poista tehtävä"
              "\n4. Lopeta?\n")
        valinta = int(input("Mitä tehdään?: "))
        print("\n")

        if valinta == 1:
            TulostaTehtavat()
        elif valinta == 2:
            lisaa()
        elif valinta == 3:         
            poista(valinta)
        elif valinta == 4:
            Kirjoita()
        else:
            print("Valintaa ei löytynyt!")
            continue
        
        input("Paina enter jatkaaksesi...")
    


def poista(valinta : int):

    print("Mitä haluat poistaa? 1. Tietty tehtävä 2. Kaikki suoritetut tehtävät 3. Kaikki tehtävät")
    valinta = int(input("Valinta: "))
    print("Sinun tehtävät ovat: ")
    TulostaTODO.TulostaTODOTehtavat()

    if valinta == 1:
        poistettava = int(input("Minkä tehtävän haluat poistaa?: "))
        varmasti = input("Oletko varma? (k/E): ")
        if (varmasti.lower() == "k"):
            todo = TODO.GetTODO(valinta)
            PoistaTODO.Poista(todo)
    elif valinta == 2:
        PoistaTODO.PoistaSuoritetut()
    elif valinta == 3:
        PoistaTODO.PoistaKaikki()
    else:
        print("Valintaa ei löytynyt!")


def lisaa():
    ()

def Kirjoita():
    ()

def TulostaTehtavat():
    TulostaTODO.TulostaTODOTehtavat()




if __name__ == "__main__":
    main()