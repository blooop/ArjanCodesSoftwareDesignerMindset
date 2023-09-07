from dataclasses import dataclass
from strenum import StrEnum
from enum import auto
import strenum
from random import choice

class EnemyType(StrEnum):
    KNIGHT = auto()
    ARCHER = auto()
    WIZARD = auto()

class SpawnType(StrEnum):
    EASY = auto()
    MEDIUM =auto()
    HARD=auto()

@dataclass
class Enemy:
    enemy_type: EnemyType
    health: int
    attack_power: int
    defense: int


def spawn_easy(enemy_type:EnemyType):

    return Enemy(enemy_type, health=100, attack_power=5, defense=5)

def spawn_medium(enemy_type:EnemyType):

    return Enemy(enemy_type, health=200, attack_power=50, defense=50)

def spawn_hard(enemy_type:EnemyType):

    return Enemy(enemy_type, health=300, attack_power=500, defense=500)




def spawn(spawn_type:SpawnType):
    enemies =[]
    match spawn_type:
        case SpawnType.EASY:
            enemies.append(spawn_easy(choice([EnemyType.ARCHER,EnemyType.KNIGHT])))
        case SpawnType.MEDIUM:
            enemies.append(spawn_medium(choice([EnemyType.ARCHER,EnemyType.KNIGHT,EnemyType.WIZARD])))
        case SpawnType.HARD:
            enemies.append(spawn_hard(choice([EnemyType.WIZARD])))
    for e in enemies:
        print(e)
    return enemies

                




def main() -> None:
    spawn(SpawnType.EASY)
    spawn(SpawnType.MEDIUM)
    spawn(SpawnType.HARD)
    


if __name__ == "__main__":
    main()
