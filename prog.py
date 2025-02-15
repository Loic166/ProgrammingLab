# #Eso 5: Definire una funzione che prende come input un file, rimuove tutte le righe duplicate, 
# # scrive il risultato in un nuovo file chiamato unique.txt.

# def rimuovi_duplicati(file_name):
#     list = []
#     try:
#         with open(file_name, 'r') as file:
#             list_righe = file.readlines()

#         for item in list_righe:
#             #item = item.strip()

#             if item not in list:
#                 list.append(item)
#         #return list
#         with open('/workspaces/ProgramingLab/Projet_python/unique.txt','w') as file:
#             for element in list:
#                 file.write(element)

#     except:
#         return "Il file non esiste."
    
# #rimuovi_duplicati('/workspaces/ProgramingLab/Projet_python/zeebaby.txt')


# # Definizione della classe ExamException
# class ExamException(Exception):
#     pass

# # Definizione della classe MovingAverage
# class MovingAverage:
#     def __init__(self, window_length):
#         if not isinstance(window_length, int) or window_length <= 0:
#             raise ExamException('Errore, la lunghezza della finestra deve essere un intero positivo')
#         self.window_length = window_length

#     def compute(self, values):
#         if not isinstance(values, list) or not all(isinstance(x, (int, float)) for x in values):
#             raise ExamException('Errore, la lista dei valori deve contenere solo numeri')
#         if len(values) < self.window_length:
#             raise ExamException('Errore, la lista dei valori è troppo corta per la lunghezza della finestra')

#         moving_averages = []
#         for i in range(len(values) - self.window_length + 1):
#             window = values[i:i + self.window_length]
#             window_average = sum(window) / self.window_length
#             moving_averages.append(window_average)

#         return moving_averages

# # Esempio di utilizzo della classe
# moving_average = MovingAverage(2)
# result = moving_average.compute([2, 4, 8, 16])
# print(result)  # Deve stampare a schermo [3.0, 6.0, 12.0]


b = [[1,2,2],1,2,3,4]
a = [1,2,3,4]
print([1,2,2] in b)