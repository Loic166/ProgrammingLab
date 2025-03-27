class ExamException(Exception):
    pass

class MovingAverage:
    def __init__(self,lunghezza_finestra):
        # inizializzo la classe con la lughezza della finestra
        self.lunghezza = lunghezza_finestra
        # Verifico che la lunghezza della finestra sia un intero positivo, se non lo è alzo un eccezione.
        if not isinstance(self.lunghezza, int):
            raise ExamException("Errore: la lunghezza della finestra deve essere un intero maggiore stretto di zero(0)")

        if self.lunghezza <= 0:
            raise ExamException("Errore: la lunghezza della finestra deve essere un intero maggiore stretto di zero(0)")
        
    def copmute(self,lista):
        # Verifico che la lista non sia vuota
        # se lo è alzo un eccezione
        
        # inizializzo una lista vuota che memorisera il risultato de la media mobile
        medie_mobile = []
        for item in lista:
            if not isinstance(item, int):
                raise ExamException(f"Errore: il valore <{item}> non è tipo <int> ma di tipo {type(item)}")

        for i in range(len(lista)-1):
            
            if self.lunghezza == len(lista[i:i+self.lunghezza]):
                med = sum(lista[i:i+self.lunghezza])/self.lunghezza
                medie_mobile.append(med)
            
        return medie_mobile
    
mov = MovingAverage(2)
mov_res = mov.copmute([2,4,8,16])
print(mov_res)

b = [n for n in mov_res if n%2 == 0]
print(b)


