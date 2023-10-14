from TODOManager.TODOLista import TODO

# ////////////////////////////////////////////////////////////////////
# Poistaa todo listasta tietyn todo tehtävän                       //
#                                                                 //
# /////////////////////////////////////////////////////////////////


def Poista(todo): # Koodi sekasin
    
    todoLista = TODO.GetTODOLista()
    todoLista.remove(todo)
    print(f"{todo.otsikko} poistettiin onnistuneesti!")


def PoistaSuoritetut():
    ()


def PoistaKaikki():
    ()

def PoistaValitut():
    ()



