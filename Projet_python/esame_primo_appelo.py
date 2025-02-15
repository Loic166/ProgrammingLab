class ExamException(Exception):
    pass

class  CSVTimeSeriesFile:
    def __init__(self,file_name):
        self.name = file_name
        
    def get_data(self):
        my_file = open(self.name, 'r')
        lista_annidate = []
        for linea in my_file:
            linea = linea.strip().split(',')
            if linea[0] != 'Date':
                data = linea[0]
                valore = float(linea[1])
                lista_annidate.append([data,valore])
        return lista_annidate
        
mov = CSVTimeSeriesFile('/workspaces/ProgramingLab/Projet_python/shampoo_sales.csv')
mov_get = mov.get_data()
print(mov_get)

class Delmas:
    def __init__(self, age, force):
        self.age = age
        self.force = force

    def __str__(self):
        return f"DElmas :age = {self.age}, force = {self.force}"
    
# moi = Delmas(45, 0.0000)
# print(moi)
        
