import random
from dataclasses import dataclass
from enum import StrEnum


class SpawnType(StrEnum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


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


def easy_spawn() -> Enemy:
    enemy_type = random.choice([EnemyType.KNIGHT, EnemyType.ARCHER])
    health = random.randint(30, 60)
    attack_power = random.randint(20, 40)
    defense = random.randint(10, 20)
    return Enemy(enemy_type, health, attack_power, defense)


def medium_spawn() -> Enemy:
    enemy_type = random.choice([EnemyType.KNIGHT, EnemyType.ARCHER, EnemyType.WIZARD])
    health = random.randint(40, 80)
    attack_power = random.randint(40, 60)
    defense = random.randint(20, 40)
    return Enemy(enemy_type, health, attack_power, defense)


def hard_spawn() -> Enemy:
    enemy_type = EnemyType.WIZARD
    health = random.randint(60, 100)
    attack_power = random.randint(50, 80)
    defense = random.randint(40, 80)
    return Enemy(enemy_type, health, attack_power, defense)


SPAWN_FUNCTIONS = {
    SpawnType.EASY: easy_spawn,
    SpawnType.MEDIUM: medium_spawn,
    SpawnType.HARD: hard_spawn,
}


def spawn_enemies(spawn_type: SpawnType, count: int) -> list[Enemy]:
    spawn_function = SPAWN_FUNCTIONS[spawn_type]
    return [spawn_function() for _ in range(count)]


def main() -> None:
    # spawn some easy enemies
    spawn_type = SpawnType.EASY
    enemies = spawn_enemies(spawn_type, 5)
    print(enemies)


if __name__ == "__main__":
    main()
