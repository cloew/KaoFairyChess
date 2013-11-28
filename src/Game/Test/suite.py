import unittest

from Game.Player.Test.suite import suite as player_suite

suites = [player_suite]
suite = unittest.TestSuite(suites)