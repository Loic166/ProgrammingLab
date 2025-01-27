# Eso 1

def media(lista):
    tot = 0
    for i in range(len(lista)):
        tot += lista[i]
    return tot/len(lista)  

class MovingAverage():

    def __init__(self,lunghezza):
        self.lunghezza = lunghezza

    def compute(self,lista):
        list = []
        for i in range(len(lista)):
            list.append(media(lista[i:self.lunghezza+i]))
            
        return list[:-1]

mov = MovingAverage(2)
tot = mov.compute([2,4,8,16])
print(tot)