def validar_contraseña(clave):
    if len(clave)>=8:
        return "Contraseña válida"
    else:
        return"Contraseña no valida"
    
print(validar_contraseña('abc12345'))
print(validar_contraseña('abc'))