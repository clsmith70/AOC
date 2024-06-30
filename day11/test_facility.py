# test_facility.py
import unittest
from facility import Elevator, Facility, Generator, Microchip, Direction

class FacilityTestCase(unittest.TestCase):
    """Test the facility elements"""
    elevator = Elevator()
    facility = Facility()

    def test_nuclearitem(self):
        """Test compatibility between chips and generators"""
        chip1 = Microchip("tritium")
        gen1 = Generator("tritium")
        chip2 = Microchip("thulium")
        gen2 = Generator("thulium")

        # chip1 and gen1 should be compatible
        self.assertTrue(chip1.is_compatible(gen1))
        # gen2 and chip2 should be compatible (opposite check)
        self.assertTrue(gen2.is_compatible(chip2))
        # gen1 and chip2 should be incompatible
        self.assertFalse(gen1.is_compatible(chip2))
        # chip2 and gen1 should be incompatible (opposite check)
        self.assertFalse(chip2.is_compatible(gen1))
        # gen1 should return the element tritium
        self.assertEqual(gen1.get_element, "tritium")
        # chip2 should return the element thulium
        self.assertEqual(chip2.get_element, "thulium")

    def test_elevator(self):
        """Test the elevator object"""
        elevator = Elevator()
        chip1 = Microchip("tritium")
        gen1 = Generator("tritium")
        chip2 = Microchip("thulium")
        gen2 = Generator("thulium")

        # the elevator should not be able to move (empty)
        self.assertFalse(elevator.can_move)
        # the elevator should be on floor 1
        self.assertEqual(elevator.get_floor, 1)
        # the elevator is empty, first item should load ok
        self.assertTrue(elevator.load_slot(1, chip1))
        # the elevator has an item loaded, it should be able to move
        self.assertTrue(elevator.can_move)
        # this generator does not match the chip, load should fail
        self.assertFalse(elevator.load_slot(2, gen2))
        # a second chip should load ok
        self.assertTrue(elevator.load_slot(2, chip2))
        # the elevator should be full
        self.assertTrue(elevator.is_full)
        # the matching generator cannot be loaded while the elevator is full
        self.assertFalse(elevator.load_slot(2, gen1))
        # unloading the second slot should return chip2
        self.assertEqual(elevator.unload_slot(2), chip2)
        # the elevator should no longer be full
        self.assertFalse(elevator.is_full)
        # loading the matching generator should be okay
        self.assertTrue(elevator.load_slot(2, gen1))
        # the fully loaded elevator should return two items
        self.assertEqual(elevator.get_slots(), \
                ("Slot 1 contains Microchip of tritium",
                 'Slot 2 contains Generator of tritium'))
        # the elevator should not be able to travel down (on floor 1)
        self.assertFalse(elevator.travel(Direction.DOWN))
        # the elevator can travel up
        self.assertTrue(elevator.travel(Direction.UP))
        # the elevator should now be on floor 2
        self.assertEqual(elevator.get_floor, 2)

        # unload the elevator completely
        for i in range(1, 3):
            elevator.unload_slot(i)
        # it should report empty
        self.assertFalse(elevator.is_full)
        # it should not be able to move
        self.assertFalse(elevator.can_move)
        
    def test_facility(self):
        """Test the facility object"""
        chip1 = Microchip("tritium")
        gen1 = Generator("tritium")
        chip2 = Microchip("thulium")
        gen2 = Generator("thulium")
        facility = Facility()

        # test adding items
        self.assertTrue(facility.add_item(2, chip1))
        self.assertTrue(facility.add_item(3, gen2))

        # test searching for an item not on any floor
        self.assertFalse(facility.find_item(gen1))
        self.assertFalse(facility.find_item(chip2))

        # test searching for an item on a floor
        self.assertEqual(facility.find_item(chip1), 2)
        self.assertEqual(facility.find_item(gen2), 3)

        # test removing an item
        self.assertEqual(facility.remove_item(3, gen2), gen2)

if __name__ == "__main__":
    unittest.main()
