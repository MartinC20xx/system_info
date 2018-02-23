# -*- coding: utf-8 -*-

#from .context import systeminfo
#importing via context seems to stop me from using the from x import y, which is all that seems to work
from systeminfo import main

import unittest
from wheel.signatures import assertTrue


class TestSystemInfo(unittest.TestCase):
    """Sample test."""

    #def test_PrintPlatform(self):
     #   output = main.printPlatform()
      #  self.assertEqual(main.printPlatform(), output)
    
   # def test_Main(self):
    #    output = main.main()
     #   self.assertIsNotNone(main.printMachineName())
     


if __name__ == '__main__':
    unittest.main()