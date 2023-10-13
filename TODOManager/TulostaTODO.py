from TODOManager.TODOLista import TODO

# ////////////////////////////////////////////////////////////////////
# Tulostaa tehtavia                                                //
#                                                                 //
# /////////////////////////////////////////////////////////////////


def TulostaTODOTehtavat(): # Tulostaa kaikki tehtavat
    luku = 0
    todoLista = TODO.GetTODOLista()
    for todo in todoLista:
        print(luku, todo.otsikko, todo.luotuPaivamaara, todo.viimmeinenPaivamaara, todo.onSuoritettu)
        luku += 1

def TulostaTODOTehtava(todo): # Tulostaa tietyn tehtavan
    todo = TODO.GetTODOLista(todo)
    print(todo.otsikko, todo.luotuPaivamaara, todo.viimmeinenPaivamaara, todo.onSuoritettu)
