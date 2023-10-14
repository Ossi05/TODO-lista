from TODOManager.TODOLista import TODO
from prettytable import PrettyTable
import colorama;
from datetime import datetime

# ////////////////////////////////////////////////////////////////////
# Tulostaa tehtavia                                                //
#                                                                 //
# /////////////////////////////////////////////////////////////////

todoLista = TODO.GetTODOLista()
todoOtsikot = ["ID", "Otsikko", "Luotu", "Määräpäivä", "Suoritettu"]

def TulostaTODOTehtavat():  # Tulostaa kaikki tehtavat
    table = PrettyTable()
    table.field_names = todoOtsikot
    for todo in todoLista:     
        suoritettu = TarkistaTODO(todo)                   
        table.add_row([todo.ID, todo.otsikko, todo.luotuPaivamaara, todo.maarapaiva, suoritettu])

    print(table)
    
def TarkistaTODO(todo : TODO):
    if (todo.onSuoritettu == True):
            suoritettu = colorama.Fore.GREEN + "Suoritettu" + colorama.Style.RESET_ALL
    else:
        tanaan = datetime.now()
        todo_maarapaiva = datetime.strptime(todo.maarapaiva, "%d.%m.%Y")
        
        if todo_maarapaiva <= tanaan:
            todo.maarapaiva = colorama.Fore.YELLOW + todo.maarapaiva + colorama.Style.RESET_ALL

        
        suoritettu = colorama.Fore.RED + "Tekemättä" + colorama.Style.RESET_ALL 

    return suoritettu


def TulostaTODOTehtava(todo): # Tulostaa tietyn tehtavan
    table = PrettyTable()
    table.field_names = todoOtsikot
    suoritettu = TarkistaTODO(todo)
    table.add_row([todo.ID, todo.otsikko, todo.luotuPaivamaara, todo.maarapaiva, suoritettu])
    print(table)

def TulostaSuoritetutTehtavat(): # Tulostaa suoritetut tehtavat
    table = PrettyTable()
    table.field_names = todoOtsikot
    for todo in todoLista:
        if (todo.onSuoritettu == True):
            suoritettu = TarkistaTODO(todo)
            table.add_row([todo.ID, todo.otsikko, todo.luotuPaivamaara, todo.maarapaiva, suoritettu])
    print(table)


def TulostaTekemattomatTehtavat(): # Tulostaa tekemattomat tehtavat
    table = PrettyTable()
    table.field_names = todoOtsikot
    for todo in todoLista:
        if (todo.onSuoritettu == False):
            suoritettu = TarkistaTODO(todo)
            table.add_row([todo.ID, todo.otsikko, todo.luotuPaivamaara, todo.maarapaiva, suoritettu])
    print(table)


