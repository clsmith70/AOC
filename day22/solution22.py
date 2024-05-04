# solution22.py

import pathlib
import sys

FIGHT_INIT = {
    'player_hit': 50,
    'player_mana': 500,
    'player_armor': 0,

    'boss_hit': 55,
    'boss_damage': 8,

    'shield_turns': 0,
    'poison_turns': 0,
    'recharge_turns': 0,

    'active_spells': [],
    'mana_spent': 0
}

SPELL_DATA = {
    'magic missile': {
        'cost': 53,
        'damage': 4,
        'armor': 0,
        'heal': 0,
        'mana': 0,
        'turns': 1
        },
    'drain': {
        'cost': 73,
        'damage': 2,
        'armor': 0,
        'heal': 2,
        'mana': 0,
        'turns': 1
        },
    'shield': {
        'cost': 113,
        'damage': 0,
        'armor': 7,
        'heal': 0,
        'mana': 0,
        'turns': 6
        },
    'poison': {
        'cost': 173,
        'damage': 3,
        'armor': 0,
        'heal': 0,
        'mana': 0,
        'turns': 6
        },
    'recharge': {
        'cost': 229,
        'damage': 0,
        'armor': 0,
        'heal': 0,
        'mana': 101,
        'turns': 5
    }
}

def get_least_mana(fight: dict, difficult: bool=False) -> int:
    """Find the least mana you can spend and win"""
    
    minimum_spent = 999999
    fights = [fight]
    while len(fights):
        fights, minimum_spent = \
            get_all_fights(fights, minimum_spent, difficult)
    return minimum_spent
    
def get_all_fights(fights: list, minimum_spent: int, 
                   difficult: bool) -> tuple[list, int]:
    """Play the main part of the game"""

    new_fights = []
    for fight in fights:
        if difficult:
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

def get_all_spells(fight: dict, minimum_spent: int, 
                   new_fights: list) -> int:
    """Get all castable spells (have enough mana and not in use)"""

    castable_spells = [spell for spell in SPELL_DATA.keys()
                if SPELL_DATA[spell]['cost'] <= fight['player_mana']]
    
    if fight['shield_turns'] and 'sheild' in castable_spells:
        castable_spells.remove('shield')
    if fight['poison_turns'] and 'poison' in castable_spells:
        castable_spells.remove('poison')
    if fight['recharge_turns'] and 'recharge' in castable_spells:
        castable_spells.remove('recharge')

    for spell in castable_spells:
        current_fight = fight.copy()
        current_fight['active_spells'] = \
            list(current_fight['active_spells']) + [spell]
        current_fight['mana_spent'] += SPELL_DATA[spell]['cost']

        player_attack(current_fight, spell)
        fightover, minimum_spent = check_fight_over(current_fight, 
                                                    minimum_spent)
        if fightover:
            continue

        if current_fight['mana_spent'] > minimum_spent:
            continue

        set_effect(current_fight)
        fightover, minimum_spent = check_fight_over(current_fight, 
                                                    minimum_spent)
        if fightover:
            continue

        boss_attack(current_fight)
        fightover, minimum_spent = check_fight_over(current_fight, 
                                                    minimum_spent)
        if fightover:
            continue

        new_fights.append(current_fight)

    return minimum_spent

def set_effect(fight: dict):
    """Set effect of multi-turn spells"""

    if fight['shield_turns']:
        fight['shield_turns'] -= 1
        if fight['shield_turns'] == 0:
            fight['player_armor'] = 0
    
    if fight['poison_turns']:
        fight['boss_hit'] -= SPELL_DATA['poison']['damage']
        fight['poison_turns'] -= 1

    if fight['recharge_turns']:
        fight['player_mana'] += SPELL_DATA['recharge']['mana']
        fight['recharge_turns'] -= 1

def player_attack(fight: dict, spell: str):
    """The hero attacks the boss"""

    fight['player_mana'] -= SPELL_DATA[spell]['cost']
    fight['player_armor'] += SPELL_DATA[spell]['armor']

    if SPELL_DATA[spell]['turns'] > 1:
        fight[spell + '_turns'] = SPELL_DATA[spell]['turns']

    if spell in ('magic missile', 'drain'):
        fight['boss_hit'] -= SPELL_DATA[spell]['damage']
        fight['player_hit'] += SPELL_DATA[spell]['heal']

def check_fight_over(fight: dict, minimum_spent: int) -> tuple:
    """See if either player is out of hit points"""

    if fight['boss_hit'] <= 0:
        minimum_spent = min(fight['mana_spent'], minimum_spent)
        return 1, minimum_spent
    if fight['player_hit'] <= 0:
        return 2, minimum_spent
    return 0, minimum_spent

def boss_attack(fight: dict):
    """The boss attacks the hero"""

    fight['player_hit'] -= max(fight['boss_damage'] - 
                               fight['player_armor'], 1)

def part1() -> str:
    """Solve part 1"""

    return get_least_mana(FIGHT_INIT.copy(), difficult=False)

def part2() -> str:
    """Solve part 2"""

    return get_least_mana(FIGHT_INIT.copy(), difficult=True)

def solve() -> list:
    """Solve the puzzle for the given input"""

    solution1 = f"Part 1: {part1()}"
    solution2 = f"Part 2: {part2()}"

    return solution1, solution2

if __name__ == "__main__":
    print("\n\tFIGHT!\n")
    solutions = solve()
    print("\n".join(str(solution) for solution in solutions))