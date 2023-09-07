from dataclasses import dataclass
from strenum import StrEnum
from typing import Callable


class EnemyType(StrEnum):
    KNIGHT = "knight"
    ARCHER = "archer"
    WIZARD = "wizard"


@dataclass
class Enemy:
    enemy_type: EnemyType
    health: int
    attack_power: int
    defense: int


Level = Callable[[EnemyType], Enemy]


def low(enemy_type: EnemyType) -> Enemy:
    return Enemy(enemy_type, health=1, attack_power=1, defense=1)


def middle(enemy_type: EnemyType) -> Enemy:
    return Enemy(enemy_type, health=50, attack_power=5, defense=3)


def high(enemy_type: EnemyType) -> Enemy:
    return Enemy(enemy_type, health=100, attack_power=10, defense=5)


def SpawnKnight(enemy_level: Level) -> Enemy:
    return enemy_level(EnemyType.KNIGHT)


def SpawnWizard(enemy_level: Level) -> Enemy:
    return enemy_level(EnemyType.WIZARD)


def SpawnArcher(enemy_level: Level) -> Enemy:
    return enemy_level(EnemyType.ARCHER)


SPAWN_ENEMIES = {
    "easy_knight": SpawnKnight(low),
    "easy_archer": SpawnArcher(low),
    "medium_knight": SpawnKnight(middle),
    "medium_archer": SpawnArcher(middle),
    "medium_wizard": SpawnWizard(middle),
    "hard_wizard": SpawnWizard(high),
}


def main() -> None:
    enemy = SPAWN_ENEMIES["easy_knight"]
    print(enemy)


if __name__ == "__main__":
    main()
