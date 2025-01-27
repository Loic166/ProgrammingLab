import re

def conteggio(file_name):
    conteggio_parole = {}
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            # Diviser le texte en phrases
            phrases = re.split(r'[.!?]', text)
            for phrase in phrases:
                # Enlever les espaces au début et à la fin de la phrase
                phrase = phrase.strip()
                if phrase:
                    # Prendre la première parole de la phrase
                    prima_parola = phrase.split()[0]
                    if prima_parola in conteggio_parole:
                        conteggio_parole[prima_parola] += 1
                    else:
                        conteggio_parole[prima_parola] = 1
        return conteggio_parole
    except FileNotFoundError:
        return "Il file non esiste."
    except Exception as e:
        return f"Si è verificato un errore: {str(e)}"

# Esempio di utilizzo
file_name = '/workspaces/ProgramingLab/Projet_python/zeebaby.txt'
print(conteggio(file_name))

def conteggio(file_name):
    conteggio_parole = {}
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            # Diviser le texte en phrases sans utiliser 're'
            phrases = []
            phrase = ""
            for char in text:
                if char in ".!?":
                    if phrase:
                        phrases.append(phrase.strip())
                    phrase = ""
                else:
                    phrase += char
            if phrase:
                phrases.append(phrase.strip())
            
            for phrase in phrases:
                if phrase:
                    # Prendre la première parole de la phrase
                    prima_parola = phrase.split()[0]
                    if prima_parola in conteggio_parole:
                        conteggio_parole[prima_parola] += 1
                    else:
                        conteggio_parole[prima_parola] = 1
        return conteggio_parole
    except FileNotFoundError:
        return "Le fichier n'existe pas."
    except Exception as e:
        return f"Une erreur est survenue: {str(e)}"

# Exemple d'utilisation
file_name = 'testo.txt'
print(conteggio(file_name))
