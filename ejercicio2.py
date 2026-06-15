comentario=input("INGRESA UN COMENTARIO DEL PRODUCTO(malo o aceptable): ").strip().lower()

if "malo" in comentario:
    print("Tu comentario no cumple con las normas, intenta de nuevo.")
elif "aceptable" in comentario:
    print("Comentario publicado con éxito.")
else:
    print("solo malo o aceptable")