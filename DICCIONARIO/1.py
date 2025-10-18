def crear_usuario(nombre,sexo,contra):
    return{
        'nombre':nombre,
        'sexo':sexo,
        'contra':contra
    }

usuario = crear_usuario('L.pereira','F','as1234yuioj')
print(usuario)