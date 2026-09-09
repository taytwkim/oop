from board import DiskColor

class Player:
    def __init__(self, name: str, color: DiskColor):
        self.name = name
        self.color = color

    def getName(self) -> str:
        return self.name

    def getColor(self) -> DiskColor:
        return self.color
