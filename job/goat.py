# Esercizio: Calcolo delle Variazioni Medie Mensili dei Prezzi di un Prodotto
# Obiettivo
# Implementare una classe in Python che legga un file CSV contenente i prezzi mensili di un prodotto e calcoli la variazione media mensile dei prezzi per ogni anno in un intervallo di anni fornito dall'utente.
# Il file CSV ha il seguente formato:
 
# data,prezzo

# 2018-01,100

# 2018-02,105

# 2018-03,103

# ...

# 2021-12,120

 
# Specifiche
# La classe CSVPricesFile deve essere in grado di leggere il file e restituire una lista di liste con i dati.
# Implementare una funzione compute_price_variations che prenda i dati, l'anno di inizio e l'anno di fine e calcoli la variazione media mensile dei prezzi per ciascun anno nel range fornito.
# La funzione deve restituire un dizionario con le variazioni medie mensili per ogni coppia di anni successivi nel formato { "anno1-anno2": variazione_media }.

class CSVPricesFile:

    def __init__(self,file_name):
        self.name = file_name

    def compute_price_variations(self,first_year,last_year):
        # try:
            my_file = open(self.name, 'r')
            diz_data_vend = {}
            for line in my_file:
                line = line.strip().split(',')
                if line[0] != 'date':
                    data = line[0].split('-')
                    anno = int(data[0])
                    vendite = int(line[1])
                if not anno in diz_data_vend.keys():
                    diz_data_vend[anno] = []
                diz_data_vend[anno].append(vendite)

            return diz_data_vend
mov = CSVPricesFile('/workspaces/ProgramingLab/Projet_python/data.csv')  
b = mov.compute_price_variations(3,3) 
print(b)
