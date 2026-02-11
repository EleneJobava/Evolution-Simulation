from src.builder import CreatureBuilder
from src.chase import ChasePhase, GreedyChaseStrategy


class TestGreedyChaseStrategy:
    def test_selects_fastest_movement(self):
        creature = CreatureBuilder().with_legs(2).with_stamina(100).build()

        strategy = GreedyChaseStrategy()
        movement = strategy.select_movement(creature)

        assert movement.get_speed() == 6

    def test_returns_none_when_no_movements_available(self):
        creature = CreatureBuilder().with_stamina(0).build()

        strategy = GreedyChaseStrategy()
        movement = strategy.select_movement(creature)

        assert movement is None


class TestChasePhase:
    def test_predator_catches_slow_prey(self):
        predator = CreatureBuilder().with_legs(2).with_stamina(100).build()
        predator.position = 0

        prey = CreatureBuilder().with_legs(0).with_stamina(100).build()
        prey.position = 5

        chase = ChasePhase(GreedyChaseStrategy())
        result = chase.execute(predator, prey)

        assert result == "caught"

    def test_prey_escapes_when_predator_exhausted(self):
        predator = CreatureBuilder().with_legs(2).with_stamina(10).build()
        predator.position = 0

        prey = CreatureBuilder().with_legs(2).with_stamina(100).build()
        prey.position = 100

        chase = ChasePhase(GreedyChaseStrategy())
        result = chase.execute(predator, prey)

        assert result == "escaped"

    def test_fast_prey_can_escape(self):
        predator = CreatureBuilder().with_legs(2).with_stamina(50).build()
        predator.position = 0

        prey = CreatureBuilder().with_wings(2).with_stamina(100).build()
        prey.position = 20

        chase = ChasePhase(GreedyChaseStrategy())
        result = chase.execute(predator, prey)

        assert result == "escaped"
