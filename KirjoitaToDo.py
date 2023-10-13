with open("toDoLista.txt", "w", encoding="utf-8") as file:
    x = input("Mitä merkataan listaan?: ")
    file.write(x)
