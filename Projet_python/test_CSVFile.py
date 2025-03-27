import unittest

from Projet_python.csvfile import CSVFile

class TestSCVFile(unittest.TestCase):

    def setUp(self):
        self.file = CSVFile('/workspaces/ProgramingLab/Projet_python/shampoo_sales.csv') 
     
    def test_attribuito(self):
        self.file_name = '/workspaces/ProgramingLab/Projet_python/shampoo_sales.csv'
        self.assertEqual(self.file.name, self.file_name)

    # def test_output(self):
    #     self.assertIsInstance(self.file.get_data(), list)

    # def test_eccezioni(self):
    #     #self.assertRaises(FileNotFoundError, 'no_file.csv')

    #     with self.assertRaises(FileNotFoundError):
    #         self.file = CSVFile('file_non_esistente.csv')


