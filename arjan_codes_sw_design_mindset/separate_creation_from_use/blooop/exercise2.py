from dataclasses import dataclass
from strenum import StrEnum
from enum import auto


class EnemyType(StrEnum):
    KNIGHT = auto()
    ARCHER = auto()
    WIZARD = auto()


class SpawnType(StrEnum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()


@dataclass
class Enemy:
    enemy_type: EnemyType
    health: int
    attack_power: int
    defense: int


def spawn_easy(enemy_type: EnemyType):
    return Enemy(enemy_type, health=100, attack_power=5, defense=5)


def spawn_medium(enemy_type: EnemyType):
    return Enemy(enemy_type, health=200, attack_power=50, defense=50)


def spawn_hard(enemy_type: EnemyType):
    return Enemy(enemy_type, health=300, attack_power=500, defense=500)


enemy_mapping = {
    SpawnType.EASY: [[EnemyType.ARCHER, EnemyType.KNIGHT]],
    SpawnType.MEDIUM: [EnemyType.ARCHER, EnemyType.KNIGHT, EnemyType.WIZARD],
    SpawnType.HARD: [EnemyType.WIZARD],
}

spawn_mapping = {
    SpawnType.EASY: spawn_easy,
    SpawnType.MEDIUM: spawn_medium,
    SpawnType.HARD: spawn_hard,
}


def spawn(spawn_type: SpawnType, count: int = 1):
    enemies = []
    for c in range(count):
        print(f"spawning enemy {c}")
        enemies.append(spawn_mapping[spawn_type](enemy_mapping[spawn_type]))
    for e in enemies:
        print(e)
    return enemies


def main() -> None:
    spawn(SpawnType.EASY)
    spawn(SpawnType.MEDIUM)
    spawn(SpawnType.HARD)


if __name__ == "__main__":
    main()
