import pygame
import os
from pynput import keyboard

pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Inventario Pygame sin estructuras")

folder_imagenes = "Minecraft copy"

slot_1 = "Madera"
slot_2 = "Valla"
slot_3 = "Antorcha"
slot_4 = "Hielo"
slot_5 = "Diamante"
slot_6 = "Esmeralda"
slot_7 = "Gradas"
slot_8 = "Escudo"
slot_9 = "Espada"
hand_left = "vacio"
posicion = 1
running = True
inventario_abierto = False
inventario_mostrando_item = False  # NUEVA VARIABLE

def cargar_imagen(nombre):
    ruta = os.path.join(folder_imagenes, nombre)
    try:
        img = pygame.image.load(ruta)
        return pygame.transform.scale(img, (200, 200))
    except Exception as e:
        print(f"No se pudo cargar {ruta}: {e}")
        return pygame.Surface((200, 200))

imagen_1 = cargar_imagen("madera.png")
imagen_2 = cargar_imagen("valla.png")
imagen_3 = cargar_imagen("antorcha.png")
imagen_4 = cargar_imagen("hielo.png")
imagen_5 = cargar_imagen("diamante.png")
imagen_6 = cargar_imagen("esmeralda.png")
imagen_7 = cargar_imagen("gradas.png")
imagen_8 = cargar_imagen("escudo.png")
imagen_9 = cargar_imagen("espada.png")
imagen_item_cambiado = cargar_imagen("Cambio_De_Mano.png")
imagen_inventario = cargar_imagen("inventario.png")
imagen_item_para_inventario = cargar_imagen("doble objetos.png")  # NUEVA IMAGEN
imagen_vacio = cargar_imagen("drop.png")

def mostrar_slot():
    pantalla.fill((50, 50, 50))
    if inventario_abierto:
        if inventario_mostrando_item:
            pantalla.blit(imagen_item_para_inventario, (ANCHO//2 - 100, ALTO//2 - 100))
        else:
            pantalla.blit(imagen_inventario, (ANCHO//2 - 100, ALTO//2 - 100))
    else:
        imagen_actual = obtener_imagen()
        pantalla.blit(imagen_actual, (ANCHO//2 - 100, ALTO//2 - 100))
    pygame.display.flip()

def obtener_imagen():
    if posicion == 1:
        return imagen_1 if slot_1 != "slot_1_vacio" else imagen_vacio
    elif posicion == 2:
        return imagen_2 if slot_2 != "slot_2_vacio" else imagen_vacio
    elif posicion == 3:
        return imagen_3 if slot_3 != "slot_3_vacio" else imagen_vacio
    elif posicion == 4:
        return imagen_4 if slot_4 != "slot_4_vacio" else imagen_vacio
    elif posicion == 5:
        return imagen_5 if slot_5 != "slot_5_vacio" else imagen_vacio
    elif posicion == 6:
        return imagen_6 if slot_6 != "slot_6_vacio" else imagen_vacio
    elif posicion == 7:
        return imagen_7 if slot_7 != "slot_7_vacio" else imagen_vacio
    elif posicion == 8:
        return imagen_item_cambiado if slot_8 == "item_cambiado" else (imagen_8 if slot_8 != "slot_8_vacio" else imagen_vacio)
    elif posicion == 9:
        return imagen_9 if slot_9 != "slot_9_vacio" else imagen_vacio

def tirar_slot():
    global slot_1, slot_2, slot_3, slot_4, slot_5, slot_6, slot_7, slot_8, slot_9
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
    elif posicion == 9:
        slot_9 = "slot_9_vacio"
    mostrar_slot()

def Hand_swap():
    global slot_8
    slot_8 = "item_cambiado"
    mostrar_slot()

def on_press(key):
    global posicion, running, inventario_abierto, inventario_mostrando_item, slot_8
    try:
        if key.char == '1':
            inventario_abierto = True
            inventario_mostrando_item = False
            mostrar_slot()
        elif key.char == '2' and inventario_abierto:
            slot_8 = "item_cambiado"
            inventario_mostrando_item = True
            mostrar_slot()
        elif key.char == '3' and inventario_abierto:
            inventario_abierto = False
            inventario_mostrando_item = False
            mostrar_slot()
        elif key.char == 'q' and not inventario_abierto:
            tirar_slot()
        elif key.char == 'f' and not inventario_abierto:
            Hand_swap()
    except AttributeError:
        if key == keyboard.Key.right and not inventario_abierto:
            posicion = (posicion % 9) + 1
            mostrar_slot()
        elif key == keyboard.Key.left and not inventario_abierto:
            posicion = (posicion - 2) % 9 + 1
            mostrar_slot()
        elif key == keyboard.Key.esc:
            running = False
            pygame.quit()
            os._exit(0)

listener = keyboard.Listener(on_press=on_press)
listener.start()

mostrar_slot()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            os._exit(0)
    pygame.time.delay(100)
    mostrar_slot()
