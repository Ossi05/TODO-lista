from TODOManager.TODOLista import TODO

with open("toDoLista.txt", "w", encoding="utf-8") as file:
    x = input("Mitä merkataan listaan?: ")
    file.write(x)

    # TulostaTODO on tallentanu kaikki tehtävät listaan
    # Tee joku for loop joka käy läpi kaikki tehtävät 
    # todoLista = TODO.GetTODOLista()
   # esim for todo in TODOLista:
             
        # Tällä tavaalla saat ero tietoja todo tehtävästä
        # todo.otsikko
        # todo.kuvaus
        # todo.luotuPaivamaara
        # todo.maarapaiva
        # todo.onSuoritettu
        # todo.ID
        
    # Mun scripti voi olla vähän sekavaa, mutta kato sitä TODOLista.py tiedostoa
    # Kirjotetaan jossain vaihees selkeempi koodi
    