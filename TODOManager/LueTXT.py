import re
from TODOManager import TODOLista

# ////////////////////////////////////////////////////////////////////
# Lukee to-do.txt tekstitiedoston main.py alussa                   //
#  lisää tekstitiedoston to-do tehtävät TODOLista.py listaan      //
# /////////////////////////////////////////////////////////////////


def LueTODO():

    TODO = TODOLista.TODO
    riviLista = []
    id = 0

    with open("ToDoLista.txt", "r", encoding="utf-8") as Tiedosto:
        for rivi in Tiedosto:
            rivi = rivi.strip()
            if rivi == "" and not riviLista: # Jos rivi on tyhjä, jatka
                continue

            riviLista.append(rivi)
            if rivi.endswith("Tekemättä"): # Tarkista löytyykö Tekemättä sanaa rivin lopusta
                paivamaarat = re.findall(r'\d{2}.\d{2}.\d{4}', riviLista[0]) # Hae päivämäärät otsikosta
                riviLista[0] = riviLista[0].split(paivamaarat[0])[0] # Poista päivämäärät otiskosta
                onSuoritettu = True
                if (rivi.find("X") != -1): # Tarkista löytyykö X merkkiä Tekemättä kohdasta (Tehtävää ei suoritettu)
                    onSuoritettu = False

                if (rivi.endswith("Tekemättä")): # Tarkista löytyykö Tekemättä sanaa rivin lopusta
                    todo = TODO(id, riviLista[0], riviLista[2], paivamaarat[0], paivamaarat[1], onSuoritettu)
                    TODO.LisaaTODOListaan(todo)
                id += 1
                riviLista.clear() # Tyhjennä riviLista

