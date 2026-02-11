from typing import Optional

from src.constants import ClawSize
from src.movement import MovementStrategy, create_all_movements


class Creature:
    def __init__(self):
        self.health = 100
        self.stamina = 100
        self.position = 0

        self.legs: int = 0
        self.wings: int = 0
        self.claws: Optional[ClawSize] = None
        self.teeth_sharpness: int = 0

        self.base_attack_power: int = 10

    def get_available_movements(self) -> list[MovementStrategy]:
        all_movements = create_all_movements()
        return [m for m in all_movements if m.can_execute(self)]

    def calculate_attack_power(self) -> int:
        power = self.base_attack_power + self.teeth_sharpness

        if self.claws:
            power *= self.claws.value

        return power

    def attack(self, target: "Creature") -> None:
        damage = self.calculate_attack_power()
        target.health -= damage

    def __str__(self) -> str:
        parts = [f"Health: {self.health}", f"Stamina: {self.stamina}", f"Legs: {self.legs}", f"Wings: {self.wings}"]
        if self.claws:
            parts.append(f"Claws: {self.claws.name}")
        if self.teeth_sharpness > 0:
            parts.append(f"Teeth: +{self.teeth_sharpness}")
        return ", ".join(parts)
