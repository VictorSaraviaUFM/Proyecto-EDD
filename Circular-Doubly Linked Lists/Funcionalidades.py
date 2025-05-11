class Slot:
    def __init__(self, item=None, quantity=0):
        self.item = item
        self.quantity = quantity
        self.prev = None
        self.next = None

    def __str__(self):
        return f"{self.item} x{self.quantity}" if self.item else "Vacío"

class Inventory:
    def __init__(self, hotbar_size=9, full_inv_size=27):
        self.hotbar_size = hotbar_size
        self.full_inv_size = full_inv_size
        self.hotbar_head = None
        self.current = None
        self.full_inventory = []
        self.off_hand = None  # No existe hasta que se active
        self.create_inventory()

    def create_inventory(self):
        previous = None
        for i in range(self.hotbar_size):
            slot = Slot()
            if self.hotbar_head is None:
                self.hotbar_head = slot
            else:
                previous.next = slot
                slot.prev = previous
            previous = slot
            self.full_inventory.append(slot)
        self.hotbar_head.prev = previous
        previous.next = self.hotbar_head
        self.current = self.hotbar_head

        for _ in range(self.hotbar_size, self.full_inv_size):
            self.full_inventory.append(Slot())

    def display(self):
        current = self.hotbar_head
        print("\nInventario hotbar:")
        for _ in range(self.hotbar_size):
            if current == self.current:
                print(f">[{current}]<", end="  ")
            else:
                print(f"[{current}]", end="  ")
            current = current.next
        if self.off_hand:
            print(f"\nSlot de la otra mano: [{self.off_hand}]")
        print()

    def display_full_inventory(self):
        print("\nInventario completo:")
        for i in range(self.full_inv_size):
            if self.full_inventory[i] == self.current:
                print(f">[{self.full_inventory[i]}]<", end="  ")
            else:
                print(f"[{self.full_inventory[i]}]", end="  ")
            if (i + 1) % 9 == 0:
                print()
        if self.off_hand:
            print(f"\nSlot de la otra mano: [{self.off_hand}]")
        print()

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

    def throw_current_item(self):
        if self.current.item:
            print(f"Tiraste {self.current.item} x{self.current.quantity}")
            self.remove_current_item()
        else:
            print("No hay ningún ítem que tirar en este slot.")

    def put_in_offhand(self):
        if self.current.item:
            if not self.off_hand:
                self.off_hand = Slot()
                print("¡Slot de la otra mano desbloqueado!")
            self.off_hand.item = self.current.item
            self.off_hand.quantity = self.current.quantity
            print(f"Moviste {self.current.item} x{self.current.quantity} a la otra mano.")
            self.remove_current_item()
        else:
            print("No hay ítem en el slot actual para mover a la otra mano.")

