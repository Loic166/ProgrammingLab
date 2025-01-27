# import csv

# with open('/workspaces/ProgramingLab/Projet_python/shampoo_sales.csv', mode='r') as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row)


import csv

# def sum_csv(file_name):
#     total_sales = 0.0
#     try:
#         with open(file_name, 'r') as file:
#             csv_reader = csv.reader(file)
#             next(csv_reader)  # Salta l'intestazione
#             for row in csv_reader:
#                 total_sales += float(row[1])  # Supponendo che i valori delle vendite siano nella seconda colonna
#         return total_sales
#     except FileNotFoundError:
#         return "Il file non esiste."
#     except Exception as e:
#         return f"Si è verificato un errore: {str(e)}"
    
def affichichage(name):
    try:
        with open(name, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Salta l'intestazione
            for row in csv_reader:
                print(row[1])  # Supponendo che i valori delle vendite siano nella seconda colonna
    except FileNotFoundError:
        print("Il file non esiste.")
    except Exception as e:
        




def affich(name):
    try:
        with open(name, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Saute l'entête
            for row in csv_reader:
                print(row[1])  # En supposant que les valeurs des ventes soient dans la deuxième colonne
    except FileNotFoundError:
        print("Le fichier n'existe pas.")
    except Exception as e:
        print(f"Une erreur est survenue : {str(e)}")

# Exemple d'utilisation
affichichage('/workspaces/ProgramingLab/Projet_python/shampoo_sales.csv')

# Esempio di utilizzo

affichichage('/workspaces/ProgramingLab/Projet_python/shampoo_sales.csv')


# with open(file_name, 'r') as file:
#     print(file.read())
    

# print(csv.reader(file_name))
# print(file_name)
# print(sum_csv(file_name))