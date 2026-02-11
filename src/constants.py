from enum import Enum

START_POS = 0
END_POS = 100

MIN_STAMINA = 50
MAX_STAMINA = 100
MIN_HEALTH = 50
MAX_HEALTH = 100

MIN_LEGS = 0
MAX_LEGS = 2
MIN_WINGS = 0
MAX_WINGS = 2


class MovementType(Enum):
    CRAWL = "Crawling"
    HOP = "Hopping"
    WALK = "Walking"
    RUN = "Running"
    FLY = "Flying"


MOVEMENT_REQUIREMENTS = {
    MovementType.CRAWL: {"min_legs": 0, "min_wings": 0, "min_stamina": 0},
    MovementType.HOP: {"min_legs": 1, "min_wings": 0, "min_stamina": 20},
    MovementType.WALK: {"min_legs": 2, "min_wings": 0, "min_stamina": 40},
    MovementType.RUN: {"min_legs": 2, "min_wings": 0, "min_stamina": 60},
    MovementType.FLY: {"min_legs": 0, "min_wings": 2, "min_stamina": 80},
}

MOVEMENT_STATS = {
    MovementType.CRAWL: {"stamina_cost": 1, "speed": 1},
    MovementType.HOP: {"stamina_cost": 2, "speed": 3},
    MovementType.WALK: {"stamina_cost": 2, "speed": 4},
    MovementType.RUN: {"stamina_cost": 4, "speed": 6},
    MovementType.FLY: {"stamina_cost": 4, "speed": 8},
}


class ClawSize(Enum):
    SMALL = 2
    MEDIUM = 3
    BIG = 4


TEETH_SHARPNESS_VALUES = [3, 6, 9]

NUM_SIMULATIONS = 100

MSG_PREY_ESCAPED = "Pray ran into infinity"
MSG_PREDATOR_WON = "Some R-rated things have happened"
