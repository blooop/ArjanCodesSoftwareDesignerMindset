import random
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import StrEnum


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


class EnemyFactory(ABC):
    @abstractmethod
    def spawn(self) -> Enemy:
        pass


class EasyEnemyFactory(EnemyFactory):
    def spawn(self) -> Enemy:
        enemy_type = random.choice([EnemyType.KNIGHT, EnemyType.ARCHER])
        health = random.randint(30, 60)
        attack_power = random.randint(20, 40)
        defense = random.randint(10, 20)
        return Enemy(enemy_type, health, attack_power, defense)


class MediumEnemyFactory(EnemyFactory):
    def spawn(self) -> Enemy:
        enemy_type = random.choice(
            [EnemyType.KNIGHT, EnemyType.ARCHER, EnemyType.WIZARD]
        )
        health = random.randint(40, 80)
        attack_power = random.randint(40, 60)
        defense = random.randint(20, 40)
        return Enemy(enemy_type, health, attack_power, defense)


class HardEnemyFactory(EnemyFactory):
    def spawn(self) -> Enemy:
        enemy_type = EnemyType.WIZARD
        health = random.randint(60, 100)
        attack_power = random.randint(50, 80)
        defense = random.randint(40, 80)
        return Enemy(enemy_type, health, attack_power, defense)


def main() -> None:
    easy_factory = EasyEnemyFactory()
    for _ in range(5):
        enemy = easy_factory.spawn()
        print(enemy)

    medium_factory = MediumEnemyFactory()
    for _ in range(5):
        enemy = medium_factory.spawn()
        print(enemy)

    hard_factory = HardEnemyFactory()
    for _ in range(5):
        enemy = hard_factory.spawn()
        print(enemy)


if __name__ == "__main__":
    main()
