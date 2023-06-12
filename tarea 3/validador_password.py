def validar_password(password):
    longitud = len(password)
    minusculas = sum(1 for c in password if c.islower())
    mayusculas = sum(1 for c in password if c.isupper())
    numeros = sum(1 for c in password if c.isdigit())
    alfanumericos = sum(1 for c in password if c.isalnum())
    
    condiciones = []
    
    if longitud >= 8 and longitud <=15:
        condiciones.append("Longitud válida")
    else:
        condiciones.append("La longitud debe estar entre 8 y 15 caracteres")
    
    if minusculas + mayusculas >= 1:
        condiciones.append("Contiene al menos 1 letra o alfanumérico")
    else: 
        condiciones.append("Debe contener al menos 1 letra o alfanumérico")
    
    if numeros == 3:
        condiciones.append("Contiene exactamente 3 números")
    else: 
        condiciones.append("Debe contener exactamente 3 números")
        
    if mayusculas == 3:
        condiciones.append("Contiene exactamente 3 letras mayúsculas")
    else:
        condiciones.append("Debe contener exactamente 3 letras mayúsculas")
        
    if alfanumericos == longitud:
        condiciones.append("No se repiten caracteres")
    else:
        condiciones.append("No deben repetirse caracteres")
    
    return all(condiciones), condiciones

valido, condiciones = validar_password(password)
print("Contraseña válida:", valido)
print("Condiciones no cumplidas")
for condicion in condiciones:
    print("- ", condicion)