# class Moyenne:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def media (self):
#         return (self.a + self.b)/2
  
#         # med =(self.a + self.b)/2 

#         # return med 
  
# lista = [1,3,[2,43,5],5,True,56,3]
 
# list_0 = [211,4,4]
# print(lista[2])

# for item in lista:
#     list_0.append(item)

# print(list_0)

# def lista (list1, list2):

#     for item in list1:
#         list2.append(item)

#     # print (list2)
#     return list2


# list1=['a',"b"]
# list2=[1,2,3,4,5,6,7]

# # print (list1)

# list0 = lista(list1,list2)
# print(list0)

# my_file = open(r'dati.csv', 'r')
# contenuto = my_file.read()
# contenuto = contenuto.split()
# print(contenuto)
# # print(contenuto)

# # for item in my_file:
# #     item = item.strip().split(',')
# #     print(item)

# my_file.close()

import csv

fichier = open('dati.csv', 'r')
contenu = csv.DictReader(fichier)
#contenu = contenu.split()
print(contenu)
