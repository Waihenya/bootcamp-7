
 #Test suite for super_sum

import unittest 
from super_sum import super_sum

# Test case for super_sum.

class SuperSumTestCase(unittest.TestCase):

#Test empty input.
	def test_empty_input(self):

		self.assertEqual(super_sum(), 0)

#Test sum of integers.
	def test_sum_of_integers(self):

		self.assertEqual(super_sum(1, 2, 3), 6)
		self.assertEqual(super_sum(-1, 1), 0)
		self.assertNotEqual(super_sum(10, 20,30), 100)

 #Test some of items in a single list

	def test_sum_of_items_in_a_list(self):
		self.assertEqual(super_sum([1, 2, 3]), 6) 

 #Test whether input is a string and returns 0

	def test_string_input_returns(self):
		self.assertEqual(super_sum("string", 1 ,4), 0)				



 