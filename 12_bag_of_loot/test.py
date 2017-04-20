import unittest
from lootbag import bag_o_loot

class TestBagOfLootMethods(unittest.TestCase):   

    @classmethod
    def setUpClass(self):
        self.bag = bag_o_loot()

    def test_add_toy_to_bag(self):
        self.bag.add_present('Vincent', 'Ball')
        vincent_toys = self.bag.list_presents('Vincent')

        self.assertIsInstance(vincent_toys, list)
        self.assertIn('Ball', vincent_toys)

    def test_remove_toy_of_child(self):
        toy = 'Slinky'
        self.bag.add_present('Vincent', toy)

        self.assertIn('Vincent', self.bag.list_children())

        self.bag.remove_present('Vincent', toy)
        vincent_toys = self.bag.list_presents('Vincent')

        self.assertNotIn(toy, vincent_toys)

    def test_list_of_children_recieving_presents(self):
        self.bag.add_present('Vincent', 'Slinky')
        list_of_children = bag.list_children()

        self.assertIsInstance(list_of_children, list)
        self.assertIn('Vincent', list_of_children)

    def test_list_of_presents_for_one_child(self):
        toy = 'Slime'
        self.bag.add_present('Vincent', toy)
        vincent_toys = self.bag.list_presents('Vincent')

        self.assertIsInstance(vincent_toys, list)
        self.assertIn(toy, vincent_toys)

    def test_child_toys_are_delivers(self):
        toy = 'Pony'
        self.bag.add_present('Vincent', toy)
        vincent_before = self.bag.get_if_delivered('Vincent')
        self.bag.deliver_to_child('Vincent')
        vincent_after = self.bag.get_if_delivered('Vincent')

        self.assertIs(vincent, dict)
        self.assertFalse(vincent['delivered'])

        self.bag.deliver_toys_to_child('Vincent')
        self.assertTrue(vincent['delivered'])


if __name__ == '__main__':
    unittest.main()


