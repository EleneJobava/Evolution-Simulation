from src.builder import CreatureBuilder
from src.combat import CombatPhase
from src.constants import ClawSize


class TestCombatPhase:
    def test_stronger_predator_wins(self):
        predator = CreatureBuilder().with_health(100).with_claws(ClawSize.BIG).with_teeth(9).build()

        prey = CreatureBuilder().with_health(50).build()

        combat = CombatPhase()
        result = combat.execute(predator, prey)

        assert result == "predator_wins"

    def test_stronger_prey_wins(self):
        predator = CreatureBuilder().with_health(30).build()

        prey = CreatureBuilder().with_health(100).with_claws(ClawSize.BIG).with_teeth(9).build()

        combat = CombatPhase()
        result = combat.execute(predator, prey)

        assert result == "prey_wins"

    def test_combat_ends_when_health_depleted(self):
        predator = CreatureBuilder().with_health(100).build()
        prey = CreatureBuilder().with_health(100).build()

        combat = CombatPhase()
        result = combat.execute(predator, prey)

        assert result in ["predator_wins", "prey_wins"]
        assert predator.health <= 0 or prey.health <= 0
