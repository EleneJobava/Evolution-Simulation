from src.builder import CreatureBuilder, create_random_creature
from src.constants import (
    MAX_HEALTH,
    MAX_LEGS,
    MAX_STAMINA,
    MAX_WINGS,
    MIN_HEALTH,
    MIN_LEGS,
    MIN_STAMINA,
    MIN_WINGS,
    TEETH_SHARPNESS_VALUES,
    ClawSize,
)


class TestCreatureBuilder:
    def test_builder_creates_creature(self):
        creature = CreatureBuilder().build()
        assert creature is not None

    def test_builder_with_health(self):
        creature = CreatureBuilder().with_health(80).build()
        assert creature.health == 80

    def test_builder_with_stamina(self):
        creature = CreatureBuilder().with_stamina(120).build()
        assert creature.stamina == 120

    def test_builder_with_legs(self):
        creature = CreatureBuilder().with_legs(4).build()
        assert creature.legs == 4

    def test_builder_with_wings(self):
        creature = CreatureBuilder().with_wings(2).build()
        assert creature.wings == 2

    def test_builder_with_claws(self):
        creature = CreatureBuilder().with_claws(ClawSize.BIG).build()
        assert creature.claws == ClawSize.BIG

    def test_builder_with_teeth(self):
        creature = CreatureBuilder().with_teeth(9).build()
        assert creature.teeth_sharpness == 9

    def test_builder_chaining(self):
        creature = (
            CreatureBuilder()
            .with_health(90)
            .with_stamina(110)
            .with_legs(3)
            .with_wings(2)
            .with_claws(ClawSize.MEDIUM)
            .with_teeth(6)
            .build()
        )

        assert creature.health == 90
        assert creature.stamina == 110
        assert creature.legs == 3
        assert creature.wings == 2
        assert creature.claws == ClawSize.MEDIUM
        assert creature.teeth_sharpness == 6


class TestRandomCreatureCreation:
    def test_create_random_creature_returns_creature(self):
        creature = create_random_creature()
        assert creature is not None

    def test_random_creature_has_valid_health(self):
        creature = create_random_creature()
        assert MIN_HEALTH <= creature.health <= MAX_HEALTH

    def test_random_creature_has_valid_stamina(self):
        creature = create_random_creature()
        assert MIN_STAMINA <= creature.stamina <= MAX_STAMINA

    def test_random_creature_has_valid_legs(self):
        creature = create_random_creature()
        assert MIN_LEGS <= creature.legs <= MAX_LEGS

    def test_random_creature_has_valid_wings(self):
        creature = create_random_creature()
        assert MIN_WINGS <= creature.wings <= MAX_WINGS

    def test_random_creature_has_valid_teeth(self):
        creature = create_random_creature()
        assert creature.teeth_sharpness in TEETH_SHARPNESS_VALUES

    def test_random_creature_claws_optional(self):
        creature = create_random_creature()
        assert creature.claws is None or isinstance(creature.claws, ClawSize)

    def test_multiple_random_creatures_differ(self):
        creatures = [create_random_creature() for _ in range(10)]
        healths = {c.health for c in creatures}
        assert len(healths) > 1, "All creatures have same health - not random enough"
