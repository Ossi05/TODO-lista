from TODOManager.TODOLista import TODO
from datetime import datetime

def LisaaTODO(otsikko: str, kuvaus: str, maarapaiva: str): # Lisää tehtävän todoListaan
    ID = TODO.GetNextID() # Hakee seuraavan ID:n
    luotu = datetime.now().strftime("%d.%m.%Y") # Hakee luomispäivämäärän
    onSuoritettu = False # Asettaa suoritetuksi false
    todo = TODO(ID, otsikko, kuvaus, luotu, maarapaiva, onSuoritettu) # Luo uuden tehtävän
    TODO.LisaaTODOListaan(todo) # Lisää tehtävän todoListaan