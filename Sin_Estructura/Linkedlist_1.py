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

def mostrar_slot():
    if posicion == 1:
        print(slot_1)
    elif posicion == 2:
        print(slot_2)
    elif posicion == 3:
        print(slot_3)
    elif posicion == 4:
        print(slot_4)
    elif posicion == 5:
        print(slot_5)
    elif posicion == 6:
        print(slot_6)
    elif posicion == 7:
        print(slot_7)
    elif posicion == 8:
        print(slot_8)

def on_press(key):
    global posicion

    if key == keyboard.Key.right:
        posicion = (posicion % 8) + 1  # Si está en 8, vuelve a 1
        mostrar_slot()
    elif key == keyboard.Key.left:
        posicion = (posicion - 2) % 8 + 1  
        mostrar_slot()
    elif key == keyboard.Key.esc:
        print("Saliendo del programa.")
        return False

mostrar_slot()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

