# Eso 0: Scrivete una funzione sum_csv(file_name)
# che sommi tutti i valori delle vendite degli
# shampoo del file passato come argomento

import csv
def sum_csv(file_name):
    tot = 0
    try:
        with open(file_name, 'r') as file:
            lettura = csv.reader(file)
            next(lettura)
            for value in lettura:
                tot += float(value[1])
        return tot
    except:
        return "Il file non esiste."
    
#print(sum_csv('Projet_python/shampoo_sales.csv'))

# ------------------------------------------------------- #
# Eso 1:  Definire una funzione che prende in input un file ed una parola e conta quante volte 
# quella parola è presente sul file

def conta_parola(file_name, parola):
    count = 0
    try:
        with open(file_name, 'r') as my_file:
            cont = my_file.read()
            list_parole = cont.split()
            for i in range(len(list_parole)):
                if list_parole[i] == parola:
                    count += 1
            return count
    except:
        return "Il file non esiste."
    
#print(conta_parola('/workspaces/ProgramingLab/Projet_python/Eso_python.py','#Eso'))

# --------------------------------------------------------- #
# Eso 2: Definire una funzione che prende come input un file e conta quante volte ogni parola è
# presente


def diz_parole(file):
    diz = {}
    try:
        with open(file, 'r') as my_file:
            cont = my_file.read()
            list_parole = cont.split()
            for i in range(len(list_parole)):
                if list_parole[i] in diz.keys():
                    diz[list_parole[i]] += 1
                else:
                    diz[list_parole[i]] = 1
            
            return diz
    except:
        return "Il file non esiste."

# print(diz_parole('/workspaces/ProgramingLab/Projet_python/zeebaby.txt'))

# -------------------------------------------------------- #

# Eso 3:  Definire una funzione che prende in input un file e costruisce un dizionario con chiavi la 
# lettere iniziali e con valore le parole di lunghezza maggiore contenute nel file che
# iniziano con quelle lettere. 

def diz_lettere(file_name):
    dizio = {}
    try:
        with open(file_name, 'r') as file:
            my_file = file.read()
            list_parole = my_file.split()
            for item in list_parole:
                if len(item) > 1:
                    dizio[item[0]] = item
            return dizio
    
    except:
        return "Il file non esiste."
    
#print(diz_lettere('/workspaces/ProgramingLab/Loic.py'))

# -------------------------------------------------------- #

# Eso 4: Definire una funzione conteggio che prende come input un file e ritorna un dizionario
# con chiave la prima parola di ogni frase e valore il numero di volte che una frase inizia
# con quella parola. Considerare come inizio di frase qualsiasi parola che segue un 
# punto, un punto esclamativo, un punto interrogativo o si trova all'inizio del testo.



import re
def contegio(file_name):
    diz = {}
    list = []

    try:
        #leggo il file
        with open(file_name, 'r') as file:
            testo = file.read()
            list_frase = re.split(r'[.!?]',testo)
            #list_parole = list_frase.split()
        #creo una lista di frase del testo   
            for element in list_frase:
                list.append(element.split())
        #riempio il dizionare  
            for item in list:
                if item:
                    if item[0] in diz.keys():
                        diz[item[0]] += 1
                    else:
                         diz[item[0]] = 1
       
            return diz
    except:
        return " Il file non esiste."
 
# pop = contegio('/workspaces/ProgramingLab/Projet_python/Eso_python.py')
# print(pop)

#--------------------------------------------------------#

#Eso 5: Definire una funzione che prende come input un file, rimuove tutte le righe duplicate, 
# scrive il risultato in un nuovo file chiamato unique.txt.

def occ(lista,element):
    tot = 0
    for i in range(len(lista)):
        if element == lista[i]:
            tot += 1
    return tot


def remove_duplicati(file_name):
    list_righe = []
    try:
        my_file = open(file_name, 'r')
        contenuto = my_file.readlines()
        my_file.close()
        for item in contenuto:
            item = item.strip()
            
            if item not in list_righe:
                list_righe.append(item)
        #return list_righe
        #list_righe = ' '.join(list_righe)
        #return list_righe
        with open('/workspaces/ProgramingLab/Projet_python/unique.txt','w') as file:
            for riga in list_righe:
                file.write(riga)
            
    except:
        return "Il file non esiste."

#remove_duplicati('/workspaces/ProgramingLab/Projet_python/zeebaby.txt')

def rimuovi_duplicato(file_name):

    # Leggo riga per riga 
    with open(file_name, 'r') as file:
        lista_righe = file.readlines()
    
    # Inizializzo una lista vuota che conterrà le righe già viste
    righe = []
    for riga in lista_righe:
        # Se la riga attuale non è nella lista della righe già viste
        if riga not in righe:
            # Aggiungo la riga alla list
            righe.append(riga)
            
    # Scrivo su un file le righe uniche
    with open('/workspaces/ProgramingLab/Projet_python/unique.txt', 'w') as file_unique:
        for riga in righe:
            file_unique.write(riga)

#rimuovi_duplicato('/workspaces/ProgramingLab/Projet_python/zeebaby.txt')

#--------------------------------------------------------------------#

# Esercizio 1
# Create un oggetto CSVFile che rappresenti un file CSV, e che:
# 1) venga inizializzato sul nome del file csv, e
# 2) abbia un attributo “name” che ne contenga il nome
# 3) abbia un metodo “get_data()” che torni i dati dal file CSV come lista di liste, 
# ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]

import csv
class CSVFile():

    
    def __init__(self,file_name):
        self.name = file_name
        with open(self.name, 'r') as file:
                
            try:
                cont = csv.reader(file)
                cont = cont
            
            except:
                return f"Error: Il file {self.name} non è stato trovato."

    def get_data(self):
        try:
            list_dati = []
            with open(self.name, 'r') as file:
                contenuto = csv.reader(file)

                next(contenuto)
                for data in contenuto:
                    list_dati.append(data)

            return list_dati
        except:
            return f"Error: Il file {self.name} non è stato trovato."
        
# sales = CSVFile('/workspaces/ProgramingLab/Projet_python/shampoo_sales.csv')
# sales.name = '/workspaces/ProgramingLab/Projet_python/shampoo_sales.csv'
# list = sales.get_data()
# print(sales)        

#----------------------------------------------------------------------#

# Esercizio (b
# Estendete l’oggetto CSVFile chiamandolo NumericalCSVFile e facendo in modo che 
# converta automaticamente a numero float tutte le colonne tranne la prima (della data). 
# Chiamate la get_data originale con super().get_data(), poi converite tutto a float

class NumericalCSVFile(CSVFile):

    def __init__(self, file_name):
        super().__init__(file_name)
    
    def get_data(self):
        data = super().get_data()
        data_cort = []
        
        for element in data:
           
            try:
                element[1] = float(element[1])
                data_cort.append(element)

            except Exception as e:
               print(f"Errore: {e}")
               data_cort.append(element)
        return data_cort
       
sales = NumericalCSVFile('/workspaces/ProgramingLab/Projet_python/sales.csv')
#sales.name = '/workspaces/ProgramingLab/Projet_python/shampoo_sales.csv'
list = sales.get_data()
print(list)         



#---------------------------------------------------------------#

# Esercizio 2: Classe Veicolo
# Scrivete una classe denominata Veicolo che disponga di questi attributi dati:
# ● modello (per il modello del veicolo);
# ● marca (per la marca del veicolo);
# ● anno (per l'anno del veicolo).
# ● speed (per la velocità del veicolo)
# E di questi metodi:
# ● __init__ che accetti come argomenti l’anno, il modello, e la marca. Il metodo dovrebbe inoltre
# assegnare 0 all’attributo dati speed.
# ● __str__ che restituisce una stringa con i dettagli del veicolo (marca, modello, anno e velocità)
# ● accellerare che aggiunge 5 all’attributo dati speed ogni volta che viene chiamato.
# ● frenare che sottrae 5 dall’attributo dati speed ogni volta che viene chiamato.
# ● get_speed che restituisce la velocità corrente.


class Veicolo():

    def __init__(self,anno,modello,marca):

        self.anno = anno
        self.modello = modello
        self.marca = marca
        self.speed = 0

    def accelerare(self):
        self.speed += 5
    
    def frenare(self):
       
       if self.speed >= 5:
           self.speed -= 5
        # else:
        #    self.speed = 0

    def __str__(self):
        #print("marca: {} , modello: {} , anno: {} , velocità: {} km/h ".format(self.marca,self.modello,self.anno,self.speed,self.speed + 5))
        return f"marca: {self.marca} , modello: {self.modello} , anno: {self.anno} , velocità: {self.speed} " 

    def get_speed(self):
        return self.speed
    
# veicolo = Veicolo(1916,'i3s', 'BMW')   

# veicolo.speed = 1000
# veicolo.accelerare()
# print(veicolo)

# print(veicolo.get_speed())

#-----------------------------------------------------------#

# Esercizio 3
# ● Crea una sottoclasse auto che ha in aggiunta l'attributo numero_porte e 
# cambia il metodo _str__ di conseguenza
# ● Crea una sottoclasse moto che ha in aggiunta l'attributo tipo (ad esempio, 
# "Sportiva" o "Touring") e cambia il metodo _str__ di conseguenza      

class Auto(Veicolo):
    
    def __init__(self,anno,modello,marca,numero_porte):
        super().__init__(anno,modello,marca)
        self.numero_porte = numero_porte

    def __str__(self):
        return f"marca: {self.marca} , modello: {self.modello} , anno: {self.anno} , velocità: {self.speed} , numero_porte: {self.numero_porte}" 


class Moto(Veicolo):

    def __init__(self,anno,modello,marca,tipo):
        super().__init__(anno,modello,marca)
        self.tipo = tipo

    def __str__(self):
        return f"marca: {self.marca} , modello: {self.modello} , anno: {self.anno} , velocità: {self.speed} , tipo: {self.tipo}" 
    
# auto = Auto(1916,'i3s', 'BMW',4)
# print(auto)

