
# ////////////////////////////////////////////////////////////////////
# todoLista on tallennettu tänne                                   //
# LueTODO tiedosto lukee to-do.txt tiedoston                      //
# ja tallentaa tehtävät todoListaan                              //
# ////////////////////////////////////////////////////////////////


class TODO:

    todoLista = []

    def __init__(self, id, otsikko, kuvaus, luotuPaivamaara, maarapaiva, onSuoritettu):
        self.ID = id
        self.otsikko = otsikko
        self.kuvaus = kuvaus
        self.luotuPaivamaara = luotuPaivamaara
        self.maarapaiva = maarapaiva
        self.onSuoritettu = onSuoritettu

    @classmethod
    def LisaaTODOListaan(cls, toDo): # Lisää tehtävän todoListaan
        cls.todoLista.append(toDo)
    
    @classmethod
    def GetTODOLista(cls): # Palauttaa todoListan
        return cls.todoLista
    
    @classmethod
    def GetTODO(cls, id): # Palauttaa tietyn tehtävän todoListasta ID perusteella
        for todo in cls.todoLista:
            if todo.ID == id:
                return todo
        return None
    
    @classmethod
    def GetNextID(cls): # Palauttaa seuraavan ID:n
        return int(len(cls.todoLista))
    
    @classmethod
    def PoistaTODOListasta(cls, todo): # Palauttaa seuraavan ID:n
        if todo in cls.todoLista:
            cls.todoLista.remove(todo)
            return True
        return False