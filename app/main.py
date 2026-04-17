class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self._health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = value
        if self._health <= 0:
            self._health = 0
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
        status = "hidden" if self.hidden else "alive"
        print(status)


class Carnivore(Animal):
    def bite(self, target: int) -> None:
        if not isinstance(target, Herbivore):
            return
        if target.hidden:
            return
        if target.health > 0:
            target.health -= 50
