palabra=input("INGRESA UNA FRASE: ").strip().lower()

if "triste" in palabra:
    areglado=palabra.replace("triste","feliz")
    print(areglado)
else:
    print(palabra.upper())
