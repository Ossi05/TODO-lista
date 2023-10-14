from TODOManager.TODOLista import TODO
from prettytable import PrettyTable
import colorama;
from datetime import datetime

# ////////////////////////////////////////////////////////////////////
# Tulostaa tehtavia                                                //
#                                                                 //
# /////////////////////////////////////////////////////////////////

todoLista = TODO.GetTODOLista()

def TulostaTODOTehtavat():  # Tulostaa kaikki tehtavat
    luku = 0
    table = PrettyTable()
    table.field_names = ["ID", "Otsikko", "Luotu", "Määräpäivä", "Suoritettu"]
    for todo in todoLista:
        if (todo.onSuoritettu == True):
            suoritettu = colorama.Fore.GREEN + "Suoritettu" + colorama.Style.RESET_ALL
        else:
            tanaan = datetime.now()
            todo_maarapaiva = datetime.strptime(todo.maarapaiva, "%d.%m.%Y")
            
            if todo_maarapaiva <= tanaan:
                todo.maarapaiva = colorama.Fore.YELLOW + todo.maarapaiva + colorama.Style.RESET_ALL

            
            suoritettu = colorama.Fore.RED + "Tekemättä" + colorama.Style.RESET_ALL 
                           
        table.add_row([luku, todo.otsikko, todo.luotuPaivamaara, todo.maarapaiva, suoritettu])
        luku += 1

    print(table)
    


def TulostaTODOTehtava(todo): # Tulostaa tietyn tehtavan
    table = PrettyTable()
    table.field_names = ["Otsikko", "Luotu", "Määräpäivä", "Suoritettu"]
    todo = TODO.GetTODOLista(todo)
    table.add_row([todo.otsikko, todo.luotuPaivamaara, todo.maarapaiva, todo.onSuoritettu])
    print(table)
