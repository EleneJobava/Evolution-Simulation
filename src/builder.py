import random

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
from src.creature import Creature


class CreatureBuilder:
    def __init__(self) -> None:
        self.creature = Creature()

    def with_health(self, health: int) -> "CreatureBuilder":
        self.creature.health = health
        return self

    def with_stamina(self, stamina: int) -> "CreatureBuilder":
        self.creature.stamina = stamina
        return self

    def with_legs(self, legs: int) -> "CreatureBuilder":
        self.creature.legs = legs
        return self

    def with_wings(self, wings: int) -> "CreatureBuilder":
        self.creature.wings = wings
        return self

    def with_claws(self, claws: ClawSize) -> "CreatureBuilder":
        self.creature.claws = claws
        return self

    def with_teeth(self, sharpness: int) -> "CreatureBuilder":
        self.creature.teeth_sharpness = sharpness
        return self

    def build(self) -> Creature:
        return self.creature


def create_random_creature() -> Creature:
    builder = CreatureBuilder()

    builder.with_health(random.randint(MIN_HEALTH, MAX_HEALTH))
    builder.with_stamina(random.randint(MIN_STAMINA, MAX_STAMINA))
    builder.with_legs(random.randint(MIN_LEGS, MAX_LEGS))
    builder.with_wings(random.randint(MIN_WINGS, MAX_WINGS))

    if random.random() > 0.5:
        builder.with_claws(random.choice(list(ClawSize)))

    builder.with_teeth(random.choice(TEETH_SHARPNESS_VALUES))

    return builder.build()
