# solution14.py

import pathlib
import sys

def parse(puzzle_input: str) -> list:
    """Parse text input"""
    return [line for line in puzzle_input.split('\n')]

def build_entrant_list(data: list, entrant_list: dict) -> dict:
    """Split each line into a dict record

    The line includes information to fill in:
        - entrant name (entrant)
        - distance flown per second (distance)
        - duration of flight possible (fly_seconds)
        - duration of required rest (rest_seconds)
    Additional data added to each record:
        - total flight distance (total_distance)
        - a boolean to indicate flight [True] or rest [False] (flying)
        - seconds flown (flown)
        - seconds rested (rested)
        - points acheived [for part 2] (points)
    """

    for line in data:
        # split the line
        entrant, _,_,distance,_,_,fly_seconds,*_,rest_seconds,_ = line.split()
        # convert numerical data to int type
        distance = int(distance)
        fly_seconds = int(fly_seconds)
        rest_seconds = int(rest_seconds)
        total_distance, flying, flown, rested, points = 0, True, 0, 0, 0

        entrant_list[entrant] = [distance,fly_seconds,rest_seconds,
                                 total_distance,flying,flown,rested,points]

def run_race(contender: list, duration: int, type: str="distance") -> list:
    """Runs the race

    A race is run by distance (part 1) or points (part 2)
    A distance race:
        - runs the entire race for each reindeer passed in
        - tracks rest and flight seconds in batches
        - tracks total distance when flying
    A points race:
        - runs the race per second and per reindeer passed in
        - tracks distance per second
        - points are scored in the calling function
    """
    
    if type == 'distance':
        # track when at rest
        at_rest = False
        # keep a timer
        clock = 0
        # track the distance
        total_distance = 0

        # while there is still time to race
        while clock < duration:
            # if the entrant is resting, clock it
            if at_rest:
                at_rest = not at_rest
                clock += contender[2]
            # if the entrant is flying, clock time and distance
            else:
                at_rest = not at_rest
                clock += contender[1]
                total_distance += contender[0] * contender[1]

        # update the entrants total flying distance
        contender[3] = total_distance

    elif type == 'points':
        # get values from the entrant data
        distance,fly_seconds,rest_seconds,_, \
            flying,flown,rested,_ = contender
        # if the entrant is flying
        if flying:
            # if they've flown as long as they can
            # set them to resting and add a resting second
            if flown == fly_seconds:
                contender[4] = False
                contender[6] = 1
            # otherwise, clock the second and km/s flown
            else:
                contender[5] += 1
                contender[3] += distance
        else:
            # if they've rested for the required time
            # set flying to true, add a second of flying
            # and add the km/s distance flown
            if rested == rest_seconds:
                contender[4] = True
                contender[5] = 1
                contender[3] += distance
            # otherwise, clock another resting second
            else:
                contender[6] += 1

    return contender

def part1(data: list, race_time: int=2503) -> tuple:
    """Solve part 1"""

    entrants = dict()
    winner = ""
    distance = 0

    build_entrant_list(data, entrants)

    # loop over all entrants
    for reindeer in entrants.keys():
        # run their distance race
        entrants[reindeer] = run_race(entrants[reindeer], race_time)
        # compare distance to the tracked distane
        if entrants[reindeer][3] > distance:
            # if this one is further, capture distance and name
            distance = entrants[reindeer][3]
            winner = reindeer

    return winner, distance

def part2(data: list, race_time: int=2503) -> tuple:
    """Solve part 2"""

    entrants = dict()
    
    build_entrant_list(data, entrants)

    # for each second in race_time
    for _ in range(race_time):
        # loop over all entrants
        for reindeer in entrants.keys():
            # run the points race for this second
            entrants[reindeer] = run_race(entrants[reindeer], _, 'points')
            
        furthest_distance = -1
        leader = None

        # loop over entrants again
        for reindeer in entrants.keys():
            # get the current distance
            distance = entrants[reindeer][3]
            # compare it to the furthest_distance
            if distance >= furthest_distance:
                # if it is >= the current furthest distance,
                # capture the distance and name
                furthest_distance = distance
                leader = reindeer

        # loop over entrants one more time to award points
        for reindeer in entrants.keys():
            # if the entrant's distance is equal to furthest distance
            if entrants[reindeer][3] == furthest_distance:
                # score a point
                entrants[reindeer][7] += 1

    winner = ""
    points = 0
    # loop one last time to find the winner by score
    for reindeer in entrants.keys():
        # if points earned > points tracked
        if entrants[reindeer][7] > points:
            # save the point value and current entrant
            points = entrants[reindeer][7]
            winner = reindeer

    return winner, points

def solve(puzzle_input: str) -> list:
    """Solve the puzzle for the given input"""
    
    data = parse(puzzle_input=puzzle_input)
    solution1 = f"Part 1: {part1(data=data)}"
    solution2 = f"Part 2: {part2(data=data)}"

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input=puzzle_input)
        print("\n".join(str(solution) for solution in solutions))