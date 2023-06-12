import numpy as np 

def generador_password():
	minusculas = np.array(list("abcdefghijklmnopqrstuvwxyz"))
    mayusculas = np.array(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    numeros = np.array(list("0123456789"))
    alfanumerico = np.concatenate((minusculas, mayusculas, numeros))
    
    primer_caracter = np.random.choice(alfanumerico)
    
    numeros = np.random.choice(numeros, size=3, replace=False)
    
    disponibles = np.concatenate((minusculas, mayusculas, numeros))
    np.random.shuffle(disponibles)
    letras_alfanumericos = disponibles[:np.random.randint(8, 14)]
    
    password = np.concatenate(([primer_caracter], numeros, letras_alfanumericos))
    np.random.shuffle(password)
    
    return "".join(password)

password = generador_password()
print("Contraseña generada:", password)