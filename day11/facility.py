# facility.py

"""Class structure for 2016 day 11 solution"""
from enum import Enum
from typing import Union

class NuclearItem:
    """Base class for thermoelectric items"""

    def __init__(self, element: str) -> None:
        self._element = element

    def __str__(self) -> str:
        return f"{self.__class__.__name__} of {self._element}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(element='{self._element}')"

    def __eq__(self, other) -> bool:
        return repr(self) == repr(other)

    def __lt__(self, other) -> bool:
        return repr(self) < repr(other)

    def __hash__(self):
        return hash(repr(self))

    @property
    def get_element(self):
        """Return the element type of the object"""
        return self._element

    def is_compatible(self, other):
        """Check if the two objects can be in proximity"""
        if (self._element == other.get_element and
            type(self).__name__ != type(other).__name__):
            return True
        elif (self._element != other.get_element and
              type(self).__name__ == type(other).__name__):
            return True
        return False


class Generator(NuclearItem):
    """Thermoelectric Radioisotope Generator"""


class Microchip(NuclearItem):
    """Thermoelectric Radioisotope Michrochip"""


class Direction(Enum):
    """Direction indicator"""
    UP = 1
    DOWN = -1


class Elevator:
    """Nuclear item transport elevator"""

    MAX_FLOOR = 4

    class Slot:
        """Elevator slot for carrying NuclearItem objects"""

        def __init__(self, position: int):
            self._position = position
            self._item = None

        def load(self, item) -> bool:
            """Load an object into the slot"""
            if not self.has_item:
                self._item = item
                return True
            return False

        def unload(self) -> Union[NuclearItem, bool]:
            """Unload an object from the slot"""
            if self.has_item:
                item = self._item
                self._item = None
                return item
            return False

        def item(self) -> Union[NuclearItem, None]:
            """Return the item in the slot or None"""
            if self.has_item:
                return self._item
            return None

        def __repr__(self):
            if self._item:
                return f"{type(self).__name__}({repr(self._item)})"
            else:
                return f"{type(self).__name__}()"

        def __str__(self):
            if self._item:
                return f"{type(self).__name__} {self._position} " \
                    f"contains {str(self._item)}"
            else:
                return f"{type(self).__name__} {self._position} is Empty"

        @property
        def has_item(self):
            """Check if an item is in the slot"""
            if isinstance(self._item, NuclearItem):
                return True
            return False

    def __init__(self):
        self._slot1 = self.Slot(1)
        self._slot2 = self.Slot(2)
        self._floor = 1

    @property
    def can_move(self) -> bool:
        """
            Check the elevator status against the rules to determine if it
            can move between floors
        """
        if self._slot1.has_item or self._slot2.has_item:
            return True
        return False

    @property
    def is_full(self):
        """Check if both slots contain and item"""
        return (self._slot1.has_item and self._slot2.has_item)

    @property
    def get_floor(self):
        """Return the floor the elevator is currently on"""
        return self._floor

    def get_slots(self):
        """Return the content of the slots"""
        return str(self._slot1), str(self._slot2)

    def load_slot(self, position, item) -> bool:
        """Load a slot according to the rules"""
        if position == 1:
            # if both slots are empty, load it
            if not self._slot1.has_item:
                if not self._slot2.has_item:
                    self._slot1.load(item)
                    return True
                # if one slot has an item in it, check that it is compatible
                elif self._slot2.item().is_compatible(item):
                    # if they are compatible, load the item
                    self._slot1.load(item)
                    return True
        elif position == 2:
            # if both slots are empty, load it
            if not self._slot2.has_item:
                if not self._slot1.has_item:
                    self._slot2.load(item)
                    return True
                # if one slot has an item in it, check that it is compatible
                elif self._slot1.item().is_compatible(item):
                    # if they are compatible, load the item
                    self._slot2.load(item)
                    return True
        return False

    def unload_slot(self, position) -> Union[NuclearItem, bool]:
        """Unload a slot"""
        if position == 1 and self._slot1.has_item:
            item = self._slot1.item()
            self._slot1.unload()
            return item
        elif position == 2 and self._slot2.has_item:
            item = self._slot2.item()
            self._slot2.unload()
            return item
        return False

    def travel(self, direction: Direction) -> bool:
        """Move in the specified direction (Up or Down)"""
        if direction == Direction.UP:
            if self._floor != self.MAX_FLOOR:
                self._floor += 1
                return True
            return False
        elif direction == Direction.DOWN:
            if self._floor != 1:
                self._floor -= 1
                return True
            return False

class Facility:
    """A sealed, 4 floor, RTG assembly area"""

    FLOORS = 4

    def __init__(self):
        self._floors = {
            1: [],
            2: [],
            3: [],
            4: [],
        }

    def add_item(self, floor, item) -> bool:
        """Add an item to a floor of the facility"""
        if item not in self._floors[floor]:
            self._floors[floor].append(item)
            return True
        return False

    def remove_item(self, floor, item) -> Union[NuclearItem, bool]:
        """Remove an item from a floor of the facility"""
        if item in self._floors[floor]:
            return self._floors[floor].pop(self._floors[floor].index(item))
        return False

    def find_item(self, item) -> Union[int, bool]:
        """Find an item in the facility, returning the floor number or False"""
        for floor in self._floors.items():
            if item in floor[1]:
                return floor[0]
        return False
