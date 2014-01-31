from Game.game import Game
from View.Console.Board.tile_picker_controller import TilePickerController

import unittest

class getIndex(unittest.TestCase):
    """ Test cases of getIndex """
    
    def  setUp(self):
        """ Build the Controller for the test """
        self.controller = TilePickerController(None, Game())
        
    def contains(self):
        """ Test that when the text contains the value the proper index is returned """
        text = '3'
        lineString = '12345'
        
        index = self.controller.getIndex(text, lineString)
        assert index is not None, "Should contain the text"
        assert index == 2, "The index should be the second element in the list"
        
    def missing(self):
        """ Test that when the text is missing None is returned """
        text = 'a'
        lineString = '12345'
        
        index = self.controller.getIndex(text, lineString)
        assert index is None, "Should not contain the text"

# Collect all test cases in this class
testcasesFunctionToTest = ["contains", "missing"]
suiteFunctionToTest = unittest.TestSuite(map(getIndex, testcasesFunctionToTest))

##########################################################

# Collect all test cases in this file
suites = [suiteFunctionToTest]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)