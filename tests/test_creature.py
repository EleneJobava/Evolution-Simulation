from src.constants import ClawSize
from src.creature import Creature


def test_creature_initialization():
    creature = Creature()
    assert creature.health == 100
    assert creature.stamina == 100
    assert creature.position == 0
    assert creature.legs == 0
    assert creature.wings == 0
    assert creature.claws is None
    assert creature.teeth_sharpness == 0
    assert creature.base_attack_power == 10


def test_calculate_attack_power():
    creature = Creature()

    assert creature.calculate_attack_power() == 10

    creature.teeth_sharpness = 3
    assert creature.calculate_attack_power() == 13

    creature.claws = ClawSize.SMALL
    assert creature.calculate_attack_power() == 26  # 13 * 2

    creature.claws = ClawSize.MEDIUM
    assert creature.calculate_attack_power() == 39  # 13 * 3

    creature.claws = ClawSize.BIG
    assert creature.calculate_attack_power() == 52  # 13 * 4


def test_attack():
    attacker = Creature()
    defender = Creature()

    initial_health = defender.health
    attacker.attack(defender)

    assert defender.health == initial_health - attacker.calculate_attack_power()


def test_str_representation():
    creature = Creature()
    creature.legs = 2
    creature.wings = 1
    creature.claws = ClawSize.SMALL
    creature.teeth_sharpness = 6

    str_rep = str(creature)
    assert "Health: 100" in str_rep
    assert "Stamina: 100" in str_rep
    assert "Legs: 2" in str_rep
    assert "Wings: 1" in str_rep
    assert "Claws: SMALL" in str_rep
    assert "Teeth: +6" in str_rep
