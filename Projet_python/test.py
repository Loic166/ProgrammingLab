import csv

# Definizione della classe ExamException
class ExamException(Exception):
    pass

# Definizione della classe CSVTimeSeriesFile
class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name

    def get_data(self):
        try:
            with open(self.name, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Salta l'intestazione
                data = []
                for row in reader:
                    try:
                        date = row[0]
                        passengers = int(row[1])
                        data.append([date, passengers])
                    except ValueError:
                        raise ExamException('Errore, dati non validi nel file')
            return data
        except FileNotFoundError:
            raise ExamException('Errore, file non trovato')
        except Exception as e:
            raise ExamException(f'Errore durante la lettura del file: {e}')

# Funzione per calcolare la differenza media dei passeggeri tra anni consecutivi
def compute_avg_passenger_difference(time_series, start_year, end_year):
    yearly_data = {}
    for date, passengers in time_series:
        year = int(date.split('-')[0])
        if start_year <= year <= end_year:
            if year not in yearly_data:
                yearly_data[year] = []    
            yearly_data[year].append(passengers)
    
    yearly_averages = {}
    for year in range(start_year, end_year + 1):
        if year in yearly_data:
            yearly_averages[year] = sum(yearly_data[year]) / len(yearly_data[year])
        else:
            raise ExamException(f'Errore, dati mancanti per l\'anno {year}')

    #differences = []
    for year in range(start_year + 1, end_year + 1):
        #differences.append([year,yearly_averages[year] - yearly_averages[year - 1]])
        yearly_averages[year] = year,yearly_averages[year] - yearly_averages[year - 1]

    return yearly_averages

# Esempio di utilizzo della classe e della funzione
time_series_file = CSVTimeSeriesFile('/workspaces/ProgramingLab/Projet_python/sales.csv')
time_series = time_series_file.get_data()
differences = compute_avg_passenger_difference(time_series, 1949, 1955)
print(differences)  # Deve stampare a schermo le differenze medie tra gli anni
