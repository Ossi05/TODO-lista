from TODOManager import LueTXT, PoistaTODO, TulostaTODO, LisaaTODO
from TODOManager.TODOLista import TODO


def main():
    LueTXT.LueTODO()

    while True:
        # Tulostaa vaihtoehtodot
        print("\n1. Tulosta tehtävät"
              "\n2. Lisää tehtävä"
              "\n3. Poista tehtävä"
              "\n4. Lopeta?\n")
        valinta = int(input("Mitä tehdään?: ")) # Kysyy käyttäjältä mitä tehdään
        print("\n")

        if valinta == 1:
            TulostaTehtavat()
        elif valinta == 2:
            lisaa()
        elif valinta == 3:         
            poista(valinta)
        elif valinta == 4:
            break
        else:
            print("Valintaa ei löytynyt!")
            continue
        
        input("Paina enter jatkaaksesi...")
    


def poista(valinta : int): # Poistaa tehtäviä

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


def lisaa(): # Lisää tehtäviä
    otsikko = input("Otsikko: ")
    kuvaus = input("Kuvaus: ")
    maarapaiva = input("Määräpäivä: ")
    LisaaTODO.LisaaTODO(otsikko, kuvaus, maarapaiva)
    

def TulostaTehtavat(): # Tulostaa tehtäviä
    TulostaTODO.TulostaTODOTehtavat()




if __name__ == "__main__":
    main()