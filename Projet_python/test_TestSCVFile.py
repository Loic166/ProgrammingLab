# Scrivete dei test o unit test (a seconda di cosa più vi aggrada) per gli
# oggetti CSVFile e NumericalCSVFile.
# Potete per esempio:
# - creare vari file di test e verificare che la funzione get data dia sempre 
# l’output che vi aspettate
# - verificare che il nome del file sia salvato come attributo
# - verificare che vengano alzate specifiche eccezioni
# (usare il costrutto try-except o self.assertRaises() se si usa il modulo unittest)

import unittest

from Projet_python.csvfile import NumericalCSVFile

class TestNumericalCSVFile(unittest.TestCase):

    def setUp(self):
        """Creamo un file contemporaneo"""
        self.file_name = "dati.csv"
        with open(self.file_name, 'w') as file:
            file.write("Date,valore\n01-05-2013,191.4\n01-07-2013,226.0\n01-12-2013,342\n01-12-2013,352.3\n")

    def test_attributo_nome(self):
        ogetto = NumericalCSVFile(self.file_name)
        self.assertEqual(ogetto.name, self.file_name)

    def test_output(self):
        ogetto = NumericalCSVFile(self.file_name)
        output_noto = [["01-05-2013",191.4],["01-07-2013",226.0],["01-12-2013",342],["01-12-2013",352.3]]
        self.assertEqual(ogetto.get_data(), output_noto)

    def test_output_is_float(self):
        # ogetto = NumericalCSVFile(self.file_name)
        output_noto = [["01-05-2013",191.4],["01-07-2013",226.0],["01-12-2013",342],["01-12-2013",352.3]]
        test = output_noto[0][1]
        self.assertIsInstance(test, float)

    def test_file_vuoto(self):
        self.file_vuoto = "data.csv"
        with open(self.file_vuoto, 'w')  as file:
            pass
        ogetto = NumericalCSVFile(self.file_vuoto)
        self.assertEqual(ogetto.get_data(), [])

    def test_eccezioni(self):
        self.file = "file_non_esistente.csv"
        ogetto = NumericalCSVFile(self.file)
        with self.assertRaises(FileExistsError):
            ogetto.get_data()

# import unittest
# from CSVFile import CSVFile, NumericalCSVFile

# class TestCSVFile(unittest.TestCase):

#     def setUp(self):
#         """ Crea un file di test temporaneo. """
#         self.test_filename = "test_data.csv"
#         with open(self.test_filename, "w") as f:
#             f.write("Date,Value\n2024-02-20,100\n2024-02-21,200\n2024-02-22,300\n")

#     def test_file_name_attribute(self):
#         """ Testa se il nome del file è salvato correttamente nell'attributo. """
#         csv_obj = CSVFile(self.test_filename)
#         self.assertEqual(csv_obj.name, self.test_filename)

#     def test_get_data_valid_file(self):
#         """ Testa se get_data() restituisce correttamente i dati. """
#         csv_obj = CSVFile(self.test_filename)
#         expected_output = [
#             ["2024-02-20", "100"],
#             ["2024-02-21", "200"],
#             ["2024-02-22", "300"]
#         ]
#         self.assertEqual(csv_obj.get_data(), expected_output)

#     def test_get_data_non_existent_file(self):
#         """ Testa il comportamento se il file non esiste. """
#         csv_obj = CSVFile("file_inesistente.csv")
#         with self.assertRaises(FileNotFoundError):
#             csv_obj.get_data()

#     def test_get_data_empty_file(self):
#         """ Testa il comportamento su un file vuoto. """
#         empty_filename = "empty.csv"
#         with open(empty_filename, "w") as f:
#             pass  # Crea un file vuoto

#         csv_obj = CSVFile(empty_filename)
#         self.assertEqual(csv_obj.get_data(), [])

# class TestNumericalCSVFile(unittest.TestCase):

#     def setUp(self):
#         """ Crea un file di test per dati numerici. """
#         self.num_filename = "test_numeric.csv"
#         with open(self.num_filename, "w") as f:
#             f.write("Date,Value\n2024-02-20,100\n2024-02-21,not_a_number\n2024-02-22,300\n")

#     def test_get_data_with_numeric_conversion(self):
#         """ Testa se NumericalCSVFile converte correttamente i numeri. """
#         num_csv_obj = NumericalCSVFile(self.num_filename)
#         expected_output = [
#             ["2024-02-20", 100.0],  # Il valore deve essere convertito in float
#             ["2024-02-21", "not_a_number"],  # Stringa non convertibile deve restare uguale
#             ["2024-02-22", 300.0]
#         ]
#         self.assertEqual(num_csv_obj.get_data(), expected_output)

# if __name__ == "__main__":
#     unittest.main()
