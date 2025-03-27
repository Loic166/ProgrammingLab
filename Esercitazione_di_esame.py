# Eso 1
class ExamException(Exception):
    pass

class MovingAverage():

    def __init__(self,lunghezza_finsetra):
        self.lunghezza = lunghezza_finsetra
        if self.lunghezza < 1:
            raise ExamException('Errore,La lunghezza della finestra deve essere un intero maggiore di 0.')

    def compute(self,lista):
        if len(lista) < self.lunghezza:
            raise ExamException ('Errore,la lunghezza della finestra deve essere minore o uguale alla dimensione della lista.')
        
        list_media = []
        try:
            for i in range(len(lista)-1):

                try:
                    if self.lunghezza == len(lista[i:i+self.lunghezza]):
                        somma = sum(lista[i:i+self.lunghezza])
                        media = somma/len(lista[i:i+self.lunghezza])
                        list_media.append(media)
                    
                    else:
                        return list_media
                
                except:
                    raise ExamException('Errore,i valori della lista devono essere i numeri.')
            return list_media   
        except:
            raise ExamException('Errore, La lista inserita è vuota.')
        
mov = MovingAverage(1)
list_mov = mov.compute([2,4,8,16,'r'])

print(list_mov)
                



        

#------------------------------------------------------------#

#Eso 2