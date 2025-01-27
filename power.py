# Apro il file
# my_file = open('power.py', 'r')
# # Leggo il contenuto
# my_file_contents = my_file.read()


# #Stampo a schermo i primi 50 caratteri/87
# if len(my_file_contents) > 50:
#     print(my_file_contents[0:50] + '...')
# else:
#     print(my_file_contents)
# #Chiudo il file
# my_file.close()

#my_file = open('power.py', 'r')

# content = my_file.read()

# my_file = open('/workspaces/ProgramingLab/job/job.py', 'r')
# for line in my_file:
#     print(line)


# with open('power.py') as file:
#     print(file.readline() )
#content = my_file.read()[1::]
# print(my_file.readline())
#print(content)
# print(my_file.readline())
# print(my_file.readline())
#my_file.close()

# mia_stringa = 'Date,Sales\n'
# lista_elementi = mia_stringa.split(',')
# print(lista_elementi)

import csv
def affich(name_file):

    try:
        with open(name_file, 'r') as file:
            content = csv.reader(file)
            next(content)
            for line in content:
                print(line[1])

    except:
        print("Il file non esiste.")

def sum_csv(name_file):
    
    tot = 0
    try:
        with open(name_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for line in csv_reader:
                tot += float(line[1])
        return tot
    
    except :
        return "Il file non esiste."
    

def conta_righe(file_name):


    with open(file_name, 'r') as file:
        content = file.readline()
        return len(content) 

  
def conta_parola(name_file, parola):
    tot = 0
    try:
        with open(name_file, 'r') as file:
            my_file = file.read()
            for line in my_file:
                if parola in line:
                    tot += 1
        return tot
    except:
        return "Il file non esiste."



    



#affich('/orkspaces/ProgramingLab/Projet_python/shampoo_sales.csv')
#print(sum_csv('/workspaces/ProgramingLab/Projet_python/shampoo_sales.csv'))
#print(conta_parola('/workspaces/ProgramingLab/power.py','Apro'))
print(affich('/workspaces/ProgramingLab/power.py'))