def obtener_calificacion(nota):
    if nota > 9.0:
        return "A"
    elif nota > 8.0:
        return "B"
    elif nota >= 7.5:
        return "C"
    else:
        return "R"

try:
    calificacion = float(input("Ingresa la calificación: "))
    if calificacion < 0 or calificacion > 10:
        print("Por favor, ingresa una calificación válida entre 0 y 10.")
    else:
        print(f"La calificación es {obtener_calificacion(calificacion)}.")
except ValueError:
    print("Por favor, ingresa un número.")
