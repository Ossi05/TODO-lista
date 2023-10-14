from TODOManager.TODOLista import TODO

# ////////////////////////////////////////////////////////////////////
# Poistaa todo listasta tietyn todo tehtävän                       //
#                                                                 //
# /////////////////////////////////////////////////////////////////


def Poista(id : int): # Poistaa tietyn todo tehtävän
    
    todo = TODO.GetTODO(id)
    if (todo == None):
        print("ID:tä ei löytynyt!")
        return
    poista = TODO.PoistaTODOListasta(todo)
    if (poista):
        print(f"{todo.otsikko} poistettiin onnistuneesti!")
    else:
        print("Poistaminen epäonnistui!")


def PoistaSuoritetut():
    ()


def PoistaKaikki():
    ()

def PoistaValitut():
    ()



