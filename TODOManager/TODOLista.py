
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
    def GetTODO(cls, numero): # Palauttaa tietyn tehtävän todoListasta
        return cls.todoLista[numero]
    @classmethod
    def GetNextID(cls): # Palauttaa seuraavan ID:n
        return int(len(cls.todoLista))