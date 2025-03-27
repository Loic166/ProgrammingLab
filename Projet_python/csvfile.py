# Esercizio 1
# Create un oggetto CSVFile che rappresenti un file CSV, e che:
# 1) venga inizializzato sul nome del file csv, e
# 2) abbia un attributo “name” che ne contenga il nome
# 3) abbia un metodo “get_data()” che torni i dati dal file CSV come lista di liste, 
# ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]


class CSVFile:
    def __init__(self, file_name):
        self.name = file_name

    def get_data(self):
        try:
            my_file = open(self.name, 'r')
            lista_dati = []
            for item in my_file:
             
                item = item.strip().split(',')
                if item[0] != 'Date':
                    data = item[0]
                    valore = item[1]
                    lista_dati.append([data,valore])
        except:
            raise Exception('Errore: il file non esiste.')
        return lista_dati 
    


# Esercizio 2
# Estendete l’oggetto CSVFile chiamandolo NumericalCSVFile e facendo in modo che 
# converta automaticamente a numero float tutte le colonne tranne la prima (della data). 
# Chiamate la get_data originale con super().get_data(), poi converite tutto a float

class NumericalCSVFile(CSVFile):
    def __init__(self, file_name):
        super().__init__(file_name)
    def get_data(self):
        lista_valori = super().get_data()
        for element in lista_valori:
            try:
                element[1] = float(element[1])
            except:
                raise Exception('Errore: Impossibile {element[1]} convertire in float ')
                
        return lista_valori
    
# mov = CSVFile('/workspaces/ProgramingLab/Projet_python/shampoo_sales.csv')
# mov_res = mov.get_data()
# print(mov_res)

    
# mov = NumericalCSVFile('/workspaces/ProgramingLab/Projet_python/shampoo_sales.csv')
# mov_res = mov.get_data()
# print(mov_res)


 