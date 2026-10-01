from size import Size

class Compartment:
    def __init__(self, size: Size):
        self.size: Size = size
        self.occupied: bool = False

    def get_size(self) -> Size:
        return self.size

    def is_occupied(self) -> bool:
        return self.occupied

    def mark_occupied(self) -> None:
        self.occupied = True

    def mark_free(self) -> None:
        self.occupied = False

    def open(self) -> None:
        pass