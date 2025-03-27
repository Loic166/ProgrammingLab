class ExamExeption(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self,name):
        self.name = name
        # Verifico il file sia apribile o leggibile
        try:
            my_file = open(self.name)
            contenuto = my_file.read()
            my_file.close()
        # Se non lo è alzo un'eccezione
        except:
            raise ExamExeption("Errore: Impossibile aprire il file.")
        
    def get_data(self):
        # Apro il file
        my_file = open(self.name)
        # Inizializzo una lista per memorizzare il risultato
        time_series = []
        for linea in my_file:
            # divido le righe del file per il ","
            linea = linea.strip().split(',')
            # Salto l'intestazione del file
            if linea[0] != "dt":
                data = linea[0]
                # Mi assicuro che le temperature sono di titpo float
                try:
                    temperatura = float(linea[1])
                except:
                    continue
            # Aggiungo a lista_result la sottolista [data,temperatura]
                time_series.append([data,temperatura])
        
        return time_series
    
def compute_variations(time_series, first_year, last_year, N):
    # Verifico che N sia un numero intero maggiore stretto di zero(0) 
    # e minore stretto della lunghezza dell'intervallo
    if N < 0 or N > (last_year-first_year) :
        raise ExamExeption("Errore: la lunghezza della finestra deve essere un intero positivo minore della lunghezza della finestra.")
    if not isinstance(N, int):
        raise ExamExeption("Errore: la lunghezza della finestra deve essere un intero positivo.")
    
    # Inizializzo un dizionare per raggruppare i dati per anno, per gli anni dell’intervallo
    diz_dati = {}
    for element in range(first_year, last_year+1):
        for item in time_series:
            try:
                data = item[0].split('-')
                anno = int(data[0])
                
                # Verifico che l'anno corrente sia nell'intervallo
                if element == anno:
                    temperatura = item[1]
                    # Verifico se l'anno corrente sia gia nel dizionare
                    if not anno in diz_dati.keys():
                        # Se non lo è lo aggiungo come chiave e inizializzo una lista vuota per raggruppare 
                        # le sue temperature associate
                        diz_dati[anno] = []
                    diz_dati[anno].append(temperatura)

            except:
                continue
    
    # Inizializzo un dizionare per mraggruppare i dati per anno-media_annuale
    diz_medie = {}
    for item in diz_dati.keys():
        media = sum(diz_dati[item])/len(diz_dati[item])
        diz_medie[item] = media
    
    # Inizializzo il dizionario che memorizzera il risultato
    diz_result = {}
    for anno in diz_medie.keys():
        chiave = str(anno)
        valore = diz_medie[anno]
        # • Calcolare la differenza tra la temperatura media annuale e la media dei N anni precedenti
        for i in range(N):
            # Provo a fare la differenza tra la temperatura media annuale e la media dei N anni precedenti
            try:
                valore -= diz_medie[anno -i -1]/N
            # Se non riesco procedo communque senza alzare eccezioni
            except:
                continue
        diz_result[chiave] = valore

    return diz_result


# Aggiungere una funzione che, dato un intervallo di temperatura, mi calcola gli anni che hanno
# almeno un mese con un valore fuori dall’intervallo. Considerare le eccezioni per l’inserimento
# sbagliato degli estremi dell’intervallo.

# def lode(time_series, first_temperatura, last_temperatura):

#     # Controllo l'inserimento degli estremi dell'intervallo
#     if first_temperatura < 8.11 or last_temperatura > 11.89:



mov = CSVTimeSeriesFile('/workspaces/ProgramingLab/Projet_python/GlobalTemperatures.csv')
mov_get = mov.get_data()
val = compute_variations(mov_get,1900,1905,3)
print(val)
# print(mov_get)

# import os

# # Chemin du fichier
# file_path = '/workspaces/ProgramingLab/Dom_23_01_2024.py'

# # Obtenir le répertoire du fichier
# directory = os.path.dirname(file_path)

# print(f"Le répertoire du fichier est : {directory}")