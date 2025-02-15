class Model():
    def fit(self, data):
        return sum(data)
    # Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
    # Predict non implementanto nella classe base

class  TrendModel(Model):
    def predict(self,lista):
      
        if not isinstance(lista, list):
            return f"{lista} non è tipo <list>"
        predict = 0
        for i in range(len(lista)-1):
            try:
                predict += lista[i+1] - lista[i]
            except:
                raise ('Errore, C')
        predict = lista[-1] + predict/len(lista[1::])
        return predict
# mov = TrendModel()
# a = [50,52,60]
# mov_data = mov.predict(a)
# print(mov_data)
# print(mov_data
with open('/workspaces/ProgramingLab/Modello_python.py', 'r') as file:
    lista = []
    file_dest = open('go.py', 'w')
    
    my_file = file.readlines()
    for line in my_file:
        if not line in lista:
            lista.append(line)
            file_dest.write(line)
        #print (line)
    file_dest.close()
   # print(lista)