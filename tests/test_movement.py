from src.creature import Creature
from src.movement import CrawlMovement, FlyMovement, HopMovement, RunMovement, WalkMovement, create_all_movements


class TestCrawlMovement:
    def test_crawl_always_available_with_stamina(self):
        creature = Creature()
        creature.stamina = 10
        creature.legs = 0
        creature.wings = 0

        crawl = CrawlMovement()
        assert crawl.can_execute(creature) is True

    def test_crawl_not_available_without_stamina(self):
        creature = Creature()
        creature.stamina = 0

        crawl = CrawlMovement()
        assert crawl.can_execute(creature) is False

    def test_crawl_execution_updates_state(self):
        creature = Creature()
        creature.stamina = 10
        creature.position = 0

        crawl = CrawlMovement()
        result = crawl.execute(creature)

        assert result is True
        assert creature.stamina == 9
        assert creature.position == 1

    def test_crawl_speed_is_one(self):
        crawl = CrawlMovement()
        assert crawl.get_speed() == 1


class TestHopMovement:
    def test_hop_requires_one_leg(self):
        creature = Creature()
        creature.legs = 0
        creature.stamina = 100

        hop = HopMovement()
        assert hop.can_execute(creature) is False

        creature.legs = 1
        assert hop.can_execute(creature) is True

    def test_hop_requires_minimum_stamina(self):
        creature = Creature()
        creature.legs = 2
        creature.stamina = 19

        hop = HopMovement()
        assert hop.can_execute(creature) is False

        creature.stamina = 20
        assert hop.can_execute(creature) is True

    def test_hop_execution(self):
        creature = Creature()
        creature.legs = 1
        creature.stamina = 50
        creature.position = 0

        hop = HopMovement()
        hop.execute(creature)

        assert creature.stamina == 48
        assert creature.position == 3


class TestWalkMovement:
    def test_walk_requires_two_legs(self):
        creature = Creature()
        creature.legs = 1
        creature.stamina = 100

        walk = WalkMovement()
        assert walk.can_execute(creature) is False

        creature.legs = 2
        assert walk.can_execute(creature) is True

    def test_walk_requires_minimum_stamina(self):
        creature = Creature()
        creature.legs = 2
        creature.stamina = 39

        walk = WalkMovement()
        assert walk.can_execute(creature) is False

        creature.stamina = 40
        assert walk.can_execute(creature) is True


class TestRunMovement:
    def test_run_requires_two_legs(self):
        creature = Creature()
        creature.legs = 1
        creature.stamina = 100

        run = RunMovement()
        assert run.can_execute(creature) is False

    def test_run_requires_minimum_stamina(self):
        creature = Creature()
        creature.legs = 2
        creature.stamina = 59

        run = RunMovement()
        assert run.can_execute(creature) is False

        creature.stamina = 60
        assert run.can_execute(creature) is True

    def test_run_execution(self):
        creature = Creature()
        creature.legs = 2
        creature.stamina = 100
        creature.position = 0

        run = RunMovement()
        run.execute(creature)

        assert creature.stamina == 96
        assert creature.position == 6


class TestFlyMovement:
    def test_fly_requires_two_wings(self):
        creature = Creature()
        creature.wings = 1
        creature.stamina = 100

        fly = FlyMovement()
        assert fly.can_execute(creature) is False

        creature.wings = 2
        assert fly.can_execute(creature) is True

    def test_fly_requires_minimum_stamina(self):
        creature = Creature()
        creature.wings = 2
        creature.stamina = 79

        fly = FlyMovement()
        assert fly.can_execute(creature) is False

        creature.stamina = 80
        assert fly.can_execute(creature) is True

    def test_fly_execution(self):
        creature = Creature()
        creature.wings = 2
        creature.stamina = 100
        creature.position = 0

        fly = FlyMovement()
        fly.execute(creature)

        assert creature.stamina == 96
        assert creature.position == 8


class TestMovementFactory:
    def test_create_all_movements_returns_five_strategies(self):
        movements = create_all_movements()
        assert len(movements) == 5

    def test_create_all_movements_returns_correct_types(self):
        movements = create_all_movements()
        types = [type(m).__name__ for m in movements]

        assert "CrawlMovement" in types
        assert "HopMovement" in types
        assert "WalkMovement" in types
        assert "RunMovement" in types
        assert "FlyMovement" in types
