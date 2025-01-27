#Eso 5: Definire una funzione che prende come input un file, rimuove tutte le righe duplicate, 
# scrive il risultato in un nuovo file chiamato unique.txt.

def rimuovi_duplicati(file_name):
    list = []
    try:
        with open(file_name, 'r') as file:
            list_righe = file.readlines()

        for item in list_righe:
            #item = item.strip()

            if item not in list:
                list.append(item)
        return list
        with open('/workspaces/ProgramingLab/Projet_python/unique.txt','w') as file:
            for element in list:
                file.write(element)

    except:
        return "Il file non esiste."
    
print(rimuovi_duplicati('/workspaces/ProgramingLab/Projet_python/zeebaby.txt'))