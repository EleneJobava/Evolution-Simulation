import random

from src.builder import create_random_creature
from src.chase import ChasePhase, GreedyChaseStrategy
from src.combat import CombatPhase
from src.constants import END_POS, MSG_PREDATOR_WON, MSG_PREY_ESCAPED, START_POS


class Simulation:
    def __init__(self):
        self.chase_phase = ChasePhase(GreedyChaseStrategy())
        self.combat_phase = CombatPhase()

    def run_single(self) -> dict[str, str]:
        predator = create_random_creature()
        predator.position = START_POS
        print(f"Predator at {predator.position}: {predator}")

        prey = create_random_creature()
        prey.position = random.randint(START_POS, END_POS)
        print(f"Prey at {prey.position}: {prey}")

        chase_result = self.chase_phase.execute(predator, prey)

        if chase_result == "escaped":
            print(MSG_PREY_ESCAPED)
            return {"result": "prey_escaped"}

        print("Fight begins!")
        fight_result = self.combat_phase.execute(predator, prey)

        if fight_result == "predator_wins":
            print(MSG_PREDATOR_WON)
            return {"result": "predator_wins"}
        else:
            print(MSG_PREY_ESCAPED)
            return {"result": "prey_wins"}

    def run_multiple(self, count: int) -> list[dict[str, str]]:
        results = []
        for i in range(count):
            print(f"\n{'=' * 50}")
            print(f"Simulation {i + 1}")
            print("=" * 50)
            result = self.run_single()
            results.append(result)
        return results
