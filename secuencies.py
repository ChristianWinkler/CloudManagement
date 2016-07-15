from elements import *

class Sequence:
    def execute(self, driver_factory, config):
        raise NotImplementedError

class OpenLogin(Sequence):
    def execute(self, driver, config):
        Open().execute(driver, config)
        Login().execute(driver, config) 
        
class OpenLoginClose(Sequence):
    def execute(self, driver, config):
        Open().execute(driver, config)
        Login().execute(driver, config)
        Close().execute(driver, config)