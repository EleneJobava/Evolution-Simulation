from src.creature import Creature


class CombatPhase:
    @staticmethod
    def execute(predator: Creature, prey: Creature) -> str:
        while predator.health > 0 and prey.health > 0:
            predator.attack(prey)
            if prey.health <= 0:
                return "predator_wins"

            prey.attack(predator)
            if predator.health <= 0:
                return "prey_wins"

        return "predator_wins" if prey.health <= 0 else "prey_wins"
