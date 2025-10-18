def validar_sexo(sexo):
    return sexo in ['M','F']
print(validar_sexo('M'))
print(validar_sexo('F'))
print(validar_sexo('X'))