from Funcionalidades import Inventory  

def main():
    inv = Inventory()
    print("Bienvenido al simulador de inventario estilo Minecraft!")
    print("Controles:")
    print(" a = izquierda | d = derecha | add = agregar ítem | del = eliminar ítem")
    print(" inv = abrir inventario completo | throw = tirar ítem | off = mover a la otra mano")
    print(" q = salir\n")

    while True:
        inv.display()
        comando = input(">> ").strip().lower()

        if comando == 'a':
            inv.move_left()
        elif comando == 'd':
            inv.move_right()
        elif comando == 'add':
            item = input("Nombre del ítem: ")
            cantidad = input("Cantidad: ")
            if cantidad.isdigit():
                inv.add_item_to_current(item, int(cantidad))
            else:
                print("Cantidad inválida.")
        elif comando == 'del':
            inv.remove_current_item()
        elif comando == 'inv':
            inv.display_full_inventory()
        elif comando == 'throw':
            inv.throw_current_item()
        elif comando == 'off':
            inv.put_in_offhand()
        elif comando == 'q':
            print("Saliendo del inventario.")
            break
        else:
            print("Comando no reconocido.")

if __name__ == "__main__":
    main()