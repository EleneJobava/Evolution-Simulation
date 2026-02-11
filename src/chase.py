from abc import ABC, abstractmethod

from src.constants import END_POS
from src.creature import Creature
from src.movement import MovementStrategy


class ChaseStrategy(ABC):
    @abstractmethod
    def select_movement(self, creature: Creature) -> MovementStrategy | None:
        pass


class GreedyChaseStrategy(ChaseStrategy):
    def select_movement(self, creature: Creature) -> MovementStrategy | None:
        available = creature.get_available_movements()
        if not available:
            return None
        return max(available, key=lambda m: m.get_speed())


class ChasePhase:
    def __init__(self, strategy: ChaseStrategy):
        self.strategy = strategy

    def execute(self, predator: Creature, prey: Creature) -> str:
        while predator.stamina > 0:
            predator_movement = self.strategy.select_movement(predator)
            if not predator_movement:
                return "escaped"

            predator_movement.execute(predator)
            prey_movement = self.strategy.select_movement(prey)
            if prey_movement:
                prey_movement.execute(prey)

            if predator.position >= prey.position:
                return "caught"

            if prey.position > END_POS:
                return "escaped"

        return "escaped"
