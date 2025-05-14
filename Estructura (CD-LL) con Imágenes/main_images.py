import pygame
import os
from pynput import keyboard

pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Inventario con CDLL")

# Carpeta de imágenes
folder_imagenes = "Minecraft copy"

def cargar_imagen(nombre):
    ruta = os.path.join(folder_imagenes, nombre)
    try:
        img = pygame.image.load(ruta)
        return pygame.transform.scale(img, (200, 200))
    except:
        return pygame.Surface((200, 200))

# Cargar imágenes
imagenes = {
    "Madera": cargar_imagen("madera.png"),
    "Valla": cargar_imagen("valla.png"),
    "Antorcha": cargar_imagen("antorcha.png"),
    "Hielo": cargar_imagen("hielo.png"),
    "Diamante": cargar_imagen("diamante.png"),
    "Esmeralda": cargar_imagen("esmeralda.png"),
    "Gradas": cargar_imagen("gradas.png"),
    "Escudo": cargar_imagen("escudo.png"),
    "Espada": cargar_imagen("espada.png"),
    "Cambio": cargar_imagen("Cambio_De_Mano.png"),
    "Inventario": cargar_imagen("inventario.png"),
    "Doble": cargar_imagen("doble objetos.png"),
    "Vacio": cargar_imagen("Minecraft 1.21.5 10_05_2025 18_17_48")
}


class Slot:
    def __init__(self, item=None):
        self.item = item
        self.prev = None
        self.next = None

class Inventory:
    def __init__(self):
        self.size = 9
        self.current = None
        self.hand_slot = None
        self.inventario_abierto = False
        self.mostrando_item = False
        self.create_slots()

    def create_slots(self):
        items = ["Madera", "Valla", "Antorcha", "Hielo", "Diamante", "Esmeralda", "Gradas", "Escudo", "Espada"]
        prev = None
        for item in items:
            slot = Slot(item)
            if not self.current:
                self.current = slot
                head = slot
            else:
                prev.next = slot
                slot.prev = prev
            prev = slot
        # Circular
        head.prev = prev
        prev.next = head

    def mover_derecha(self):
        self.current = self.current.next

    def mover_izquierda(self):
        self.current = self.current.prev

    def eliminar_item_actual(self):
        self.current.item = None

    def activar_mano_secundaria(self):
        if not self.hand_slot:
            self.hand_slot = Slot("Cambio")

    def obtener_imagen_actual(self):
        item = self.current.item
        if item in imagenes:
            return imagenes[item]
        return imagenes["Vacio"]

    def mostrar(self):
        pantalla.fill((50, 50, 50))
        if self.inventario_abierto:
            if self.mostrando_item:
                pantalla.blit(imagenes["Doble"], (ANCHO//2 - 100, ALTO//2 - 100))
            else:
                pantalla.blit(imagenes["Inventario"], (ANCHO//2 - 100, ALTO//2 - 100))
        else:
            pantalla.blit(self.obtener_imagen_actual(), (ANCHO//2 - 100, ALTO//2 - 100))
        pygame.display.flip()


# Inicializar el inventario
inventario = Inventory()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            os._exit(0)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and not inventario.inventario_abierto:
                inventario.mover_derecha()
            elif event.key == pygame.K_LEFT and not inventario.inventario_abierto:
                inventario.mover_izquierda()
            elif event.key == pygame.K_q and not inventario.inventario_abierto:
                inventario.eliminar_item_actual()
            elif event.key == pygame.K_f and not inventario.inventario_abierto:
                inventario.activar_mano_secundaria()
            elif event.key == pygame.K_1:
                inventario.inventario_abierto = True
                inventario.mostrando_item = False
            elif event.key == pygame.K_2 and inventario.inventario_abierto:
                inventario.activar_mano_secundaria()
                inventario.mostrando_item = True
            elif event.key == pygame.K_3:
                inventario.inventario_abierto = False
                inventario.mostrando_item = False
            elif event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                os._exit(0)

    pygame.time.delay(100)
    inventario.mostrar()
