#*********** Requisitos *************
# menu con opciones
# 1) agregar un producto
# 2) remover un producto
# 3) listarlos todos
# 4) buscar un producto
# 5) salir del prog

# listas 
# condicionales
# while
#**************************************

productos = []
producto_busqueda =[]

while True:
    print("")
    print("**** Sistema de Gestión Básica de Productos ****\n")
    print("\t 1) Agregar")
    print("\t 2) Mostrar")
    print("\t 3) Buscar")
    print("\t 4) Remover")
    print("\t 5) Salir")
    print("")
    print("************************************************\n")
    
    usuario = input("Elija una opción (1-5): ")
    if usuario == "5":
        print("")
        print("\n\t¡Adiós!\n")
        print("")
        break
    
    elif usuario == "1":
        print("")
        producto = input("Producto a agregar: ").strip()
        productos.append(producto)
        print("")
        print(f"\nSe agregó {producto}\n")
        print("")
                
    elif usuario == "2":
        print("Su lista de productos: ")
        print("")
        if productos:
            for p in productos:
                print(f"\t * {p}")
        else:
            print("\t(La lista está vacía)")
        print("")

    elif usuario =="3":
        print("")
        producto_busqueda = input("Producto a Buscar: ")
        if producto_busqueda in productos:
           print("")
           print(f"{producto_busqueda} esta en la lista")
           print("")
        else:
            print("")
            print(f"{producto_busqueda} no se encuentra en la lista")
            print("")

    elif usuario == "4":
        print("")
        remover = input("Producto a remover: ")
        productos.remove(remover)
        print("")
        print(f"Se removio {remover}")
        print("")
        
