
# ////////////////////////////////////////////////////////////////////
# todoLista on tallennettu tänne                                   //
# LueTODO tiedosto lukee to-do.txt tiedoston                      //
# ja tallentaa tehtävät todoListaan                              //
# ////////////////////////////////////////////////////////////////


class TODO:

    todoLista = []

    def __init__(self, otsikko, kuvaus, luotuPaivamaara, maarapaiva, onSuoritettu):
        self.otsikko = otsikko
        self.kuvaus = kuvaus
        self.luotuPaivamaara = luotuPaivamaara
        self.maarapaiva = maarapaiva
        self.onSuoritettu = onSuoritettu

    @classmethod
    def LisaaTODOListaan(cls, toDo):
        cls.todoLista.append(toDo)
    
    @classmethod
    def GetTODOLista(cls):
        return cls.todoLista
    
    @classmethod
    def GetTODO(cls, numero):
        return cls.todoLista[numero]
