from TODOManager.TODOLista import TODO
from prettytable import PrettyTable
import colorama;
from datetime import datetime

# ////////////////////////////////////////////////////////////////////
# Tulostaa tehtavia                                                //
#                                                                 //
# /////////////////////////////////////////////////////////////////

todoLista = TODO.GetTODOLista()
todoOtsikot = ["ID", "Otsikko","Kuvaus" , "Luotu", "Määräpäivä", "Suoritettu"]

def TulostaTODOTehtavat():  # Tulostaa kaikki tehtavat
    table = PrettyTable() 
    table.field_names = todoOtsikot # Asettaa otsikot
    for todo in todoLista:       # Käy läpi kaikki tehtavat
        suoritettu, kuvaus, maarapaiva = TarkistaTODO(todo)          
        # Lisää tehtavan tiedot taulukkoon
        table.add_row([todo.ID, todo.otsikko, kuvaus ,todo.luotuPaivamaara, maarapaiva, suoritettu])

    print(table) # Tulostaa taulukon
    
def TarkistaTODO(todo : TODO):

    maarapaiva = todo.maarapaiva
    kuvaus = todo.kuvaus

    if (todo.onSuoritettu == True): # Tarkistaa onko tehtava suoritettu
            suoritettu = colorama.Fore.GREEN + "Suoritettu" + colorama.Style.RESET_ALL # Suoritettu teksti vihreällä
    else: 
        tanaan = datetime.now()
        todo_maarapaiva = datetime.strptime(todo.maarapaiva, "%d.%m.%Y")
        
        if todo_maarapaiva <= tanaan: # Tarkistaa onko tehtava myohassa
            maarapaiva = colorama.Fore.YELLOW + maarapaiva  + colorama.Style.RESET_ALL # Maarapaivaan keltainen teksti

        suoritettu = colorama.Fore.RED + "Tekemättä" + colorama.Style.RESET_ALL # Suoritettu teksti punaisella   

    # Näytä vain 60 merkkiä kuvausta ja 2 riviä, jos kuvaus on yli 2 riviä
    kuvaus = kuvaus.split("\n") 
    if len(kuvaus) > 1:
        kuvaus = kuvaus[0] + "\n" + kuvaus[1] 
    else:
        kuvaus = kuvaus[0]
    if len(kuvaus) > 60:
        kuvaus = kuvaus[:60] + "..."

         
    return suoritettu, kuvaus, maarapaiva # Palauttaa suoritettu tekstin ja kuvauksen


def TulostaTODOTehtava(todo): # Tulostaa tietyn tehtavan
    table = PrettyTable()
    table.field_names = todoOtsikot # Asettaa otsikot
    suoritettu, kuvaus, maarapaiva = TarkistaTODO(todo)                   
    # Lisää tehtavan tiedot taulukkoon
    table.add_row([todo.ID, todo.otsikko, kuvaus ,todo.luotuPaivamaara, maarapaiva, suoritettu]) 
    print(table) # TUlostaa taulukon

def TulostaSuoritetutTehtavat(): 
    TulostaTehtavatSuorituksenMukaan(True) # Kutsuu TulostaTehtavatSuorituksenMukaan funktiota


def TulostaTekemattomatTehtavat(): 
    TulostaTehtavatSuorituksenMukaan(False) # Kutsuu TulostaTehtavatSuorituksenMukaan funktiota

def TulostaTehtavatSuorituksenMukaan(suoritettu): # Tulostaa tekemattomat tai suoritetut tehtavat
    table = PrettyTable()
    table.field_names = todoOtsikot
    for todo in todoLista: # Käy läpi kaikki tehtavat
        if (todo.onSuoritettu == suoritettu):
            suoritettu, kuvaus, maarapaiva = TarkistaTODO(todo)                    
            table.add_row([todo.ID, todo.otsikko, kuvaus ,todo.luotuPaivamaara, maarapaiva, suoritettu])
    print(table)


