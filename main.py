from TODOManager import LueTXT, PoistaTODO, TulostaTODO, LisaaTODO
from TODOManager.TODOLista import TODO
from datetime import datetime


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
            # Fuse kutsu tässä KirjoitaTODO.py kun saat sen valmiiks. että sitä voi testata.
            # Tallenna ne vaikka johonkin testi.txt tiedostoon
        elif valinta == 2:
            lisaa()
            # Fuse kutsu tässä KirjoitaTODO.py kun saat sen valmiiks. että sitä voi testata
        elif valinta == 3:         
            poista(valinta)
            # Fuse kutsu tässä KirjoitaTODO.py kun saat sen valmiiks. että sitä voi testata
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
            PoistaTODO.Poista(poistettava)
    elif valinta == 2:
        PoistaTODO.PoistaSuoritetut()
    elif valinta == 3:
        PoistaTODO.PoistaKaikki()
    else:
        print("Valintaa ei löytynyt!")


def lisaa(): # Lisää tehtäviä
    
    while True:
        otsikko = input("Otsikko: ")
        if otsikko != "":
            break
        else:
            print("Otsikko ei voi olla tyhjä!")
    
    kuvaus = input("Kuvaus: ")
    
    while True:
        maarapaiva = input("Määräpäivä (muodossa pp.kk.vvvv): ")
        try:
            if maarapaiva.count(".") == 1: # Jos maarapaiva on muodossa pp.kk
                maarapaiva += "." + str(datetime.now().year)
            elif maarapaiva.count(".") == 2 and maarapaiva.endswith("."): # Jos maarapaiva on muodossa pp.kk.
                maarapaiva += str(datetime.now().year)

            datetime.strptime(maarapaiva, '%d.%m.%Y')
            break
        except ValueError:
            print("Virheellinen päivämäärä, yritä uudelleen.")
    
    LisaaTODO.LisaaTODO(otsikko, kuvaus, maarapaiva)
    

def TulostaTehtavat(): # Tulostaa tehtäviä
    TulostaTODO.TulostaTODOTehtavat()




if __name__ == "__main__":
    main()