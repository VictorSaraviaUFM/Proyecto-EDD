from pynput import keyboard

slot_1 = "Espada"
slot_2 = "Tierra"
slot_3 = "Hacha"
slot_4 = "Arco"
slot_5 = "Metal"
slot_6 = "Oro"
slot_7 = "Ballesta"
slot_8 = "Diamante"

posicion = 1
hand_left = "Mano vacía"


def mostrar_slot():
    print("\nInventario principal:")
    print(f"1: {slot_1} | Mano izquierda: {hand_left}" if posicion == 1 else f"1: {slot_1}")
    print(f"2: {slot_2} | Mano izquierda: {hand_left}" if posicion == 2 else f"2: {slot_2}")
    print(f"3: {slot_3} | Mano izquierda: {hand_left}" if posicion == 3 else f"3: {slot_3}")
    print(f"4: {slot_4} | Mano izquierda: {hand_left}" if posicion == 4 else f"4: {slot_4}")
    print(f"5: {slot_5} | Mano izquierda: {hand_left}" if posicion == 5 else f"5: {slot_5}")
    print(f"6: {slot_6} | Mano izquierda: {hand_left}" if posicion == 6 else f"6: {slot_6}")
    print(f"7: {slot_7} | Mano izquierda: {hand_left}" if posicion == 7 else f"7: {slot_7}")
    print(f"8: {slot_8} | Mano izquierda: {hand_left}" if posicion == 8 else f"8: {slot_8}")


def tirar_slot():
    global slot_1, slot_2, slot_3, slot_4, slot_5, slot_6, slot_7, slot_8

    if posicion == 1:
        slot_1 = "slot_1_vacio"
    elif posicion == 2:
        slot_2 = "slot_2_vacio"
    elif posicion == 3:
        slot_3 = "slot_3_vacio"
    elif posicion == 4:
        slot_4 = "slot_4_vacio"
    elif posicion == 5:
        slot_5 = "slot_5_vacio"
    elif posicion == 6:
        slot_6 = "slot_6_vacio"
    elif posicion == 7:
        slot_7 = "slot_7_vacio"
    elif posicion == 8:
        slot_8 = "slot_8_vacio"
    print(f"El objeto en la posición {posicion} ha sido eliminado.")


def Hand_swap():
    global slot_1, slot_2, slot_3, slot_4, slot_5, slot_6, slot_7, slot_8, hand_left

    if posicion == 1:
        slot_1, hand_left = hand_left, slot_1
    elif posicion == 2:
        slot_2, hand_left = hand_left, slot_2
    elif posicion == 3:
        slot_3, hand_left = hand_left, slot_3
    elif posicion == 4:
        slot_4, hand_left = hand_left, slot_4
    elif posicion == 5:
        slot_5, hand_left = hand_left, slot_5
    elif posicion == 6:
        slot_6, hand_left = hand_left, slot_6
    elif posicion == 7:
        slot_7, hand_left = hand_left, slot_7
    elif posicion == 8:
        slot_8, hand_left = hand_left, slot_8

    print(f"Mano izquierda: {hand_left}")
    mostrar_slot()


def inventario():
    global slot_8

    matriz_inventario = [["{}", "{}", "{}", "{}", "{}"],
                         ["{}", "{}", "{}", "{}", "{}"],
                         ["{}", "{}", "Tierra", "{}", "{}"],
                         ["{}", "{}", "{}", "{}", "{}"],
                         ["{}", "{}", "{}", "{}", "{}"]]

    def mostrar_matriz():
        print("\nInventario secundario:")
        for fila in matriz_inventario:
            print(" ".join(fila))

    mostrar_matriz()

    def on_press_inventario(key):
        global slot_8  # Declarar slot_8 como global
        nonlocal matriz_inventario
        try:
            if key.char == '2':  # Intercambiar "Tierra" con slot_8
                fila, columna = 2, 2  # Posición de "Tierra" en la matriz
                if matriz_inventario[fila][columna] == "Tierra":
                    # Realizar el intercambio entre "Tierra" y slot_8
                    matriz_inventario[fila][columna], slot_8 = slot_8, matriz_inventario[fila][columna]
                    print("\nObjeto intercambiado con éxito.")
                    mostrar_matriz()
                    mostrar_slot()
                else:
                    print("\nNo hay un objeto seleccionable en esa posición.")
                return False  # Cerrar el inventario secundario después del intercambio
            elif key.char == '3':  # Salir del inventario secundario
                mostrar_slot()  # Mostrar los slots del inventario principal
                return False  # Detener el listener del inventario secundario
        except AttributeError:
            pass

    # Listener para el inventario secundario
    with keyboard.Listener(on_press=on_press_inventario) as listener:
        listener.join()


def on_press(key):
    global posicion

    try:
        if key.char == '1':  # Abrir inventario secundario
            inventario()  # Llamar a la función inventario
        elif key.char == 'q':  # Tira el item
            tirar_slot()
            mostrar_slot()
        elif key.char == 'f':  # Cambia el item de mano
            Hand_swap()
    except AttributeError:
        if key == keyboard.Key.right:
            posicion = (posicion % 8) + 1  # Si está en 8, vuelve a 1
            mostrar_slot()
        elif key == keyboard.Key.left:
            posicion = (posicion - 2) % 8 + 1  # Si está en 1, vuelve a 8
            mostrar_slot()
        elif key == keyboard.Key.esc:
            print("Saliendo del programa.")
            return False


# Mostrar el inventario inicial una sola vez
mostrar_slot()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

