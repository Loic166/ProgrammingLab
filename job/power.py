# Apro il file
# my_file = open('power.py', 'r')
# # Leggo il contenuto
# my_file_contents = my_file.read()


# #Stampo a schermo i primi 50 caratteri
# if len(my_file_contents) > 50:
#     print(my_file_contents[0:50] + '...')
# else:
#     print(my_file_contents)
# #Chiudo il file
# my_file.close()

#my_file = open('power.py', 'r')

# content = my_file.read()

# my_file = open('/workspaces/ProgramingLab/Projet_python/Loic.py', 'r')
# for line in my_file:
#     print(line)

my_file = open('/workspaces/ProgramingLab/job/job.py', 'a')
my_file.write('print("Addio")')
print(my_file)
#my_file.close()

# with open('power.py') as file:
#     print(file.readline() )
#content = my_file.read()[1::]
# print(my_file.readline())
#print(content)
# print(my_file.readline())
# print(my_file.readline())
my_file.close()