# solution21.py

import pathlib
import sys

from collections import namedtuple

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    
    return [line for line in puzzle_input.split('\n')]

def turn (hero_hit: int, hero_damage: int, hero_armor: int,
          boss_hit: int, boss_damage: int, boss_armor: int) -> bool:
    """Take turns attacking and defending"""
    boss_damage_per_turn = max([1, hero_damage - boss_armor])
    hero_damage_per_turn = max([1, boss_damage - hero_armor])

    n, remain = divmod(boss_hit, boss_damage_per_turn)
    if remain == 0:
        n -= 1
    if hero_damage_per_turn * (n) >= hero_hit:
        # does the hero survive?
        return False
    return True

def fight(data: list) -> tuple:
    """Fight and return winning (min) and losing (max) costs"""
    Item = namedtuple('Item', ['name','cost','damage','armor'])
    hero_hp = 100
    boss_hp = int(data[0].split(': ')[1])
    boss_damage = int(data[1].split(': ')[1])
    boss_armor = int(data[2].split(': ')[1])

    min_gold = 356 # the most you can spend according to the rules
    max_gold = 0

    Weapons = [Item('Dagger', 8, 4, 0),
               Item('Shortsword', 10, 5, 0),
               Item('Warhammer', 25, 6, 0),
               Item('Longsword', 40, 7, 0),
               Item('Greataxe', 74, 8, 0)]
    
    Armor = [Item('None', 0, 0, 0),
            Item('Leather', 13, 0, 1),
            Item('Chainmail', 31, 0, 2),
            Item('Splintmail', 53, 0, 3),
            Item('Bandedmail', 75, 0, 4),
            Item('Platemail', 102, 0, 5)]

    Rings = [Item('None1', 0, 0, 0),
            Item('None2', 0, 0, 0),
            Item('Damage +1', 25, 1, 0),
            Item('Damage +2', 50, 2, 0),
            Item('Damage +3', 100, 3, 0),
            Item('Defense +1', 20, 0, 1),
            Item('Defense +2', 40, 0, 2),
            Item('Defense +3', 80, 0, 3)]
    
    for weapon in Weapons: # get one
        for armor in Armor: # get zero or one
            for ring1 in Rings: # get zero or one
                for ring2 in Rings: # get zero or one, no duplicates
                    if ring1.name == ring2.name: # try again
                        continue

                    hero_damage = sum([weapon.damage, ring1.damage,
                                         ring2.damage])
                    hero_armor = sum([armor.armor, ring1.armor, ring2.armor])
                    cost = sum([weapon.cost, armor.cost, 
                                ring1.cost, ring2.cost])
                    
                    if turn(hero_hp, hero_damage, hero_armor, boss_hp,
                            boss_damage, boss_armor): # hero won
                        min_gold = min(cost, min_gold)
                    else: # boss won
                        max_gold = max(cost, max_gold)

    return min_gold, max_gold

def solve(puzzle_input: str) -> list:
    """Solve the puzzle for the given input"""

    data = parse(puzzle_input=puzzle_input)
    gold1, gold2 = fight(data=data)
    solution1 = f"Part 1: {gold1}"
    solution2 = f"Part 2: {gold2}"

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input=puzzle_input)
        print("\n".join(str(solution) for solution in solutions))