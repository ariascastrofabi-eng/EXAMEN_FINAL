comentario=input("INGRESA UN COMENTARIO DEL PRODUCTO(malo o aceptable): ").strip().lower()

if comentario == "malo":
    print("Tu comentario no cumple con las normas, intenta de nuevo.")
elif comentario == "aceptable":
    print("Comentario publicado con éxito.")
else:
    print("solo malo o aceptable")