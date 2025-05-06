class Slot:
    def __init__(self, item=None, quantity=0):
        self.item = item
        self.quantity = quantity
        self.prev = None
        self.next = None

    def __str__(self):
        return f"{self.item} x{self.quantity}" if self.item else "Vacío"

class Inventory:
    def __init__(self, size=9):  # Hotbar de 9 espacios
        self.size = size
        self.head = None
        self.current = None
        self.create_inventory()

    def create_inventory(self):
        previous = None
        for i in range(self.size):
            slot = Slot()
            if self.head is None:
                self.head = slot
            else:
                previous.next = slot
                slot.prev = previous
            previous = slot
        # Cerrar la lista circular
        self.head.prev = previous
        previous.next = self.head
        self.current = self.head  # Slot seleccionado al inicio

    def display(self):
        current = self.head
        print("\nInventario hotbar:")
        for _ in range(self.size):
            if current == self.current:
                print(f">[{current}]<", end="  ")
            else:
                print(f"[{current}]", end="  ")
            current = current.next
        print("\n")

    def move_right(self):
        self.current = self.current.next

    def move_left(self):
        self.current = self.current.prev

    def add_item_to_current(self, item, quantity):
        self.current.item = item
        self.current.quantity = quantity

    def remove_current_item(self):
        self.current.item = None
        self.current.quantity = 0

# Interaccción
def main():
    inv = Inventory()
    print("Bienvenido al simulador de inventario estilo Minecraft!")
    print("Controles: a = izquierda | d = derecha | add = agregar ítem | del = eliminar ítem | q = salir")
    
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
        elif comando == 'q':
            print("Saliendo del inventario.")
            break
        else:
            print("Comando no reconocido.")

if __name__ == "__main__":
    main()

