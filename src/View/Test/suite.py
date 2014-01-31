import unittest

from View.Console.Test.suite import suite as console_suite

suites = [console_suite]
suite = unittest.TestSuite(suites)