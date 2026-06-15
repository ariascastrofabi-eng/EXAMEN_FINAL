contraseña="12345"
contraseña1=input("INGRESA TU CONTRASEÑA: ").strip()

while contraseña == contraseña1:
    if contraseña == contraseña1:
        contraseña1=input("Contraseña insegura,ingresa otra: ").strip()

if contraseña != contraseña1:
    print("ACCESO CONCEDIDO")
