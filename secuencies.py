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
        
class OpenLoginNewLocation(Sequence):
    def execute(self, driver, config):
        OpenLogin().execute(driver, config)
        addLocation().execute(driver, config)
        
class OpenLoginDeleteLocationsClose(Sequence):
    def execute(self, driver, config):
        OpenLogin().execute(driver, config)
        deleteLocations().execute(driver, config)
        Close().execute(driver, config)

class OpenLoginNewLocationClose(Sequence):
    def execute(self, driver, config):
        OpenLogin().execute(driver, config)
        addLocation().execute(driver, config)
        Close().execute(driver, config)
        
class OpenLoginNewLocation3Close(Sequence):
    def execute(self, driver, config):
        OpenLogin().execute(driver, config)
        addLocation().execute(driver, config)
        addLocation().execute(driver, config)
        addLocation().execute(driver, config)
        Close().execute(driver, config)
        
class OpenLoginLocationlistClose(Sequence):
    def execute(self, driver, config):
        Open().execute(driver, config)
        Login().execute(driver, config)
        doLocationList().execute(driver, config)
        Close().execute(driver, config)
