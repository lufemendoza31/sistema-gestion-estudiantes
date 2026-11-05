# =====================================================================
# Sistema de Gestión de Estudiantes (SGE) Básico
# Autor: Luisa Fernanda Mendoza Peña
# Materia: Lógica de Programación - UCompensar
# =====================================================================

def mostrar_estudiante(estudiante):
    """Función reutilizable para mostrar los datos detallados de un estudiante."""
    print(f"ID: {estudiante['id']} | Nombre: {estudiante['nombre']} | Edad: {estudiante['edad']} | Promedio: {estudiante['promedio']}")

def main():
    # Inicialización de la lista y variables especiales requeridas
    estudiantes = []          # Lista para almacenar los diccionarios de estudiantes
    bandera_salir = False     # Variable bandera para controlar la salida del bucle principal
    total_estudiantes = 0     # Variable de conteo para llevar el total de registros
    
    while not bandera_salir:
        print("\n==========================================")
        print("   SISTEMA DE GESTIÓN DE ESTUDIANTES (SGE)")
        print("==========================================")
        print("1. Agregar estudiante")
        print("2. Mostrar lista completa")
        print("3. Buscar estudiante por ID")
        print("4. Salir del sistema")
        
        # Validación de entrada del menú mediante manejo de excepciones
        try:
            opcion = int(input("Seleccione una opción (1-4): "))
        except ValueError:
            print("[Error]: Por favor, ingrese un número entero válido.")
            continue
            
        if opcion == 1:
            print("\n--- Registrar Nuevo Estudiante ---")
            id_est = input("Ingrese el ID del estudiante: ").strip()
            
            # Verificación de unicidad del ID
            encontrado = False
            for est in estudiantes:
                if est['id'] == id_est:
                    encontrado = True
                    break
            
            if encontrado:
                print("[Error]: Ya existe un estudiante registrado con ese ID.")
            else:
                nombre = input("Ingrese el nombre completo: ").strip()
                try:
                    edad = int(input("Ingrese la edad: "))
                    promedio = float(input("Ingrese el promedio académico (0.0 - 5.0): "))
                    
                    if edad <= 0 or promedio < 0.0 or promedio > 5.0:
                        print("[Error]: Los valores ingresados están fuera del rango permitido.")
                    else:
                        nuevo_estudiante = {
                            'id': id_est,
                            'nombre': nombre,
                            'edad': edad,
                            'promedio': promedio
                        }
                        estudiantes.append(nuevo_estudiante)
                        total_estudiantes += 1
                        print("¡Estudiante agregado exitosamente!")
                except ValueError:
                    print("[Error]: La edad y el promedio deben ser valores numéricos.")
                    
        elif opcion == 2:
            print(f"\n--- Lista de Estudiantes (Total: {total_estudiantes}) ---")
            if total_estudiantes == 0:
                print("No hay estudiantes registrados actualmente.")
            else:
                for est in estudiantes:
                    mostrar_estudiante(est)
                    
        elif opcion == 3:
            print("\n--- Buscar Estudiante por ID ---")
            if total_estudiantes == 0:
                print("No hay registros disponibles para realizar la búsqueda.")
            else:
                id_buscar = input("Ingrese el ID a buscar: ").strip()
                estudiante_encontrado = None
                
                for est in estudiantes:
                    if est['id'] == id_buscar:
                        estudiante_encontrado = est
                        break
                
                # Estructura de decisión simple para validar si fue encontrado
                if estudiante_encontrado is not None:
                    print("¡Estudiante encontrado con éxito!")
                    mostrar_estudiante(estudiante_encontrado)
                else:
                    print("El estudiante con el ID especificado no fue encontrado.")
                    
        elif opcion == 4:
            print("\nSaliendo del Sistema de Gestión de Estudiantes. ¡Hasta pronto!")
            bandera_salir = True
        else:
            print("[Advertencia]: Opción inválida. Seleccione un número entre 1 y 4.")

if __name__ == "__main__":
    main()