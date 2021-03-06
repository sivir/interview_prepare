#!/usr/bin/env python

import unittest
import random
import copy

import insertionsort

class TestInertionsort(unittest.TestCase):
  def test_random_data(self):
    data = [ random.randint(0,100) for _ in range(0, 50) ] 
    sorted_data  = copy.copy(data)
    sorted_data.sort()
    insertionsort.sort(data)
    self.assertEqual(data,sorted_data)


if __name__ == '__main__':
  unittest.main()
