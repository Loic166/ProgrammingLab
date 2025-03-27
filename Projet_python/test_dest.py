import unittest
# from dest import somma
# class Testsomma(unittest.TestCase):
#     def test_somma(self):
#         self.assertEqual(somma(1,2),3)
#         self.assertEqual(somma(0,0),0)
#         self.assertEqual(somma(1.5,2.5),4)

# Esercizio
# Scrivete dei test o unit test (a seconda di cosa più vi aggrada) per gli
# oggetti CSVFile e NumericalCSVFile.
# Potete per esempio:
# - creare vari file di test e verificare che la funzione get data dia sempre 
# l’output che vi aspettate
# - verificare che il nome del file sia salvato come attributo
# - verificare che vengano alzate specifiche eccezioni
# (usare il costrutto try-except o self.assertRaises() se si usa il modulo unittest)

from csvfile import CSVFile

class TestCSVFile:

    def setup(self):
        #diamo un nome arbitrario a un file contemporaneo
        self.file_name = 'file.csv'
        # Creamo un file contemporaneo per i test
        self.file = open('self.file_name', 'w')
        self.file.write("Date,valore\n2024-01,111\n2024-02,124\n2024-03,101\n")

    def test_attributo(self):
        #Instanziamo la classe CSVFile
        ogetto = CSVFile(self.file_name)
        self.assertEqual(ogetto.name, self.file_name)




