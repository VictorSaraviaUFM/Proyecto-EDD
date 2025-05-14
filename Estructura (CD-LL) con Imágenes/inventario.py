import pygame
import os
from pynput import keyboard

pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Inventario con Estructura Circular Doble")

# Carpeta de imágenes
folder_imagenes = "Minecraft copy"

class Slot:
    def __init__(self, nombre="vacío"):
        self.item = nombre
        self.prev = None
        self.next = None

class Inventory:
    def __init__(self):
        self.head = None
        self.current = None
        self.offhand_enabled = False
        self.offhand_slot = None
        self.build_inventory()

    def build_inventory(self):
        items = [
            "Madera", "Valla", "Antorcha", "Hielo", "Diamante",
            "Esmeralda", "Gradas", "Escudo", "Espada"
        ]
        previous = None
        for nombre in items:
            slot = Slot(nombre)
            if not self.head:
                self.head = slot
            else:
                previous.next = slot
                slot.prev = previous
            previous = slot
        # Circular
        previous.next = self.head
        self.head.prev = previous
        self.current = self.head

    def move_right(self):
        self.current = self.current.next

    def move_left(self):
        self.current = self.current.prev

    def drop_current_item(self):
        self.current.item = "vacío"

    def hand_swap(self):
        if not self.offhand_enabled:
            self.offhand_slot = Slot("item_cambiado")
            self.offhand_enabled = True
        else:
            self.offhand_slot.item = "item_cambiado"
