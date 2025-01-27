# frasi = ["Bonjour", " ", "Salut", "  ", "Hello", "Bonjour"]
# dizionario = {}
# list = []
# for item in frasi:
#     item = item.strip()
#     if item not in list:
#         list.append(item)
# print(list)


# for f in frasi:
#     f = f.strip()
#     if f:  # Vérifie que la chaîne n'est pas vide
#         parola_iniziale = f.split()[0].lower()
#         if parola_iniziale not in dizionario.keys():
#             dizionario[parola_iniziale] = 1
#         else:
#             dizionario[parola_iniziale] += 1

# #print(dizionario)

# def occ(lista,element):
#     tot = 0
#     for i in range(len(lista)):
#         if element == lista[i]:
#             tot += 1
#     return tot

# #print(occ(frasi,'bonjour'))

# with open('/workspaces/ProgramingLab/Projet_python/zeebaby.txt','r') as file:
#     cont0 = file.read()


# my_file = open('/workspaces/ProgramingLab/Projet_python/unique.txt', 'w')
# #cont = my_file.read()

# my_file.write(cont0)

# my_file.close()

# def rimuovi_duplicati(file_input):
#     try:
#         with open(file_input, 'r') as file:
#             righe = file.readlines()
        
#         righe_uniche = list(set(righe))
        
#         with open('/workspaces/ProgramingLab/Projet_python/unique.txt', 'w') as file_output:
#             file_output.writelines(righe_uniche)
        
#         print("Le righe duplicate sono state rimosse e il risultato è stato scritto in 'unique.txt'.")
#     except FileNotFoundError:
#         print(f"Il file {file_input} non è stato trovato.")
#     except Exception as e:
#         print(f"Si è verificato un errore: {e}")

# # Esempio di utilizzo
# rimuovi_duplicati('/workspaces/ProgramingLab/Projet_python/zeebaby.txt')

# import csv

# class CSVFile:
#     def __init__(self, file_name):
#         self.name = file_name

#     def get_data(self):
#         data = []
#         try:
#             with open(self.name, 'r') as file:
#                 reader = csv.reader(file)
#                 next(reader)
#                 for row in reader:
#                     data.append(row)
#         except FileNotFoundError:
#             print(f"Il file {self.name} non è stato trovato.")
#         except Exception as e:
#             print(f"Si è verificato un errore: {e}")
#         return data

# # Esempio di utilizzo
# csv_file = CSVFile('/workspaces/ProgramingLab/Projet_python/shampoo_sales.csv')
# dati = csv_file.get_data()
# print(dati)


class Veicolo:
    def __init__(self, anno, modello, marca):
        self.anno = anno
        self.modello = modello
        self.marca = marca
        self.speed = 0

    def __str__(self):
        return f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Velocità: {self.speed} km/h"

    def accellerare(self):
        self.speed += 5

    def frenare(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def get_speed(self):
        return self.speed

class Auto(Veicolo):
    def __init__(self, anno, modello, marca, numero_porte):
        super().__init__(anno, modello, marca)
        self.numero_porte = numero_porte

    def __str__(self):
        return f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Velocità: {self.speed} km/h, Numero di porte: {self.numero_porte}"

class Moto(Veicolo):
    def __init__(self, anno, modello, marca, tipo):
        super().__init__(anno, modello, marca)
        self.tipo = tipo

    def __str__(self):
        return f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Velocità: {self.speed} km/h, Tipo: {self.tipo}"

# Esempio di utilizzo
auto = Auto(2022, "Model S", "Tesla", 4)
moto = Moto(2021, "Ninja", "Kawasaki", "Sportiva")

# print(auto)  # Output: Marca: Tesla, Modello: Model S, Anno: 2022, Velocità: 0 km/h, Numero di porte: 4
# print(moto)  # Output: Marca: Kawasaki, Modello: Ninja, Anno: 2021, Velocità: 0 km/h, Tipo: Sportiva


import csv

class CSVFile:
    def __init__(self, file_name):
        self.name = file_name

    def get_data(self):
        data = []
        try:
            with open(self.name, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"Il file {self.name} non è stato trovato.")
        except Exception as e:
            print(f"Si è verificato un errore: {e}")
        return data

class NumericalCSVFile(CSVFile):
    def get_data(self):
        data = super().get_data()
        numerical_data = []
        for row in data:
            try:
                new_row = [row[0]]  # Mantiene la prima colonna (data) come stringa

                for value in row[1:]:
                    new_row.append(float(value))
                numerical_data.append(new_row)
            except ValueError as e:
                print(f"Errore di conversione nella riga {row}: {e}")
        return numerical_data

# Esempio di utilizzo
# numerical_sales = NumericalCSVFile('/workspaces/ProgramingLab/Projet_python/sales.csv')
# dati_numerici = numerical_sales.get_data()
# print(dati_numerici)

def media(lista):
    tot = 0
    for i in range(len(lista)):
        tot += lista[i]

    return tot/len(lista)  

def compute(lista,lunghezza):
        list = []
        for i in range(len(lista)):
        
            list.append(media(lista[i:lunghezza+1]))
            
        return list

diz = [2,4,8,16]

diz0 = compute(diz,2)

print(diz0)


