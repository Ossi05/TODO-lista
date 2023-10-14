import re
from TODOManager import TODOLista

# ////////////////////////////////////////////////////////////////////
# Lukee to-do.txt tekstitiedoston main.py alussa                   //
#  lisää tekstitiedoston to-do tehtävät TODOLista.py listaan      //
# /////////////////////////////////////////////////////////////////


def LueTODO():

    TODO = TODOLista.TODO
    riviLista = []
    kuvaus = ""
    onKuvaus = False
    id = 0

    with open("ToDoLista.txt", "r", encoding="utf-8") as Tiedosto:
        for rivi in Tiedosto:
            rivi = rivi.strip()
            if rivi == "" and not riviLista: # Jos rivi on tyhjä, jatka
                continue
            
            if rivi.startswith("Lisätietoa:"): # Jos rivi alkaa Lisätietoa: sanalla
                onKuvaus = True
                continue
            
            if onKuvaus and not rivi.endswith("Tehty"): # Jos onKuvaus ja rivi ei lopu Tehty sanaan
                if len(rivi) == 0 or rivi.isspace(): # Jos rivi on tyhjä, jatka
                    continue 
                kuvaus += rivi + "\n" # Lisää rivi kuvaus muuttujaan
                continue
            elif rivi.endswith("Tehty"): # Jos rivi loppuu Tehty sanaan
                onKuvaus = False
                kuvaus = kuvaus[:-1] # Poista viimeinen rivinvaihto
                riviLista.append(kuvaus) # Lisää kuvaus riviListaan
                kuvaus = "" # Tyhjennä kuvaus muuttuja

            riviLista.append(rivi) # Lisää rivi riviListaan
            if rivi.endswith("Tekemättä"): # Tarkista löytyykö Tekemättä sanaa rivin lopusta
                paivamaarat = re.findall(r'\d{2}.\d{2}.\d{4}', riviLista[0]) # Hae päivämäärät otsikosta
                riviLista[0] = riviLista[0].split(paivamaarat[0])[0] # Poista päivämäärät otiskosta
                onSuoritettu = True
                if (rivi.find("X") != -1): # Tarkista löytyykö X merkkiä Tekemättä kohdasta (Tehtävää ei suoritettu)
                    onSuoritettu = False

                if (rivi.endswith("Tekemättä")): # Tarkista löytyykö Tekemättä sanaa rivin lopusta
                    todo = TODO(id, riviLista[0], riviLista[1], paivamaarat[0], paivamaarat[1], onSuoritettu)
                    TODO.LisaaTODOListaan(todo)
                id += 1
                riviLista.clear() # Tyhjennä riviLista

