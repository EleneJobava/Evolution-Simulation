from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from src.constants import MOVEMENT_REQUIREMENTS, MOVEMENT_STATS, MovementType

if TYPE_CHECKING:
    from src.creature import Creature


class MovementStrategy(ABC):
    def __init__(self, movement_type: MovementType):
        self.movement_type = movement_type
        self.requirements = MOVEMENT_REQUIREMENTS[movement_type]
        self.stats = MOVEMENT_STATS[movement_type]

    @abstractmethod
    def can_execute(self, creature: "Creature") -> bool:
        pass

    def execute(self, creature: "Creature") -> bool:
        if not self.can_execute(creature):
            return False

        creature.stamina -= self.stats["stamina_cost"]
        creature.position += self.stats["speed"]
        return True

    def get_speed(self) -> int:
        return self.stats["speed"]


class CrawlMovement(MovementStrategy):
    def __init__(self):
        super().__init__(MovementType.CRAWL)

    def can_execute(self, creature: "Creature") -> bool:
        result: bool = creature.stamina >= int(self.stats["stamina_cost"])
        return result


class BodyPartMovement(MovementStrategy):
    def can_execute(self, creature: "Creature") -> bool:
        has_body_parts = (
            creature.legs >= self.requirements["min_legs"] and creature.wings >= self.requirements["min_wings"]
        )
        has_enough_stamina = creature.stamina >= self.requirements["min_stamina"]
        can_afford_cost = creature.stamina >= self.stats["stamina_cost"]

        return has_body_parts and has_enough_stamina and can_afford_cost


class HopMovement(BodyPartMovement):
    def __init__(self):
        super().__init__(MovementType.HOP)


class WalkMovement(BodyPartMovement):
    def __init__(self):
        super().__init__(MovementType.WALK)


class RunMovement(BodyPartMovement):
    def __init__(self):
        super().__init__(MovementType.RUN)


class FlyMovement(BodyPartMovement):
    def __init__(self):
        super().__init__(MovementType.FLY)


def create_all_movements() -> list[MovementStrategy]:
    return [
        CrawlMovement(),
        HopMovement(),
        WalkMovement(),
        RunMovement(),
        FlyMovement(),
    ]
