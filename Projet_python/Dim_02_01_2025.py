class ExamException(Exception):
    pass

# Creo la classe CSVTimeSeriesFile
class CSVTimeSeriesFile:
    def __init__(self,file_name):
        self.name = file_name

    def get_data(self):
        # Verifico che il file sia apribile
        try:
            my_file = open(self.name, 'r')
        # Se non lo è, alzo un eccezione
        except:
            raise ExamException('Errore,Impossibile aprire il file.')
        # Creo la lista times_series
        times_series = []
        for line in my_file:
            line = line.strip().split(',')
            if line[0] != 'date':
                data = line[0]
                # Provo a convertire un numeri di passegeri in interi
                try:
                    num_pass = int(line[1])
                    if num_pass <= 0:
                        print('Errore,numero negativo riga: "{}"'.format(line))
                        continue
                # Se non posso, la riga viene ignorata
                except:
                    print('Errore, Impossibile convertire "{}" in <int> '.format(line[1]))
                    continue
                # verifico se ci siano righe duplicate, se si queste righe vengono ignorate
                if not [data,num_pass] in times_series:
                    times_series.append([data,num_pass])
                   
                else:
                    print('Riga duplicata: "{}" '.format([data,num_pass]))
                    continue
        # for element in times_series:
        #     element[0] = element[0][0]
      
        return times_series
    

def  compute_variations(time_series, first_year, last_year):
    first_year = int(first_year)
    last_year = int(last_year)
    diz = {}
    for i in range(first_year,last_year+1):

        for item in time_series:
            data = item[0].split('-')
            anno = int(data[0])
            if i == anno:
                if not anno in diz.keys():
                    diz[anno] = []
                diz[anno].append(item[1])
    list_medie = []
    for item in diz.keys():
        media = sum(diz[item])/len(diz[item])
        list_medie.append([item,media])
    diz_finale = {}
    for i in range(len(list_medie)-1):
        chiave = str(list_medie[i][0]) + '-' + str(list_medie[i+1][0])
        valore = list_medie[i+1][1] - list_medie[i][1]
        diz_finale[chiave] = valore
    return diz_finale


mov = CSVTimeSeriesFile('/workspaces/ProgramingLab/Projet_python/data.csv')
m = mov.get_data()
diz = compute_variations(m,1949,1958)
print(diz)