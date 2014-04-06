import pickle
import unittest
from pickler import list_pickler, unpickler

class TDDPickler(unittest.TestCase):

	def setUp(self):
		self.original_list = ['jill', 'zoe', 'kevin']
		self.fil_name = 'pick.p'

	def test_unpickler_returns_same_list_as_original(self):
		pick_list = list_pickler(self.original_list, self.fil_name)
		self.assertEqual(self.original_list, unpickler(self.fil_name))
	