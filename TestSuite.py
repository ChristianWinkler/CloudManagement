import sys
import unittest
import AddDevice
import AddLocation

class Test_Suite(unittest.TestCase):
    
    def test_main(self):
        
        self.suite = unittest.TestSuite()
        self.suite.addTests([
                             unittest.defaultTestLoader.loadTestsFromTestCase(AddLocation.addLocations),
                             unittest.defaultTestLoader.loadTestsFromTestCase(AddDevice.addDevice),
                             ])
        runner = unittest.TextTestRunner()
        runner.run(self.suite)
        
if __name__ == "__main__":
    unittest.main()