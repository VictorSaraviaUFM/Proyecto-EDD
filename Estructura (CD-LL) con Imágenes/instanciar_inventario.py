from inventario import Inventory
import pygame
import os
from pynput import keyboard
from inventario import folder_imagenes

inventory = Inventory()
running = True
inventario_abierto = False
inventario_mostrando_item = False


pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Inventario")

# Cargar imágenes
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
imagen_item_para_inventario = cargar_imagen("doble objetos.png")
imagen_vacio = cargar_imagen("Minecraft 1.21.5 10_05_2025 18_17_48.png")

def obtener_imagen():
    nombre = inventory.current.item.lower()
    if nombre == "vacío":
        return imagen_vacio
    elif nombre == "item_cambiado":
        return imagen_item_cambiado
    elif nombre == "madera":
        return imagen_1
    elif nombre == "valla":
        return imagen_2
    elif nombre == "antorcha":
        return imagen_3
    elif nombre == "hielo":
        return imagen_4
    elif nombre == "diamante":
        return imagen_5
    elif nombre == "esmeralda":
        return imagen_6
    elif nombre == "gradas":
        return imagen_7
    elif nombre == "escudo":
        return imagen_8
    elif nombre == "espada":
        return imagen_9
    return imagen_vacio

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

def on_press(key):
    global running, inventario_abierto, inventario_mostrando_item

    try:
        if key.char == '1':
            inventario_abierto = True
            inventario_mostrando_item = False
            mostrar_slot()
        elif key.char == '2' and inventario_abierto:
            inventory.hand_swap()
            inventario_mostrando_item = True
            mostrar_slot()
        elif key.char == '3' and inventario_abierto:
            inventario_abierto = False
            inventario_mostrando_item = False
            mostrar_slot()
        elif key.char == 'q' and not inventario_abierto:
            inventory.drop_current_item()
            mostrar_slot()
        elif key.char == 'f' and not inventario_abierto:
            inventory.hand_swap()
            mostrar_slot()
    except AttributeError:
        if key == keyboard.Key.right and not inventario_abierto:
            inventory.move_right()
            mostrar_slot()
        elif key == keyboard.Key.left and not inventario_abierto:
            inventory.move_left()
            mostrar_slot()
        elif key == keyboard.Key.esc:
            running = False
            pygame.quit()
            os._exit(0)

# Listener de teclado
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