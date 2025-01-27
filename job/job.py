def compter_lignes(nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            lignes = fichier.readlines()
            return len(lignes)
    except FileNotFoundError:
        return "Le fichier n'existe pas."
    except Exception as e:
        return f"Une erreur est survenue: {str(e)}"
    

print(compter_lignes('/workspaces/ProgramingLab/job/job.py'))

def compte(file):
    count = 0
    for line in file.readline():
        line = line
        count += 1
        file.close()
    return count

print(compter_lignes('/workspaces/ProgramingLab/job/job.py'))

def compteur(nom):
    with open(nom, 'r') as file:
        return len(file)


print(compter_lignes('/workspaces/ProgramingLab/power.py'))
#

def conta_parola(nome_file,parola):
    compt = 0
    try:
        with open(nome_file, 'r') as file:
            contenuto = file.read()
            list_parole = contenuto.split()
            for i in range(len(list_parole)):
                if list_parole[i] == parola:
                    compt += 1
            return compt
    except:
        return "Il file non esiste."
    
    
print(conta_parola('prog.py'))