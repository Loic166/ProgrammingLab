# def conteggio(file_name):
    
#     # Provo ad Aprire il file
#     try:
#         my_file = open(file_name, 'r')
#     # Se riesco ad aprirlo lo leggo
#         contenuto = my_file.read()
#         my_file.close()
#     # Se non riesco ad aprire il file alzo un'eccezione
#     except Exception as e:
#         raise Exception(f"{e}")
    
#     # sostituisco i punti "!" e "?" con "."
#     contenuto = contenuto.replace('!', '.').replace('?', '.')
#     # Divido gli elementi di contenuto per un punto per ottenere ogni frase del testo
#     contenuto = contenuto.strip().split('.')
    
#     # Inizializzo un dizionario  vuoto
#     diz = {}
#     for frase in contenuto:
#         # Divido ogni frase per parola
#         words = frase.strip().split()
#         # verifico frasi vuote
#         if words != []:
#             # Controllo che la prima parola di una frase non sia gia nel dizionario
#             if words[0] not in diz.keys():
#                 # Se non lo è inizializzo il contatore a zero(0)
#                 diz[words[0]] = 0
#             # Se lo è aggiorno il contatore di uno (1) 
#             diz[words[0]] += 1

#     return diz

# def rimove_duplicati(file_name):
#     # Provo ad aprire il file
#     try:
#         # Se riesco lo leggo
#         my_file = open(file_name, 'r')
  
#     except Exception as e:
#         raise Exception(f"{e}")
#     #
#     new_file = open('unique.txt', 'w')
#     lista = []
#     for riga in my_file:
#         if riga not in lista:
#             lista.append(riga)
#     for item in lista:
#         new_file.write(item)
#     my_file.close()

# p = rimove_duplicati('/workspaces/ProgramingLab/Projet_python/loic.txt')

def lettera_init(file_name):
    my_file = open(file_name, 'r')
    contenuto = my_file.read()
    words = contenuto.strip().split()
    diz = {}
    for word in words:
        lettera = word[0].lower()
        if lettera not in diz.keys() or len(diz[lettera]) < len(word):
            diz[lettera] = word
    
    return diz

# b= lettera_init('/workspaces/ProgramingLab/unique.txt')
# print(b)

def longest_words_by_initial(file_path):
    # Inizializza un dizionario vuoto per memorizzare il risultato
    result = {}

    # Leggi il contenuto del file
    with open(file_path, 'r') as file:
        content = file.read()

    # Dividi il contenuto in parole
    words = content.split()

    # Itera su ogni parola
    for word in words:
        # Ottieni la lettera iniziale della parola
        initial = word[0].lower()

        # Se la lettera iniziale non è nel dizionario o la parola corrente è più lunga della parola memorizzata
        if initial not in result or len(word) > len(result[initial]):
            # Aggiorna il dizionario con la parola corrente
            result[initial] = word

    return result

# # Esempio di utilizzo
# file_path = '/workspaces/ProgramingLab/unique.txt'
# print(longest_words_by_initial(file_path))

import os

# Chemin du fichier
file_path = '/workspaces/ProgramingLab/Dom_23_01_2024.py'

# Obtenir le répertoire du fichier
directory = os.path.dirname(file_path)

print(f"Le répertoire du fichier est : {directory}")

