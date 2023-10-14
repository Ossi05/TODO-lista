from TODOManager.TODOLista import TODO
from datetime import datetime

def LisaaTODO(otsikko: str, kuvaus: str, maarapaiva: str):
    ID = TODO.GetNextID()
    luotu = datetime.now().strftime("%d.%m.%Y")
    onSuoritettu = False
    todo = TODO(ID, otsikko, kuvaus, luotu, maarapaiva, onSuoritettu)
    TODO.LisaaTODOListaan(todo)