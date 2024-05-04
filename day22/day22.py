# scripts/day22.py

from typing import cast
import pathlib
import sys

SPELL_PRICES = {
    'magic missile': 53,
    'drain': 73,
    'shield': 113,
    'poison': 173,
    'recharge': 229
}

FIGHT_INIT = {
    'player_hit': 50,
    'player_mana': 500,
    'player_armor': 0,

    'boss_hit': 55,
    'boss_damage': 8,

    'shield_timer': 0,
    'poison_timer': 0,
    'recharge_timer': 0,

    'active_spells': [],
    'mana_spent': 0
}

def get_minimum_mana(fight: dict, part2: bool = False) -> int:
    minimum_spent = 999999
    fights = [fight]
    while len(fights):
        fights, minimum_spent = get_all_fights(fights, minimum_spent, part2)
    return minimum_spent

def get_all_fights(fights: list, minimum_spent: int, part2: bool) -> tuple[list, int]:
    new_fights = []
    for fight in fights:
        if part2:
            fight['player_hit'] -= 1
        fightover, minimum_spent = check_fight_over(fight, minimum_spent)
        if fightover:
            continue

        set_effect(fight)
        fightover, minimum_spent = check_fight_over(fight, minimum_spent)
        if fightover:
            continue

        minimum_spent = get_all_spells(fight, minimum_spent, new_fights)

    return new_fights, minimum_spent

def get_all_spells(fight: dict, minimum_spent: int, new_fights: list) -> int:
    castable_spells = [spell for spell, price in SPELL_PRICES.items()
            if price <= fight['player_mana']]
    if fight['shield_timer'] and 'shield' in castable_spells:
        castable_spells.remove('shield')
    if fight['poison_timer'] and 'poison' in castable_spells:
        castable_spells.remove('poison')
    if fight['recharge_timer'] and 'recharge' in castable_spells:
        castable_spells.remove('recharge')

    for spell in castable_spells:
        current_fight = fight.copy()
        current_fight['active_spells'] = list(current_fight['active_spells']) + [spell]
        current_fight['mana_spent'] += SPELL_PRICES[spell]

        player_attack(current_fight, spell)
        fightover, minimum_spent = check_fight_over(current_fight, minimum_spent)
        if fightover:
            continue

        if current_fight['mana_spent'] > minimum_spent:
            continue

        set_effect(current_fight)
        fightover, minimum_spent = check_fight_over(current_fight, minimum_spent)
        if fightover:
            continue

        boss_attack(current_fight)
        fightover, minimum_spent = check_fight_over(current_fight, minimum_spent)
        if fightover:
            continue

        new_fights.append(current_fight)
    return minimum_spent

def set_effect(fight: dict):
    if fight['shield_timer']:
        fight['shield_timer'] -= 1
        if fight['shield_timer'] == 0:
            fight['player_armor'] = 0

    if fight['poison_timer']:
        fight['boss_hit'] -= 3
        fight['poison_timer'] -= 1

    if fight['recharge_timer']:
        fight['player_mana'] += 101
        fight['recharge_timer'] -= 1

def player_attack(fight: dict, spell: str):
    if spell == 'magic missile':
        fight['boss_hit'] -= 4
    elif spell == 'drain':
        fight['boss_hit'] -= 2
        fight['player_hit'] += 2
    elif spell == 'shield':
        fight['shield_timer'] = 6
        fight['player_armor'] += 7
    elif spell == 'poison':
        fight['poison_timer'] = 6
    elif spell == 'recharge':
        fight['recharge_timer'] = 5
    fight['player_mana'] -= SPELL_PRICES[spell]

def check_fight_over(fight: dict, minimum_spent: int) -> tuple[int, int]:
    if fight['boss_hit'] <= 0:
        minimum_spent = min(fight['mana_spent'], minimum_spent)
        return 1, minimum_spent
    if fight['player_hit'] <= 0:
        return 2, minimum_spent
    return 0, minimum_spent

def boss_attack(fight: dict):
    fight['player_hit'] -= max(fight['boss_damage'] - fight['player_armor'], 1)

def part1() -> str:
    """Solve part 1"""
    return f"Part 1: {get_minimum_mana(FIGHT_INIT.copy(), part2=False)}"

def part2() -> str:
    """Solve part 2"""
    return f"Part 2: {get_minimum_mana(FIGHT_INIT.copy(), part2=True)}"

def solve():
    """Solve the puzzle for the given input."""
    solution1 = part1()
    solution2 = part2()

    return solution1, solution2

if __name__ == "__main__":
    print("\nDay 22")
    solutions = solve()
    print("\n".join(str(solution) for solution in solutions))
    print("\n")